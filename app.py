"""Music Production Workshop - 2026
Reference library for FL Studio producers. Stock plugins only.
All guidance is starting-point guidance, not universal rules.
Not endorsed by Image-Line.
"""
import streamlit as st

from data.scales import NOTES, SCALES, get_scale_notes, parse_shorthand
from data.arrangements import ARRANGEMENTS
from data.presets import PRESETS_3XOSC, PRESETS_SYTRUS, MANUALS
from data.mixing import DRY_WET_LEVELS, MIXER_MANUAL, CONSOLIDATE_NOTES, STOCK_MIXER_CHAIN

st.set_page_config(page_title="Music Production Workshop - 2026", layout="wide")
st.title("Music Production Workshop - 2026")
st.caption("FL Studio stock plugins only. General guidance and starting points, not fixed rules. Not endorsed by Image-Line.")

tab_scales, tab_arr, tab_vst, tab_mix = st.tabs(["Scales", "Arrangement", "VST", "Audio Mixing"])

# ---------------- Scales ----------------
with tab_scales:
    st.header("Scales")
    st.write("Select a root and scale type, or type a shorthand such as Cmaj or Cmin.")
    col1, col2, col3 = st.columns(3)
    with col1:
        root = st.selectbox("Root note", NOTES, index=0, key="scale_root")
    with col2:
        scale_name = st.selectbox("Scale type", list(SCALES.keys()), index=1, key="scale_type")
    with col3:
        shorthand = st.text_input("Shorthand (optional, overrides above)", placeholder="e.g. Cmaj, Cmin, F#min")
        if shorthand:
            parsed = parse_shorthand(shorthand)
            if parsed:
                root, scale_name = parsed
                st.success(f"Parsed as {root} {scale_name}")
            else:
                st.warning("Could not parse shorthand. Try Cmaj, Cmin, F#min, Bb maj.")

    notes = get_scale_notes(root, scale_name)
    info = SCALES[scale_name]
    st.subheader(f"{root} {scale_name}")
    st.write(info["description"])
    # Visual note layout as a table / piano-style row
    st.markdown("**Scale notes (visual layout)**")
    cols = st.columns(len(notes))
    for i, n in enumerate(notes):
        with cols[i]:
            label = f"**{n}**" if i == 0 else n
            st.markdown(f"<div style='text-align:center;padding:10px;border:1px solid #555;border-radius:6px;background:#3a3a3a'>{label}<br><small>{info['degrees'][i]}</small></div>", unsafe_allow_html=True)
    st.table({"Note": notes, "Degree": info["degrees"], "Semitones from root": info["intervals"]})
    st.write(f"**Step pattern:** {info['steps']}")
    st.write(f"**Intervals (semitones):** {', '.join(str(x) for x in info['intervals'])}")
    st.subheader("All scales in selected root")
    rows = []
    for name, s in SCALES.items():
        rows.append({"Scale": name, "Notes": " - ".join(get_scale_notes(root, name)), "Steps": s["steps"]})
    st.table(rows)
    st.info("In FL Studio: Piano Roll > Helpers > Scale Highlighting lets you highlight a scale while you write. Use this tab as the reference for which notes belong.")

# ---------------- Arrangement ----------------
with tab_arr:
    st.header("Arrangement")
    st.warning("These patterns are common guidelines, not universal rules. Many tracks vary length, order, and section count.")
    genre = st.selectbox("Genre", list(ARRANGEMENTS.keys()))
    data = ARRANGEMENTS[genre]
    st.write(f"**Total (guideline):** {data['total_bars']} bars")
    st.write(f"**Tempo guideline:** {data['bpm_guideline']}")
    st.table(data["sections"])
    # Simple bar chart of section lengths
    try:
        import pandas as pd
        df = pd.DataFrame(data["sections"])
        st.bar_chart(df.set_index("Section")["Length"])
    except Exception:
        pass

# ---------------- VST ----------------
with tab_vst:
    st.header("VST")
    st.write("Interactive parameter guides for stock FL Studio generators only. Recreate the settings manually in FL Studio. These are original guides, not official presets and not preset files.")
    st.markdown(f"- [3xOsc manual]({MANUALS['3xOsc']})")
    st.markdown(f"- [Sytrus manual]({MANUALS['Sytrus']})")

    st.subheader("3xOsc")
    p1 = st.selectbox("3xOsc guide", list(PRESETS_3XOSC.keys()), key="preset_3x")
    guide1 = PRESETS_3XOSC[p1]
    st.write(guide1["description"])
    st.table(guide1["params"])
    detune = st.slider("Try a detune amount (cents, for supersaw style guides)", 0, 50, 12, key="detune_demo")
    st.write(f"Detune demo: set Osc 2 Fine to +{detune} cents and Osc 3 Fine to -{detune} cents, then adjust by ear. Guideline only.")

    st.subheader("Sytrus")
    p2 = st.selectbox("Sytrus guide", list(PRESETS_SYTRUS.keys()), key="preset_sytrus")
    guide2 = PRESETS_SYTRUS[p2]
    st.write(guide2["description"])
    st.table(guide2["params"])
    mod = st.slider("FM modulation amount demo (%)", 0, 100, 40, key="fm_demo")
    st.write(f"FM demo value: {mod}%. Start lower for bass and piano guides, higher adds brightness and growl. Adjust by ear, guideline only.")

# ---------------- Audio Mixing ----------------
with tab_mix:
    st.header("Audio Mixing")
    st.markdown(f"Mixer reference: [FL Studio Mixer manual]({MIXER_MANUAL})")
    st.warning("All dB levels below are starting-point guidelines, not universal optimal values. Check peaks with Fruity dB Meter and judge by ear in your room and genre.")
    st.subheader("Dry / wet dB levels before MIDI-to-audio")
    st.write("Dry here means the generator / instrument level before you consolidate or record MIDI to audio. Use these ranges to leave headroom and avoid clipping inserts.")
    st.table(DRY_WET_LEVELS)
    st.subheader("Before you consolidate / record MIDI to audio")
    for note in CONSOLIDATE_NOTES:
        st.write(f"- {note}")
    st.subheader("Stock mixer chain (example order)")
    st.table(STOCK_MIXER_CHAIN)
    target = st.slider("Master peak target demo (dBFS)", -12, -1, -6, key="master_target")
    st.write(f"You selected {target} dBFS as a pre-master peak guideline. Common guideline range in this app is -6 to -3 dBFS, not a rule.")
