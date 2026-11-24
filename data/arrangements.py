"""Arrangement patterns. Common guidelines, not universal rules."""
ARRANGEMENTS = {
    "EDM": {
        "total_bars": 128,
        "bpm_guideline": "120-150 (genre dependent, guideline only)",
        "sections": [
            {"Section": "Intro", "Bars": "1-16", "Length": 16, "Purpose": "DJ-friendly, sparse drums / atmosphere, establish key"},
            {"Section": "Verse / Build 1", "Bars": "17-32", "Length": 16, "Purpose": "Add bass, chords, melody fragments"},
            {"Section": "Breakdown", "Bars": "33-48", "Length": 16, "Purpose": "Strip drums, focus melody and pads"},
            {"Section": "Buildup", "Bars": "49-64", "Length": 16, "Purpose": "Risers, snare roll, automation, tension"},
            {"Section": "Drop / Chorus", "Bars": "65-80", "Length": 16, "Purpose": "Full energy: kick, bass, lead together"},
            {"Section": "Drop B / Variation", "Bars": "81-96", "Length": 16, "Purpose": "Same energy, varied lead or bass pattern"},
            {"Section": "Breakdown 2", "Bars": "97-112", "Length": 16, "Purpose": "Reset energy, new melodic idea"},
            {"Section": "Outro", "Bars": "113-128", "Length": 16, "Purpose": "Strip back to intro elements for mixing out"},
        ],
    },
    "Rock": {
        "total_bars": 104,
        "bpm_guideline": "90-160 (genre dependent, guideline only)",
        "sections": [
            {"Section": "Intro", "Bars": "1-8", "Length": 8, "Purpose": "Riff or drums establish groove and key"},
            {"Section": "Verse 1", "Bars": "9-24", "Length": 16, "Purpose": "Vocals forward, instruments support, lower energy"},
            {"Section": "Pre-Chorus", "Bars": "25-32", "Length": 8, "Purpose": "Harmonic lift, build tension toward chorus"},
            {"Section": "Chorus 1", "Bars": "33-48", "Length": 16, "Purpose": "Hook, full band, widest and loudest section so far"},
            {"Section": "Verse 2", "Bars": "49-64", "Length": 16, "Purpose": "Verse energy with small arrangement variations"},
            {"Section": "Pre-Chorus 2", "Bars": "65-72", "Length": 8, "Purpose": "Build again, often shorter or more intense"},
            {"Section": "Chorus 2", "Bars": "73-88", "Length": 16, "Purpose": "Hook returns, added layers or harmonies"},
            {"Section": "Bridge / Solo", "Bars": "89-96", "Length": 8, "Purpose": "Contrast: new chords, solo, or stripped section"},
            {"Section": "Final Chorus + Outro", "Bars": "97-104", "Length": 8, "Purpose": "Final hook statement, then ending riff or fade"},
        ],
    },
    "Hip Hop": {
        "total_bars": 88,
        "bpm_guideline": "80-100 / 130-160 double-time feel (guideline only)",
        "sections": [
            {"Section": "Intro", "Bars": "1-4", "Length": 4, "Purpose": "Sample, tag, or sparse loop establishes mood"},
            {"Section": "Hook / Chorus", "Bars": "5-12", "Length": 8, "Purpose": "Memorable loop + hook, full drums and 808"},
            {"Section": "Verse 1", "Bars": "13-28", "Length": 16, "Purpose": "Rap forward, beat slightly stripped vs hook"},
            {"Section": "Hook / Chorus", "Bars": "29-36", "Length": 8, "Purpose": "Hook returns, full energy"},
            {"Section": "Verse 2", "Bars": "37-52", "Length": 16, "Purpose": "Second verse, small beat variations / drops"},
            {"Section": "Hook / Chorus", "Bars": "53-60", "Length": 8, "Purpose": "Hook returns"},
            {"Section": "Bridge", "Bars": "61-68", "Length": 8, "Purpose": "Beat switch, stripped loop, or melodic break"},
            {"Section": "Final Hook", "Bars": "69-76", "Length": 8, "Purpose": "Final hook, ad-libs, variation"},
            {"Section": "Outro", "Bars": "77-88", "Length": 12, "Purpose": "Loop fades or hard stop, space for DJ / transition"},
        ],
    },
}
