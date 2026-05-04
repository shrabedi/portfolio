"""Schema validation for DataVault."""

from typing import Dict, List

import pandas as pd


class SchemaValidator:
    """Validate data against schema."""

    def __init__(self, schema: Dict[str, str]):
        """
        Initialize validator.

        Args:
            schema: Column name to type mapping
        """
        self.schema = schema
        self.issues: List[str] = []

    def validate(self, df: pd.DataFrame) -> Dict:
        """
        Validate DataFrame.

        Args:
            df: DataFrame to validate

        Returns:
            Validation report
        """
        self.issues = []
        actual_types = {col: str(dtype) for col, dtype in df.dtypes.items()}

        # Check missing columns
        missing = set(self.schema.keys()) - set(df.columns)
        if missing:
            self.issues.append(f"Missing columns: {missing}")

        # Check type mismatches
        for col, expected_type in self.schema.items():
            if col in actual_types:
                actual = actual_type_name(actual_types[col])
                expected = expected_type.lower()
                if actual != expected:
                    self.issues.append(f"Column {col}: expected {expected}, got {actual}")

        return {
            "valid": len(self.issues) == 0,
            "issues": self.issues,
            "missing_columns": list(missing),
        }


def expected_type_name(pandas_type: str) -> str:
    """Convert pandas type to schema type."""
    if "int" in pandas_type:
        return "int"
    elif "float" in pandas_type:
        return "float"
    elif "object" in pandas_type:
        return "string"
    elif "bool" in pandas_type:
        return "bool"
    elif "datetime" in pandas_type:
        return "datetime"
    return pandas_type
