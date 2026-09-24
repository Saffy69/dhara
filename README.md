# DHARĀ — Earth Change Intelligence

> *"The land speaks in millimetres. We built the ears."*

DHARĀ (Deformation and Hazard Analysis using Radar for Alert-readiness) turns NASA-ISRO NISAR satellite SAR data into **Change Passports** — structured, confidence-scored records of ground deformation, glacier motion, and flood-extent change across Nepal's Koshi Basin and global subsidence hotspots.

We detect precursor signals that precede landslides and Glacial Lake Outburst Floods (GLOFs) — events like the 2015 Sindhupalchowk landslide (>3,000 deaths) and the 2021 Melamchi flood — **before** they become disasters, using NISAR's 12-day repeat-pass InSAR stack validated against the NASA COOLR ground-truth catalog.

The system exposes three interfaces: a **Story Mode** for public understanding, an **Explorer Mode** for field analysts, and a **Research Mode** for scientific reproducibility — all fed exclusively by real pipeline-derived Change Passports, never synthetic data.

**⚠️ This is not an emergency alert system. All data is PROVISIONAL.**

## Quick Start

```bash
# Data pipeline
cd data-pipeline && pip install -e .

# API backend
cd api && pip install -e .
uvicorn app.main:app --reload

# Frontend
cd frontend && npm install && npm run dev
```

## Architecture
See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) and [docs/METHODOLOGY.md](docs/METHODOLOGY.md).

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md).
# dhara
