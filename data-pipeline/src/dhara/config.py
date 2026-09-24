"""
DHARĀ Pipeline Configuration
==============================
All scientific constants live here. Changing a threshold in one place
changes it everywhere — no magic numbers scattered across the codebase.

WARNING: Before changing any threshold, read P4.2 (Threshold Calibration).
Changes must be validated against the COOLR precision/recall evaluation and
documented in docs/METHODOLOGY.md before being committed to main.
"""
from pathlib import Path
from typing import Final

# ---------------------------------------------------------------------------
# Repository layout — all paths relative to this file's parent
# ---------------------------------------------------------------------------
PACKAGE_ROOT: Final[Path] = Path(__file__).parent
PIPELINE_ROOT: Final[Path] = PACKAGE_ROOT.parent.parent
DATA_ROOT: Final[Path] = PIPELINE_ROOT / "data"

RAW_DATA_DIR: Final[Path] = DATA_ROOT / "raw"
ANCILLARY_DIR: Final[Path] = DATA_ROOT / "ancillary"
PROCESSED_DIR: Final[Path] = DATA_ROOT / "processed"
VALIDATION_DIR: Final[Path] = DATA_ROOT / "validation"

# ---------------------------------------------------------------------------
# InSAR / GUNW processing constants
# ---------------------------------------------------------------------------

# Coherence mask threshold (P2.1).
# Pixels with coherence < this value are set to NaN — never treated as zero.
# Justification: 0.3 is a standard conservative threshold for C-band SAR;
# values below this indicate phase noise dominates over signal.
# Calibration sweep range: [0.2, 0.5] — see P4.2.
COHERENCE_THRESHOLD: Final[float] = 0.3

# ---------------------------------------------------------------------------
# Velocity / acceleration thresholds (P3.1, P3.2)
# ---------------------------------------------------------------------------

# Minimum velocity magnitude (mm/year, LOS) to flag a pixel as anomalous.
# Justification: NISAR's stated LOS displacement precision is ~2-5 mm;
# flagging below 5 mm/yr risks drowning in noise.
# Calibration sweep range: [3, 15] — see P4.2.
MIN_VELOCITY_MM_PER_YEAR: Final[float] = 5.0

# Quadratic coefficient threshold for classifying trend as "accelerating" vs "steady".
# Units: mm/year^2. Pixels whose |quadratic term| >= this are "accelerating".
# Justification: derived from expected seasonal noise amplitude in the region;
# acceleration below 1 mm/yr² is within typical seasonal noise.
ACCELERATION_THRESHOLD_MM_PER_YEAR_SQ: Final[float] = 1.0

# ---------------------------------------------------------------------------
# Event clustering (P3.2)
# ---------------------------------------------------------------------------

# Minimum cluster area to survive (dropped if smaller than this).
# In pixels — converted to km² at runtime using the product's pixel spacing.
# Justification: clusters < 4 pixels are more likely noise artifacts than
# real slope deformation signals.
MIN_CLUSTER_PIXELS: Final[int] = 4

# Approximate real-world minimum area in km² (for reporting and sanity checks).
# This is derived from MIN_CLUSTER_PIXELS * (pixel_spacing_m)^2 at 80m NISAR resolution.
MIN_CLUSTER_AREA_KM2: Final[float] = 0.05

# ---------------------------------------------------------------------------
# Confidence scoring weights (P3.3)
# DO NOT CHANGE THESE WEIGHTS without updating docs/METHODOLOGY.md.
# These are the exact weights from the DHARĀ spec — any change breaks the
# promise made in the project methodology.
# ---------------------------------------------------------------------------
CONF_WEIGHT_DATA_QUALITY: Final[float] = 0.25
CONF_WEIGHT_TEMPORAL_PERSISTENCE: Final[float] = 0.25
CONF_WEIGHT_SPATIAL_COHERENCE: Final[float] = 0.20
CONF_WEIGHT_CROSS_SOURCE_AGREEMENT: Final[float] = 0.15
CONF_WEIGHT_MODEL_VALIDITY: Final[float] = 0.15

