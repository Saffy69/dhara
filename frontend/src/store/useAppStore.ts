/**
 * DHARĀ Global State Store (Zustand)
 * 
 * Manages:
 *   - appMode: The three-way toggle between STORY, EXPLORER, and RESEARCH modes
 *   - currentDate: ISO date string driven by the timeline slider
 *   - activeEventId: The selected Change Passport event ID (null = none selected)
 * 
 * This store is the single source of truth for UI state.
 * Scientific data (Change Passports) is fetched via the API client, not stored here.
 */
import { create } from 'zustand'

export type AppMode = 'STORY' | 'EXPLORER' | 'RESEARCH'

interface AppState {
  /** Current UI mode controlling which panels are visible and map camera behavior */
  appMode: AppMode
  /** ISO date string (YYYY-MM-DD) from the timeline slider — filters visible layers */
  currentDate: string
  /** event_id of the currently selected Change Passport, or null */
  activeEventId: string | null
  /** Actions */
  setAppMode: (mode: AppMode) => void
  setCurrentDate: (date: string) => void
  setActiveEventId: (id: string | null) => void
}

export const useAppStore = create<AppState>((set) => ({
  appMode: 'STORY',
  // Default to latest available — will be overridden by timeline slider
  currentDate: new Date().toISOString().split('T')[0],
  activeEventId: null,
  setAppMode: (mode) => set({ appMode: mode }),
  setCurrentDate: (date) => set({ currentDate: date }),
  setActiveEventId: (id) => set({ activeEventId: id }),
}))
