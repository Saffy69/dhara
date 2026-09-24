# Change Passport Schema
(authoritative — use exactly this shape everywhere)

```json
{
  "event_id": "string",
  "hazard_type": "slow_slope_deformation | glacier_motion | flood_extent_change | land_subsidence",
  "aoi_name": "string",
  "centroid": { "lat": 0.0, "lon": 0.0 },
  "area_km2": 0.0,
  "first_detected": "YYYY-MM-DD",
  "last_confirmed": "YYYY-MM-DD",
  "observation_count": 0,
  "displacement": {
    "mean_velocity_mm_per_year": 0.0,
    "trend": "accelerating | steady | decelerating",
    "line_of_sight_only": true
  },
  "confidence": {
    "overall_score": 0.0,
    "tier": "High | Moderate | Low",
    "components": {
      "data_quality": 0.0,
      "temporal_persistence": 0.0,
      "spatial_coherence": 0.0,
      "cross_source_agreement": 0.0,
      "model_validity": 0.0
    }
  },
  "alternative_explanations_checked": [
    { "explanation": "string", "ruled_out": true, "basis": "string" }
  ],
  "supporting_evidence": {
    "recent_rainfall_mm": 0.0,
    "slope_degrees": 0.0,
    "known_seismic_history": false
  },
  "validation": {
    "matched_to_coolr_event": true,
    "coolr_event_id": "string or null",
    "detection_lead_time_days": 0,
    "validation_leg": "sentinel1_historical | nisar_live"
  },
  "data_provenance": {
    "product": "GUNW | GOFF | GCOV | Sentinel-1 SBAS",
    "maturity": "PROVISIONAL | validation-leg",
    "crid_or_processor": "string",
    "source_urls": ["string"]
  },
  "recommended_next_step": "string",
  "not_an_emergency_alert_disclaimer": true
}
```
