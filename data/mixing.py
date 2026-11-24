"""Mixing guidance. All values are starting-point guidelines, not universal optimal values."""
MIXER_MANUAL = "https://www.image-line.com/fl-studio-learning/fl-studio-beta-online-manual/html/mixer_index.htm"

# Dry = level before MIDI-to-audio consolidation / recording, Wet = suggested balance context.
# dBFS ranges are guidelines for headroom before consolidation, check with Fruity dB Meter.
DRY_WET_LEVELS = [
    {"Element": "Kick", "Dry dBFS (guideline)": "-12 to -8", "Wet / Mix Note": "Reference element, other drums balanced relative to kick", "Explanation": "Leaves headroom on master, avoids clipping inserts"},
    {"Element": "Snare / Clap", "Dry dBFS (guideline)": "-14 to -10", "Wet / Mix Note": "Slightly under or equal to kick peak", "Explanation": "Transient element, check peak not RMS only"},
    {"Element": "Hi-hats / Percussion", "Dry dBFS (guideline)": "-22 to -16", "Wet / Mix Note": "Lower than kick/snare in most genres", "Explanation": "High frequency energy reads louder than meter suggests"},
    {"Element": "Sub Bass", "Dry dBFS (guideline)": "-14 to -10", "Wet / Mix Note": "Balance against kick, sidechain is genre dependent", "Explanation": "Monitor on meter and small speaker check, room dependent"},
    {"Element": "Mid Bass / Reese", "Dry dBFS (guideline)": "-16 to -11", "Wet / Mix Note": "Under sub in level, more harmonic presence", "Explanation": "Avoid masking kick, use EQ carving as guideline"},
    {"Element": "Pads / Chords", "Dry dBFS (guideline)": "-20 to -14", "Wet / Mix Note": "Background layer in verses, lift in chorus", "Explanation": "Sustained sounds build RMS quickly"},
    {"Element": "Lead / Supersaw", "Dry dBFS (guideline)": "-16 to -11", "Wet / Mix Note": "Forward in drop/chorus, automate down in verses", "Explanation": "Detuned stacks are dense, watch master headroom"},
    {"Element": "Vocals", "Dry dBFS (guideline)": "-18 to -12", "Wet / Mix Note": "Usually forward, genre dependent", "Explanation": "Record / consolidate with peaks below 0 dBFS, leave processing headroom"},
    {"Element": "FX / Risers", "Dry dBFS (guideline)": "-24 to -16", "Wet / Mix Note": "Automate, peaks only at transitions", "Explanation": "Prevent FX from masking main elements"},
    {"Element": "Master (pre-mastering)", "Dry dBFS (guideline)": "Peak -6 to -3, no limiter squash", "Wet / Mix Note": "Leave headroom for mastering stage", "Explanation": "Guideline only, not a loudness target"},
]

CONSOLIDATE_NOTES = [
    "In FL Studio, use Playlist > Consolidate (or Mixer track recording) to render MIDI to audio when CPU is high or to commit a sound.",
    "Before consolidating: set the instrument output so peaks sit in the guideline range for its element, disable master limiting for the render if you plan to mix further, and leave mixer FX intentional: printed FX cannot be undone after consolidation.",
    "VST / generator volume is pre-insert, mixer fader is post-insert. Lowering generator volume changes drive into inserts such as Fruity WaveShaper and sidechain gain reduction. Lowering the fader changes balance without changing that drive.",
    "After consolidating, mute (do not delete) the original MIDI pattern until you have checked the audio render.",
]

STOCK_MIXER_CHAIN = [
    {"Slot Idea": "EQ", "Stock Plugin": "Fruity Parametric EQ 2", "Purpose": "High-pass non-bass elements, gentle carving (guideline)"},
    {"Slot Idea": "Dynamics", "Stock Plugin": "Fruity Limiter / Fruity Compressor", "Purpose": "Control peaks, sidechain input from kick where wanted"},
    {"Slot Idea": "Saturation", "Stock Plugin": "Fruity WaveShaper / Fruity Blood Overdrive", "Purpose": "Add harmonics in small amounts"},
    {"Slot Idea": "Space", "Stock Plugin": "Fruity Reverb 2 / Fruity Delay 3", "Purpose": "Send-based space, keep low end mostly dry"},
    {"Slot Idea": "Metering", "Stock Plugin": "Fruity dB Meter (last slot)", "Purpose": "Check dBFS peaks before consolidation / export"},
]
