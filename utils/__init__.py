"""
Utility package for CareerConsultant.

This package provides shared utilities such as:
- Data processing
- Recommendation engine logic
- Helper functions for cross-module use
"""

from .data_processor import DataProcessor
from .recommendation_engine import RecommendationEngine

__all__ = ["DataProcessor", "RecommendationEngine"]
