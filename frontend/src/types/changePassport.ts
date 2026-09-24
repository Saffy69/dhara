/**
 * TypeScript type definitions for the DHARĀ Change Passport.
 * 
 * CRITICAL: This type MUST stay in sync with:
 *   - docs/tasks/00_Change_Passport_Schema.md (the authoritative JSON schema)
 *   - api/app/schemas/change_passport.json (the JSON Schema validator)
 *   - data-pipeline/src/dhara/models/change_passport.py (the Python dataclass)
 * 
 * If you change this type, you MUST update all three counterparts.
 * A mismatch here causes silent data corruption across the entire system.
 */

export type HazardType =
  | 'slow_slope_deformation'
  | 'glacier_motion'
  | 'flood_extent_change'
  | 'land_subsidence'

export type ConfidenceTier = 'High' | 'Moderate' | 'Low'

export type DisplacementTrend = 'accelerating' | 'steady' | 'decelerating'

export type ValidationLeg = 'sentinel1_historical' | 'nisar_live'

export type DataProduct = 'GUNW' | 'GOFF' | 'GCOV' | 'Sentinel-1 SBAS'

export interface ConfidenceComponents {
  /** Fraction of non-masked, PROVISIONAL-or-better pixels in the cluster [0..1] */
  data_quality: number
  /** Fraction of time steps where anomaly reappears at same location [0..1] */
  temporal_persistence: number
  /** Mean InSAR coherence across cluster pixels [0..1] */
  spatial_coherence: number
  /** 0 | 0.33 | 0.67 | 1.0 based on 0/1/2/3 ancillary checks passing */
  cross_source_agreement: number
  /** 1.0 if in validated S1 region, else 0.6 for NISAR-only */
  model_validity: number
}

export interface Confidence {
  /** Weighted sum: 0.25*dq + 0.25*tp + 0.20*sc + 0.15*csa + 0.15*mv */
  overall_score: number
  tier: ConfidenceTier
  components: ConfidenceComponents
}

export interface Displacement {
  mean_velocity_mm_per_year: number
  trend: DisplacementTrend
  /** true = LOS displacement only; never interpret as vertical without decomposition */
  line_of_sight_only: boolean
}

export interface AlternativeExplanation {
  explanation: string
  ruled_out: boolean
  basis: string
}

export interface SupportingEvidence {
  recent_rainfall_mm: number
  slope_degrees: number
  known_seismic_history: boolean
}

export interface ValidationInfo {
  matched_to_coolr_event: boolean
  coolr_event_id: string | null
  /** Positive = detected before COOLR report; negative = detected after */
  detection_lead_time_days: number
  validation_leg: ValidationLeg
}

export interface DataProvenance {
  product: DataProduct
  maturity: 'PROVISIONAL' | 'validation-leg'
  crid_or_processor: string
  source_urls: string[]
}

export interface ChangePassport {
  event_id: string
  hazard_type: HazardType
  aoi_name: string
  centroid: { lat: number; lon: number }
  area_km2: number
  first_detected: string  // YYYY-MM-DD
  last_confirmed: string  // YYYY-MM-DD
  observation_count: number
  displacement: Displacement
  confidence: Confidence
  alternative_explanations_checked: AlternativeExplanation[]
  supporting_evidence: SupportingEvidence
  validation: ValidationInfo
  data_provenance: DataProvenance
  recommended_next_step: string
  /** MUST be true — enforced by JSON Schema validator in the pipeline */
  not_an_emergency_alert_disclaimer: true
}
