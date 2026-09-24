# Week 1 Issues — Exit Criterion

**Exit Criterion:** A sane displacement time series running on real data for at least one test patch, for BOTH the Sentinel-1 validation leg AND the NISAR PROVISIONAL live leg.

---

## Issue 1 — Set up ASF search authentication
**Label:** pipeline | **Milestone:** Week 1  
**Summary:** Configure `.netrc` or environment variable auth for `asf_search` and verify login works without interactive prompt.  
**Acceptance Criterion:** Running `asf_search` against the Nepal AOI bbox in a fresh virtual environment authenticates and returns results without error. Document the setup in CONTRIBUTING.md.

---

## Issue 2 — P1.1: Run AOI coverage verification for Nepal flagship
**Label:** pipeline | **Milestone:** Week 1  
**Summary:** Run the coverage verification script (P1.1) for the Sindhupalchowk bbox and print a real coverage report.  
**Acceptance Criterion:** Script outputs a table showing exact acquisition dates and counts for (a) Sentinel-1 SLC/GUNW and (b) NISAR PROVISIONAL GUNW. Clearly states INSUFFICIENT COVERAGE if either has < 4 acquisitions. No assumed results — must come from a real ASF API call.

---

## Issue 3 — P1.1: Run AOI coverage verification for secondary AOI
**Label:** pipeline | **Milestone:** Week 1  
**Summary:** Choose a secondary subsidence AOI (Jakarta or Mexico City), run the same P1.1 coverage check, and confirm NISAR PROVISIONAL data is available.  
**Acceptance Criterion:** Real coverage report printed. Secondary AOI is locked in based on actual data availability, not assumed.

---

## Issue 4 — P1.2: Download first Sentinel-1 GUNW stack for Nepal
**Label:** pipeline | **Milestone:** Week 1  
**Summary:** Download the confirmed Sentinel-1 GUNW (or equivalent SBAS output) granules for Nepal across the confirmed date range. Populate manifest.json.  
**Acceptance Criterion:** At least 4 real `.h5` or raster files exist in `data/raw/nepal_flagship/`. `manifest.json` is valid JSON with source URLs and dates. Re-running the script does not re-download existing files.

---

## Issue 5 — P1.2: Download first NISAR PROVISIONAL GUNW granule for Nepal
**Label:** pipeline | **Milestone:** Week 1  
**Summary:** Download at least 1 real NISAR L2 GUNW PROVISIONAL granule for the Nepal AOI and log it in the manifest.  
**Acceptance Criterion:** Real NISAR `.h5` file exists in `data/raw/nepal_flagship/GUNW/`. Manifest entry includes CRID/processor field. If no PROVISIONAL GUNW exists for Nepal, document this honestly and pivot to the coverage-confirmed secondary AOI.

---

## Issue 6 — P2.1: Read one GUNW granule and apply coherence mask
**Label:** pipeline | **Milestone:** Week 1  
**Summary:** Implement and test the GUNW reader (P2.1) on one real downloaded granule. Produce a coherence-masked displacement raster.  
**Acceptance Criterion:** Running the reader on the real granule produces a raster where pixels with coherence < 0.3 are NaN. Verified visually with matplotlib. The threshold is the `COHERENCE_THRESHOLD` constant from `config.py`.

---

## Issue 7 — P3.1: Extract displacement time series for one test patch
**Label:** pipeline | **Milestone:** Week 1  
**Summary:** Stack all available displacement rasters for the Nepal AOI and extract the time series for a 3x3 pixel test patch with high coherence.  
**Acceptance Criterion:** A Python list/array of (date, displacement_mm) tuples exists for the test patch from real data. Values are in a physically sane range (not thousands of mm). At least 4 time steps are present.

---

## Issue 8 — P3.1: Fit velocity to the test patch time series
**Label:** pipeline | **Milestone:** Week 1  
**Summary:** Apply the least-squares linear velocity fit to the test patch time series from Issue 7.  
**Acceptance Criterion:** A real velocity value in mm/year is produced and printed. A known-answer unit test is written verifying the fitting function against a synthetic time series with hand-calculated velocity.

---

## Issue 9 — P1.3: Pull ancillary data (DEM + rainfall) for Nepal
**Label:** pipeline | **Milestone:** Week 1  
**Summary:** Download the Copernicus GLO-30 DEM tile(s) and GPM IMERG rainfall for the Nepal AOI and date range.  
**Acceptance Criterion:** DEM `.tif` exists in `data/ancillary/nepal_flagship/`. Slope raster is derived and visually sane (mountainous terrain, wide distribution). Rainfall data file exists with real dates.

---

## Issue 10 — P1.4: Pull COOLR ground truth for Nepal
**Label:** validation | **Milestone:** Week 1  
**Summary:** Query COOLR for all catalogued events in the Nepal flagship AOI and save as GeoJSON.  
**Acceptance Criterion:** `coolr_events.geojson` exists and is valid. Console prints real event count, date range, and an honest assessment of whether coverage is dense enough for precision/recall evaluation.
