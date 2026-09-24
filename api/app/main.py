"""
DHARĀ FastAPI Application

Endpoints are implemented in P7.1 and P7.2.
This file provides the app instance, CORS config, and health check.

Database choice: SQLite (aiosqlite) for MVP.
Rationale: team size 1-2, time-constrained hackathon. A single SQLite file
is sufficient for the data volumes involved (~hundreds of Change Passports).
Migration to PostgreSQL (asyncpg) requires only changing the DATABASE_URL
environment variable and removing the aiosqlite dependency.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="DHARĀ API",
    description="Earth Change Intelligence — NISAR-powered hazard detection for Nepal and beyond.",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS — allow the frontend origin in production (set via env var)
# During local development, allow all origins for convenience.
import os

ALLOWED_ORIGINS = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:3000,http://localhost:5173",  # Vite dev server ports
).split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/health", tags=["System"])
async def health_check() -> dict:
    """Basic health check endpoint for deployment monitoring."""
    return {"status": "ok", "service": "dhara-api", "version": "0.1.0"}


# TODO P7.1: Register routers
# from app.routers import events, observations, validation, layers, timeseries
# app.include_router(events.router)
# app.include_router(observations.router)
# app.include_router(validation.router)
# app.include_router(layers.router)
# app.include_router(timeseries.router)
