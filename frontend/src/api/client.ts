/**
 * DHARĀ API Client
 * 
 * All frontend data fetching goes through this module.
 * Base URL is set via VITE_API_BASE_URL env var (never hardcoded).
 * 
 * No mock data. Every function here hits a real FastAPI endpoint.
 * Errors are propagated with meaningful messages, never silently swallowed.
 */
import type { ChangePassport } from '@/types/changePassport'

const API_BASE = import.meta.env.VITE_API_BASE_URL ?? '/api'

type HazardTypeFilter =
  | 'slow_slope_deformation'
  | 'glacier_motion'
  | 'flood_extent_change'
  | 'land_subsidence'

/** Fetch all Change Passports for an AOI, optionally filtered by hazard type */
export async function fetchEvents(
  aoiName: string,
  hazardType?: HazardTypeFilter,
): Promise<ChangePassport[]> {
  const url = new URL(`${API_BASE}/events`)
  url.searchParams.set('aoi', aoiName)
  if (hazardType) url.searchParams.set('hazard_type', hazardType)

  const res = await fetch(url.toString())
  if (!res.ok) throw new Error(`Failed to fetch events for ${aoiName}: ${res.statusText}`)
  return res.json()
}

/** Fetch a single Change Passport by event_id */
export async function fetchEvent(eventId: string): Promise<ChangePassport> {
  const res = await fetch(`${API_BASE}/events/${eventId}`)
  if (!res.ok) throw new Error(`Event ${eventId} not found: ${res.statusText}`)
  return res.json()
}

export interface TimeseriesPoint {
  date: string  // YYYY-MM-DD
  displacement_mm: number | null  // null = masked pixel
}

/** Fetch displacement time series for a clicked pixel */
export async function fetchTimeseries(
  lat: number,
  lon: number,
  layer: string = 'deformation',
): Promise<TimeseriesPoint[]> {
  const url = new URL(`${API_BASE}/timeseries`)
  url.searchParams.set('lat', String(lat))
  url.searchParams.set('lon', String(lon))
  url.searchParams.set('layer', layer)

  const res = await fetch(url.toString())
  if (!res.ok) throw new Error(`Timeseries fetch failed: ${res.statusText}`)
  return res.json()
}

export interface ValidationSummary {
  precision: number
  recall: number
  f1: number
  matched_events: number
  total_detected: number
  total_coolr: number
}

/** Fetch precision/recall/F1 validation summary for an AOI */
export async function fetchValidation(aoiName: string): Promise<ValidationSummary> {
  const res = await fetch(`${API_BASE}/validation/${aoiName}`)
  if (!res.ok) throw new Error(`Validation fetch failed: ${res.statusText}`)
  return res.json()
}

export interface CommunityObservation {
  event_id?: string | null
  lat: number
  lon: number
  description: string
  reporter_contact?: string
}

/** Submit a community field observation */
export async function submitObservation(obs: CommunityObservation): Promise<{ id: string }> {
  const res = await fetch(`${API_BASE}/observations`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(obs),
  })
  if (!res.ok) {
    const err = await res.json().catch(() => ({}))
    throw new Error(err.detail ?? `Submission failed: ${res.statusText}`)
  }
  return res.json()
}
