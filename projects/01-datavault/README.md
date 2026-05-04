# DataVault

A powerful Python utility for data processing, transformation, and validation. Handle CSV, JSON, and SQL data with ease.

## Features

- **Multi-format Support**: CSV, JSON, Parquet, SQL databases
- **Data Transformation**: Filter, aggregate, pivot, and reshape data
- **Validation Framework**: Schema validation and data quality checks
- **Performance**: Optimized for large datasets using pandas and polars
- **CLI Interface**: Command-line tools for batch operations
- **Testing**: Comprehensive test suite with 90%+ coverage

## Quick Start

```bash
pip install -r requirements.txt

# Transform CSV to JSON
python -m datavault transform input.csv output.json --format json

# Validate data
python -m datavault validate data.csv --schema schema.json

# Aggregate data
python -m datavault aggregate sales.csv --group-by region --sum amount
```

## Installation

```bash
git clone https://github.com/shrabedi/portfolio.git
cd portfolio/projects/01-datavault
pip install -r requirements.txt
```

## Usage

### As a Library

```python
from datavault import DataProcessor

processor = DataProcessor("data.csv")
result = processor.filter(amount__gte=1000).aggregate({"total": "sum"})
result.to_json("output.json")
```

### Command Line

```bash
datavault transform input.csv output.parquet --format parquet
datavault validate data.csv --rules validation_rules.yaml
datavault stats data.csv --output stats.json
```

## Architecture

- `datavault/core/` - Core processing engine
- `datavault/transforms/` - Transformation functions
- `datavault/validators/` - Validation framework
- `datavault/cli/` - Command-line interface
- `tests/` - Test suite

## Performance

- Handles 1M+ rows efficiently
- Streaming support for large files
- In-memory and out-of-core processing options
- Parallel processing for multi-core systems

## Testing

```bash
pytest tests/ -v --cov=datavault
```

## License

MIT

## Author

Hussain Raza Abedi
