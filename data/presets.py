"""Preset guides for stock plugins only. Parameter values users recreate manually.
These are original starting-point guides, not official Image-Line presets."""
MANUALS = {
    "3xOsc": "https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/3x%20Osc.htm",
    "Sytrus": "https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Sytrus.htm",
}

PRESETS_3XOSC = {
    "Sub Bass": {
        "description": "Clean sine sub. Layer under a mid bass, keep mono.",
        "params": [
            {"Parameter": "Osc 1 Wave", "Value": "Sine", "Notes": "Fundamental only"},
            {"Parameter": "Osc 1 Coarse", "Value": "0 (or -12 for lower octave)", "Notes": "Tune to track root"},
            {"Parameter": "Osc 2 / 3", "Value": "Off / volume 0", "Notes": "Keep clean"},
            {"Parameter": "Volume Envelope Attack", "Value": "5-15 ms", "Notes": "Avoid click"},
            {"Parameter": "Volume Envelope Decay / Sustain", "Value": "Sustain high, release 80-150 ms", "Notes": "Guideline only"},
            {"Parameter": "Stereo Detune", "Value": "0", "Notes": "Subs stay centred"},
        ],
    },
    "Supersaw Lead": {
        "description": "Detuned saw stack. Recreate manually, adjust detune to taste.",
        "params": [
            {"Parameter": "Osc 1 Wave", "Value": "Saw", "Notes": "Main voice"},
            {"Parameter": "Osc 2 Wave", "Value": "Saw, Fine +12 cents", "Notes": "Detune for width"},
            {"Parameter": "Osc 3 Wave", "Value": "Saw, Fine -12 cents", "Notes": "Detune opposite side"},
            {"Parameter": "Osc Mix", "Value": "Osc1 100%, Osc2 80%, Osc3 80%", "Notes": "Balance by ear"},
            {"Parameter": "Volume Envelope", "Value": "Attack 2-8 ms, Release 120-250 ms", "Notes": "Guideline only"},
        ],
    },
    "Soft Pluck": {
        "description": "Short triangle pluck for arps and melodies.",
        "params": [
            {"Parameter": "Osc 1 Wave", "Value": "Triangle", "Notes": "Softer harmonics"},
            {"Parameter": "Osc 2 Wave", "Value": "Sine, +12 semitones, low volume", "Notes": "Adds sparkle"},
            {"Parameter": "Volume Envelope", "Value": "Attack 1-3 ms, Decay 180-300 ms, Sustain 0", "Notes": "Pluck shape"},
            {"Parameter": "Filter / FX in Mixer", "Value": "Use Fruity Parametric EQ 2 + Fruity Delay 3 in mixer", "Notes": "Stock mixer FX only"},
        ],
    },
    "Square Bass": {
        "description": "Hollow square bass for electro / chiptune colour.",
        "params": [
            {"Parameter": "Osc 1 Wave", "Value": "Square", "Notes": "Hollow tone"},
            {"Parameter": "Osc 2 Wave", "Value": "Sine, -12 semitones", "Notes": "Sub reinforcement"},
            {"Parameter": "Volume Envelope", "Value": "Attack 3-10 ms, Sustain medium-high", "Notes": "Guideline only"},
        ],
    },
}

PRESETS_SYTRUS = {
    "FM Electric Piano": {
        "description": "Operator FM piano style guide. Ratios and envelopes are the sound.",
        "params": [
            {"Parameter": "Operators", "Value": "OP1 carrier sine, OP2 modulator sine ratio 2.00", "Notes": "Start simple"},
            {"Parameter": "OP2 Envelope", "Value": "Fast attack, decay 600-900 ms to low sustain", "Notes": "Brightness fades like a piano"},
            {"Parameter": "OP1 Envelope", "Value": "Fast attack, decay 1200-1800 ms", "Notes": "Body"},
            {"Parameter": "Filter", "Value": "Low pass, light cutoff modulation", "Notes": "Tame top end"},
            {"Parameter": "Effects (in Sytrus)", "Value": "Chorus light, Reverb small amount", "Notes": "Guideline, adjust by ear"},
        ],
    },
    "FM Bass": {
        "description": "Punchy FM bass, controlled harmonics.",
        "params": [
            {"Parameter": "Operators", "Value": "OP1 sine carrier, OP2 sine ratio 1.00, OP3 ratio 3.01 low level", "Notes": "Growl control"},
            {"Parameter": "OP2 Envelope", "Value": "Attack 1 ms, Decay 150-300 ms", "Notes": "Punch transient"},
            {"Parameter": "OP1 Envelope", "Value": "Sustain high, Release 80-150 ms", "Notes": "Guideline only"},
            {"Parameter": "Unison / Detune", "Value": "Off or very low for bass", "Notes": "Keep low end tight"},
        ],
    },
    "Pad (Additive / FM)": {
        "description": "Slow evolving pad. Long envelopes, gentle detune.",
        "params": [
            {"Parameter": "Operators", "Value": "2-3 operators, ratios 1.00 / 2.00 / 3.00, low mod levels", "Notes": "Soft harmonics"},
            {"Parameter": "Volume Envelope", "Value": "Attack 400-1200 ms, Release 800-2000 ms", "Notes": "Swell shape"},
            {"Parameter": "Filter", "Value": "Low pass, slow LFO on cutoff (small amount)", "Notes": "Movement"},
            {"Parameter": "Effects (in Sytrus)", "Value": "Chorus medium, Reverb medium", "Notes": "Guideline only"},
        ],
    },
    "Reese-style Bass": {
        "description": "Detuned saw movement. Recreate with Sytrus oscillators, keep sub centred in mixer.",
        "params": [
            {"Parameter": "Oscillators / Operators", "Value": "Saw waves, detune +/- 15-25 cents", "Notes": "Phasing movement"},
            {"Parameter": "Filter", "Value": "Low pass, cutoff modulated slowly", "Notes": "Core Reese motion"},
            {"Parameter": "Volume Envelope", "Value": "Attack 5-20 ms, Sustain high", "Notes": "Guideline only"},
        ],
    },
}
