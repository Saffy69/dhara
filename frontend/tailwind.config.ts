import type { Config } from 'tailwindcss'

const config: Config = {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        // Scientific glassmorphism palette — NOT cyberpunk
        // High-contrast, accessible, trust-inspiring
        'dhara-bg': '#0a0f1a',          // Deep space navy
        'dhara-surface': '#111827',     // Panel background
        'dhara-glass': 'rgba(17,24,39,0.75)', // Glass panels
        'dhara-border': '#1f2d47',      // Subtle borders
        // Data confidence tier colors (colorblind-accessible)
        'tier-high': '#ef4444',         // Red — high risk confidence
        'tier-moderate': '#f97316',     // Orange — moderate confidence  
        'tier-low': '#eab308',          // Yellow — low confidence
        // Scientific accent (NASA blue inspired)
        'nasa-blue': '#1d4ed8',
        'nasa-cyan': '#06b6d4',
        'nasa-white': '#f0f4ff',
        // Displacement data viz
        'deform-pos': '#ef4444',        // Positive displacement (uplift)
        'deform-neg': '#3b82f6',        // Negative displacement (subsidence)
        'deform-neutral': '#6b7280',    // Within noise threshold
      },
      fontFamily: {
        mono: ['JetBrains Mono', 'Fira Code', 'monospace'],
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
      backdropBlur: {
        xs: '2px',
      },
      boxShadow: {
        'glass': '0 4px 30px rgba(0, 0, 0, 0.3)',
        'tier-high': '0 0 20px rgba(239, 68, 68, 0.3)',
        'tier-moderate': '0 0 20px rgba(249, 115, 22, 0.3)',
        'tier-low': '0 0 20px rgba(234, 179, 8, 0.3)',
      },
      animation: {
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'fade-in': 'fadeIn 0.3s ease-in-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0', transform: 'translateY(8px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
      },
    },
  },
  plugins: [],
}

export default config
