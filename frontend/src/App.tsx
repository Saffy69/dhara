/**
 * DHARĀ App Root
 * 
 * Renders the full-screen MapLibre canvas behind all UI overlays.
 * Mode switching (STORY | EXPLORER | RESEARCH) is managed via Zustand.
 * 
 * THIS IS A SCAFFOLD. Map and UI components will be implemented in P8.x tasks.
 */
import React from 'react'

export default function App() {
  return (
    <div className="relative w-screen h-screen overflow-hidden bg-dhara-bg">
      {/* TODO P8.1: Replace with <MapScene /> */}
      <div className="absolute inset-0 flex items-center justify-center">
        <div className="text-center">
          <h1 className="text-4xl font-bold text-nasa-white mb-2">DHARĀ</h1>
          <p className="text-nasa-cyan font-mono text-sm">Earth Change Intelligence</p>
          <p className="text-gray-500 text-xs mt-4">Pipeline initializing...</p>
        </div>
      </div>
      {/* TODO P8.1: Replace with <UIOverlay /> */}
    </div>
  )
}