# Sanity check: weights must sum to 1.0
assert abs(
    CONF_WEIGHT_DATA_QUALITY
    + CONF_WEIGHT_TEMPORAL_PERSISTENCE
    + CONF_WEIGHT_SPATIAL_COHERENCE
    + CONF_WEIGHT_CROSS_SOURCE_AGREEMENT
    + CONF_WEIGHT_MODEL_VALIDITY
    - 1.0
) < 1e-9, "Confidence weights must sum to exactly 1.0"

# Confidence tier thresholds
CONF_TIER_HIGH_THRESHOLD: Final[float] = 0.75
CONF_TIER_MODERATE_THRESHOLD: Final[float] = 0.50  # >= moderate, < high

# Model validity score for clusters outside the validated Sentinel-1 region
CONF_MODEL_VALIDITY_UNVALIDATED: Final[float] = 0.60

# ---------------------------------------------------------------------------
# Cross-source agreement thresholds (P3.3)
# ---------------------------------------------------------------------------

# Minimum recent rainfall (mm, 30-day accumulation) to count as a corroborating check.
RAINFALL_THRESHOLD_MM: Final[float] = 100.0

# Minimum slope (degrees from DEM) to count as a corroborating check.
# Justification: slopes < 15° rarely produce rapid mass movement in Nepal's geology.
SLOPE_THRESHOLD_DEGREES: Final[float] = 15.0

# Look-back window for seismic history check (years).
SEISMIC_HISTORY_YEARS: Final[int] = 20

# Minimum earthquake magnitude to count.
SEISMIC_MIN_MAGNITUDE: Final[float] = 4.5

# Search radius for seismic events (km from AOI centroid).
SEISMIC_SEARCH_RADIUS_KM: Final[float] = 200.0

# ---------------------------------------------------------------------------
# Validation (P4.1)
# ---------------------------------------------------------------------------

# Spatial tolerance for matching detected cluster to COOLR event (km).
# Justification: COOLR location accuracy is variable; 5 km is conservative
# but avoids spurious matches across different sub-watersheds.
VALIDATION_SPATIAL_TOLERANCE_KM: Final[float] = 5.0

# Temporal tolerance for matching detected cluster to COOLR event (days).
# Justification: COOLR events are often reported days to weeks after the event;
# 30 days allows for reporting lag without spanning multiple monsoon seasons.
VALIDATION_TEMPORAL_TOLERANCE_DAYS: Final[int] = 30

# ---------------------------------------------------------------------------
# AOI definitions
# ---------------------------------------------------------------------------

# Primary flagship AOI: Sindhupalchowk / Melamchi watershed, Nepal
AOI_NEPAL_BBOX: Final[tuple[float, float, float, float]] = (
    85.2, 27.8, 86.1, 28.4  # (lon_min, lat_min, lon_max, lat_max)
)
AOI_NEPAL_NAME: Final[str] = "nepal_flagship"
AOI_NEPAL_CENTROID: Final[tuple[float, float]] = (85.65, 28.1)  # (lon, lat)

# Secondary AOI: TBD after P1.1 coverage check confirms data availability.
# Do not hardcode here until P1.1 is run and coverage is confirmed.
AOI_SECONDARY_NAME: Final[str] = "secondary_tbd"

# ---------------------------------------------------------------------------
# NISAR / data product constants
# ---------------------------------------------------------------------------

# ASF minimum acquisitions needed for a usable time series
MIN_ACQUISITIONS_FOR_TIMESERIES: Final[int] = 4

# NISAR GCOV backscatter water mask threshold (dB)
# Pixels below this dB value are classified as water (open water ~ -15 to -20 dB)
# Justification: land surfaces typically return > -12 dB; water << -12 dB
WATER_MASK_BACKSCATTER_THRESHOLD_DB: Final[float] = -12.0

# Flood extent change threshold — percent area growth to flag as candidate flood
FLOOD_EXTENT_CHANGE_THRESHOLD_PCT: Final[float] = 20.0

# Glacier velocity change threshold (m/year) for flagging speed-up events
GLACIER_VELOCITY_CHANGE_THRESHOLD_M_PER_YEAR: Final[float] = 5.0
