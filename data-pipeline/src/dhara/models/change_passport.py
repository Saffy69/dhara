"""
DHARĀ Change Passport — Python dataclass representation.

The authoritative schema is in docs/tasks/00_Change_Passport_Schema.md.
This dataclass mirrors that schema exactly. The JSON Schema validator
(api/app/schemas/change_passport.json) is generated from this module.

Any change here MUST be reflected in:
  - frontend/src/types/changePassport.ts
  - api/app/schemas/change_passport.json
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

HazardType = Literal[
    "slow_slope_deformation",
    "glacier_motion",
    "flood_extent_change",
    "land_subsidence",
]

DisplacementTrend = Literal["accelerating", "steady", "decelerating"]

ConfidenceTier = Literal["High", "Moderate", "Low"]

DataProduct = Literal["GUNW", "GOFF", "GCOV", "Sentinel-1 SBAS"]

DataMaturity = Literal["PROVISIONAL", "validation-leg"]

ValidationLeg = Literal["sentinel1_historical", "nisar_live"]


@dataclass
class ConfidenceComponents:
    data_quality: float           # [0..1]
    temporal_persistence: float   # [0..1]
    spatial_coherence: float      # [0..1]
    cross_source_agreement: float # 0 | 0.33 | 0.67 | 1.0
    model_validity: float         # 0.6 | 1.0


@dataclass
class Confidence:
    overall_score: float
    tier: ConfidenceTier
    components: ConfidenceComponents


@dataclass
class Displacement:
    mean_velocity_mm_per_year: float
    trend: DisplacementTrend
    line_of_sight_only: bool = True  # Always True for LOS InSAR — never assume vertical


@dataclass
class AlternativeExplanation:
    explanation: str
    ruled_out: bool
    basis: str


@dataclass
class SupportingEvidence:
    recent_rainfall_mm: float
    slope_degrees: float
    known_seismic_history: bool


@dataclass
class ValidationInfo:
    matched_to_coolr_event: bool
    coolr_event_id: str | None
    detection_lead_time_days: int
    validation_leg: ValidationLeg


@dataclass
class DataProvenance:
    product: DataProduct
    maturity: DataMaturity
    crid_or_processor: str
    source_urls: list[str] = field(default_factory=list)


@dataclass
class ChangePassport:
    event_id: str
    hazard_type: HazardType
    aoi_name: str
    centroid: dict  # {"lat": float, "lon": float}
    area_km2: float
    first_detected: str   # YYYY-MM-DD
    last_confirmed: str   # YYYY-MM-DD
    observation_count: int
    displacement: Displacement
    confidence: Confidence
    alternative_explanations_checked: list[AlternativeExplanation]
    supporting_evidence: SupportingEvidence
    validation: ValidationInfo
    data_provenance: DataProvenance
    recommended_next_step: str
    not_an_emergency_alert_disclaimer: bool = True  # MUST always be True

    def __post_init__(self) -> None:
        if not self.not_an_emergency_alert_disclaimer:
            raise ValueError(
                "not_an_emergency_alert_disclaimer must be True in every Change Passport. "
                "DHARĀ is not an emergency alert system."
            )
