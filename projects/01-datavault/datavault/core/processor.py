"""Data processing engine for DataVault."""

from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import pandas as pd


class DataProcessor:
    """Main data processing engine supporting multiple formats."""

    def __init__(self, source: Union[str, Path], format: Optional[str] = None):
        """
        Initialize DataProcessor.

        Args:
            source: File path or data source
            format: Data format (csv, json, parquet)
        """
        self.source = Path(source)
        self.format = format or self.source.suffix.lstrip(".")
        self.data: pd.DataFrame = None
        self._load()

    def _load(self) -> None:
        """Load data from source."""
        if self.format == "csv":
            self.data = pd.read_csv(self.source)
        elif self.format == "json":
            self.data = pd.read_json(self.source)
        elif self.format == "parquet":
            self.data = pd.read_parquet(self.source)
        else:
            raise ValueError(f"Unsupported format: {self.format}")

    def filter(self, **kwargs) -> "DataProcessor":
        """
        Filter data based on conditions.

        Args:
            **kwargs: Filter conditions (e.g., amount__gte=1000)

        Returns:
            Self for chaining
        """
        for col, value in kwargs.items():
            if "__" in col:
                col_name, op = col.rsplit("__", 1)
                if op == "gte":
                    self.data = self.data[self.data[col_name] >= value]
                elif op == "lte":
                    self.data = self.data[self.data[col_name] <= value]
                elif op == "eq":
                    self.data = self.data[self.data[col_name] == value]
                elif op == "in":
                    self.data = self.data[self.data[col_name].isin(value)]
            else:
                self.data = self.data[self.data[col] == value]
        return self

    def aggregate(self, aggs: Dict[str, str], group_by: Optional[List[str]] = None) -> "DataProcessor":
        """
        Aggregate data.

        Args:
            aggs: Aggregation spec (e.g., {'total': 'sum'})
            group_by: Columns to group by

        Returns:
            Self for chaining
        """
        if group_by:
            self.data = self.data.groupby(group_by).agg(aggs).reset_index()
        else:
            self.data = self.data.agg(aggs).to_frame().T
        return self

    def pivot(self, index: str, columns: str, values: str, aggfunc: str = "sum") -> "DataProcessor":
        """Pivot table transformation."""
        self.data = self.data.pivot_table(
            index=index, columns=columns, values=values, aggfunc=aggfunc
        )
        return self

    def to_csv(self, path: Union[str, Path], **kwargs) -> None:
        """Export to CSV."""
        self.data.to_csv(path, index=False, **kwargs)

    def to_json(self, path: Union[str, Path], **kwargs) -> None:
        """Export to JSON."""
        self.data.to_json(path, orient="records", **kwargs)

    def to_parquet(self, path: Union[str, Path], **kwargs) -> None:
        """Export to Parquet."""
        self.data.to_parquet(path, index=False, **kwargs)

    def describe(self) -> Dict[str, Any]:
        """Get data statistics."""
        return {
            "shape": self.data.shape,
            "columns": list(self.data.columns),
            "dtypes": self.data.dtypes.to_dict(),
            "memory": str(self.data.memory_usage(deep=True).sum()),
        }

    def __repr__(self) -> str:
        return f"DataProcessor(shape={self.data.shape}, format={self.format})"
