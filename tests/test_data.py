import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from data.scales import get_scale_notes, parse_shorthand, SCALES
from data.arrangements import ARRANGEMENTS
from data.presets import PRESETS_3XOSC, PRESETS_SYTRUS, MANUALS
from data.mixing import DRY_WET_LEVELS, MIXER_MANUAL

def test_c_major():
    assert get_scale_notes("C", "Major") == ["C", "D", "E", "F", "G", "A", "B"]
def test_c_minor():
    assert get_scale_notes("C", "Natural Minor") == ["C", "D", "D#", "F", "G", "G#", "A#"]
def test_shorthand():
    assert parse_shorthand("Cmaj") == ("C", "Major")
    assert parse_shorthand("Cmin") == ("C", "Natural Minor")
    assert parse_shorthand("F#min") == ("F#", "Natural Minor")
def test_arrangements_genres():
    assert set(ARRANGEMENTS.keys()) == {"EDM", "Rock", "Hip Hop"}
    for v in ARRANGEMENTS.values():
        assert v["sections"]
def test_presets_and_links():
    assert PRESETS_3XOSC and PRESETS_SYTRUS
    assert "3x%20Osc" in MANUALS["3xOsc"]
    assert "Sytrus" in MANUALS["Sytrus"]
    assert "mixer_index" in MIXER_MANUAL
def test_mixing_levels():
    assert len(DRY_WET_LEVELS) >= 8
