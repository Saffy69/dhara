# DHARĀ — Refined Frontend UI Specification

**Status:** ALIGNED WITH DHARĀ MASTER PIPELINE
**Objective:** A visually stunning, highly interactive, yet rigorously scientific frontend that proves real NISAR data works in the hands of real stakeholders.

## 1. Project Overview & Vibe Check
We are building the UI for **DHARĀ — Earth Change Intelligence**. 
* **The Pivot:** We are rejecting the "cyberpunk/neon" aesthetic and the "mock data" approach. To win this NASA Space Apps challenge, the UI must scream *trust, transparency, and scientific rigor*. 
* **The Aesthetic:** Clean, modern "Glassmorphism" but grounded in accessible, scientific data-viz palettes (NASA/ICIMOD compliant). Dark mode is acceptable for high contrast with radar data, but it must look like a real analytical tool used by disaster response teams, not a video game.

## 2. Tech Stack & Libraries
* **Framework:** React 18 + Vite + TypeScript (Aligns with DHARĀ Phase 0 specs).
* **Styling:** Tailwind CSS (configured for clean glass panels, high-contrast text, and scientific data scales).
* **Geospatial & 3D Engine:** MapLibre GL JS (`maplibre-gl`). 
  * *Crucial Shift:* We are NOT using React Three Fiber or a generic Three.js mesh. We will use MapLibre's native 3D Terrain capabilities driven by our actual Copernicus GLO-30 DEM data (Phase 1.3). This ensures geospatial accuracy and aligns perfectly with real coordinate systems.
* **Data Visualization:** Recharts (`recharts`) for pixel-level time-series and confidence breakdowns.
* **Icons:** Lucide React (`lucide-react`).
* **State Management:** Zustand (`zustand`) for Mode toggles and global timeline state.
* **Animation:** Framer Motion (`framer-motion`) for smooth, cinematic transitions between UI states.

## 3. Step-by-Step Execution Plan

### Step 1: Global State Management (Zustand)
Create a `useAppStore.ts` to manage:
* `appMode`: Enum (`'STORY' | 'EXPLORER' | 'RESEARCH'`). Defaults to `STORY`.
* `currentDate`: Driven by the timeline slider, used to filter which Change Passports and raster overlays are visible.
* `activeEventId`: The currently selected Change Passport.

### Step 2: The 3D Geospatial Environment (MapLibre GL JS)
Create a `MapScene.tsx` component that renders behind the UI (`z-index: 0`).
1. Initialize MapLibre centered on the **Sindhupalchowk / Melamchi watershed**.
2. **Real 3D Terrain:** Enable 3D terrain using the real DEM fetched from the pipeline.
3. **The Data Pulse:** Instead of fake spherical hotspots, overlay the real event clusters (Change Passports). Use MapLibre data-driven styling to pulse or color-code these polygons/points based on their `confidence.tier` (High = Red, Moderate = Orange, Low = Yellow).
4. **Cinematic Camera:** When `appMode` changes, use MapLibre's `flyTo` or `easeTo` to smoothly transition the camera (e.g., low-angle cinematic pitch for Story Mode, top-down tactical pitch for Explorer/Research Mode).

### Step 3: The User Interface (Overlay)
Create a `UIOverlay.tsx` (`z-index: 10`, `pointer-events-none`).

#### 3A: Global Controls
* **Top-Center:** A sleek Framer Motion toggle switch bridging `Story` -> `Explorer` -> `Research`.
* **Always Visible (CRITICAL):** A fixed disclaimer: *"This is not an emergency alert. Data is provisional."*

#### 3B: Story Mode (Public/Cinematic)
* **Bottom-Left Panel:** A glass card displaying the *Change Passport* in plain language (Phase 8.2). Shows the one-sentence summary, confidence badge, and "what we ruled out".
* **Right Edge Timeline:** A vertical slider controlling `currentDate`. As it moves, the MapLibre layers update to show historical progression of the hazard cascade (glacier motion -> slope deformation -> flood extent).

#### 3C: Explorer Mode (Interactive Analysis)
* **Left Panel:** Layer toggles (Deformation, Glacier Motion, Water Extent, Rainfall).
* **Center Map Interaction:** Swipe-compare widget to compare two dates.
* **Bottom Panel (Data Chart):** When a user clicks a pixel on the map, fetch from the real FastAPI `/timeseries` endpoint and render a glowing Recharts line chart showing actual displacement (mm/year) over time (Phase 9.2).

#### 3D: Research Mode (Scientific Transparency)
* **Top-Right Panel:** The full Confidence Breakdown (Phase 10.1). A Recharts bar chart showing exactly how the score was calculated (`data_quality`, `spatial_coherence`, etc.).
* **Bottom-Right:** Data Provenance panel linking to raw NASA/ESA source granules. A prominent "Export for Reproducibility" button (Jupyter Notebook stub).

### Step 4: API Integration (NO MOCK DATA)
* Connect Zustand actions directly to the FastAPI backend defined in Phase 7.
* `GET /events?aoi=nepal_flagship` feeds the map markers.
* `GET /timeseries?lat={x}&lon={y}` feeds the Recharts panels.
* *Self-Healing Note:* The frontend must gracefully handle missing data or low-coherence (NaN) pixels with a "No reliable signal at this location" message, rather than crashing or showing empty charts.

## 4. Testing & Validation
* Run Vite dev server. Verify MapLibre context doesn't conflict with React rendering cycles.
* Ensure UI elements have `pointer-events-auto` so the map can still be panned/zoomed beneath them.
* Validate that no fake data, mock JSON, or hallucinatory hazard warnings exist anywhere in the application. Every metric must trace to a Change Passport.
