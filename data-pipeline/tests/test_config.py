"""
Sanity tests for the config module.
Run with: pytest data-pipeline/tests/test_config.py
"""
import pytest
from dhara.config import (
    CONF_WEIGHT_DATA_QUALITY,
    CONF_WEIGHT_TEMPORAL_PERSISTENCE,
    CONF_WEIGHT_SPATIAL_COHERENCE,
    CONF_WEIGHT_CROSS_SOURCE_AGREEMENT,
    CONF_WEIGHT_MODEL_VALIDITY,
    COHERENCE_THRESHOLD,
    CONF_TIER_HIGH_THRESHOLD,
    CONF_TIER_MODERATE_THRESHOLD,
)


def test_confidence_weights_sum_to_one() -> None:
    """The five confidence weights must sum exactly to 1.0."""
    total = (
        CONF_WEIGHT_DATA_QUALITY
        + CONF_WEIGHT_TEMPORAL_PERSISTENCE
        + CONF_WEIGHT_SPATIAL_COHERENCE
        + CONF_WEIGHT_CROSS_SOURCE_AGREEMENT
        + CONF_WEIGHT_MODEL_VALIDITY
    )
    assert abs(total - 1.0) < 1e-9, f"Weights sum to {total}, not 1.0"


def test_coherence_threshold_in_valid_range() -> None:
    """Coherence threshold must be between 0 and 1."""
    assert 0.0 < COHERENCE_THRESHOLD < 1.0


def test_confidence_tier_thresholds_ordered() -> None:
    """High threshold must be greater than Moderate threshold."""
    assert CONF_TIER_HIGH_THRESHOLD > CONF_TIER_MODERATE_THRESHOLD
    assert CONF_TIER_MODERATE_THRESHOLD > 0.0
