"""Scale definitions. Semitone intervals from root."""
NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
NOTE_ALIASES = {"Db": "C#", "Eb": "D#", "Gb": "F#", "Ab": "G#", "Bb": "A#"}

SCALES = {
    "Major": {"intervals": [0, 2, 4, 5, 7, 9, 11], "steps": "W-W-H-W-W-W-H", "degrees": ["1", "2", "3", "4", "5", "6", "7"], "description": "Bright, resolved. Foundation for pop, rock, house melodies."},
    "Natural Minor": {"intervals": [0, 2, 3, 5, 7, 8, 10], "steps": "W-H-W-W-H-W-W", "degrees": ["1", "2", "b3", "4", "5", "b6", "b7"], "description": "Darker, emotional. Common in EDM, hip hop, rock."},
    "Harmonic Minor": {"intervals": [0, 2, 3, 5, 7, 8, 11], "steps": "W-H-W-W-H-1.5-H", "degrees": ["1", "2", "b3", "4", "5", "b6", "7"], "description": "Natural minor with raised 7th. Tense, classical / dramatic pull to tonic."},
    "Melodic Minor": {"intervals": [0, 2, 3, 5, 7, 9, 11], "steps": "W-H-W-W-W-W-H", "degrees": ["1", "2", "b3", "4", "5", "6", "7"], "description": "Minor with raised 6th and 7th ascending. Smooth, jazzy minor."},
    "Dorian": {"intervals": [0, 2, 3, 5, 7, 9, 10], "steps": "W-H-W-W-W-H-W", "degrees": ["1", "2", "b3", "4", "5", "6", "b7"], "description": "Minor with raised 6th. Funk, house, modal grooves."},
    "Phrygian": {"intervals": [0, 1, 3, 5, 7, 8, 10], "steps": "H-W-W-W-H-W-W", "degrees": ["1", "b2", "b3", "4", "5", "b6", "b7"], "description": "Dark, Spanish / metal colour from the flat 2nd."},
    "Lydian": {"intervals": [0, 2, 4, 6, 7, 9, 11], "steps": "W-W-W-H-W-W-H", "degrees": ["1", "2", "3", "#4", "5", "6", "7"], "description": "Major with raised 4th. Floating, dreamy."},
    "Mixolydian": {"intervals": [0, 2, 4, 5, 7, 9, 10], "steps": "W-W-H-W-W-H-W", "degrees": ["1", "2", "3", "4", "5", "6", "b7"], "description": "Major with flat 7th. Blues, rock, funk dominant grooves."},
    "Locrian": {"intervals": [0, 1, 3, 5, 6, 8, 10], "steps": "H-W-W-H-W-W-W", "degrees": ["1", "b2", "b3", "4", "b5", "b6", "b7"], "description": "Unstable, diminished tonic. Use sparingly for tension."},
    "Major Pentatonic": {"intervals": [0, 2, 4, 7, 9], "steps": "W-W-1.5-W-1.5", "degrees": ["1", "2", "3", "5", "6"], "description": "Safe, melodic subset of major. Great for hooks."},
    "Minor Pentatonic": {"intervals": [0, 3, 5, 7, 10], "steps": "1.5-W-W-1.5-W", "degrees": ["1", "b3", "4", "5", "b7"], "description": "Core blues / rock / hip hop melody scale."},
    "Blues": {"intervals": [0, 3, 5, 6, 7, 10], "steps": "1.5-W-H-H-1.5-W", "degrees": ["1", "b3", "4", "b5", "5", "b7"], "description": "Minor pentatonic plus flat 5 blue note."},
    "Chromatic": {"intervals": list(range(12)), "steps": "H x 11", "degrees": ["1", "b2", "2", "b3", "3", "4", "b5", "5", "b6", "6", "b7", "7"], "description": "All 12 notes. Reference only, passing tones."},
}

def get_scale_notes(root: str, scale_name: str) -> list[str]:
    root = NOTE_ALIASES.get(root, root)
    idx = NOTES.index(root)
    intervals = SCALES[scale_name]["intervals"]
    return [NOTES[(idx + i) % 12] for i in intervals]

def parse_shorthand(text: str):
    """Parse e.g. Cmaj, Cmin, F#min, Bb maj. Returns (root, scale_name) or None."""
    if not text:
        return None
    t = text.strip().replace(" ", "")
    # root: letter + optional # or b
    if len(t) < 2:
        return None
    root = t[0].upper()
    rest = t[1:]
    if rest and rest[0] in ("#", "b"):
        root += rest[0]
        rest = rest[1:]
    rest_low = rest.lower()
    if rest_low in ("maj", "major", "m", "ionian") and rest_low != "m":
        scale = "Major"
    elif rest_low in ("min", "minor", "m", "aeolian"):
        scale = "Natural Minor"
    elif rest_low in ("hmin", "harmonicminor"):
        scale = "Harmonic Minor"
    elif rest_low in ("dor", "dorian"):
        scale = "Dorian"
    elif rest_low in ("pent", "pentatonic"):
        scale = "Minor Pentatonic"
    else:
        return None
    if root not in NOTES and root not in NOTE_ALIASES:
        return None
    return (NOTE_ALIASES.get(root, root), scale)
