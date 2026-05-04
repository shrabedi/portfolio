"""DataVault - Data Processing & Transformation Utility."""

__version__ = "1.0.0"
__author__ = "Hussain Raza Abedi"

from datavault.core.processor import DataProcessor
from datavault.validators.schema import SchemaValidator

__all__ = ["DataProcessor", "SchemaValidator"]
