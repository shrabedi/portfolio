"""Tests for DataProcessor."""

import tempfile
from pathlib import Path

import pandas as pd
import pytest

from datavault.core.processor import DataProcessor


@pytest.fixture
def sample_csv():
    """Create sample CSV file."""
    data = {
        "id": [1, 2, 3, 4, 5],
        "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "amount": [100, 200, 150, 300, 250],
        "region": ["USA", "USA", "Europe", "Europe", "Asia"],
    }
    df = pd.DataFrame(data)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        df.to_csv(f.name, index=False)
        yield f.name
    Path(f.name).unlink()


def test_load_csv(sample_csv):
    """Test CSV loading."""
    processor = DataProcessor(sample_csv, format="csv")
    assert processor.data.shape == (5, 4)


def test_filter(sample_csv):
    """Test filtering."""
    processor = DataProcessor(sample_csv, format="csv")
    result = processor.filter(amount__gte=200)
    assert len(result.data) == 3


def test_aggregate(sample_csv):
    """Test aggregation."""
    processor = DataProcessor(sample_csv, format="csv")
    result = processor.aggregate({"amount": "sum"})
    assert result.data["amount"].iloc[0] == 1000


def test_export(sample_csv, tmp_path):
    """Test exporting to different formats."""
    processor = DataProcessor(sample_csv, format="csv")

    output_json = tmp_path / "output.json"
    processor.to_json(output_json)
    assert output_json.exists()
