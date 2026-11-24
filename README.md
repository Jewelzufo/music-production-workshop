# Music Production Workshop - 2026

A reference library for music producers using **FL Studio stock plugins only**.
Sound design and arrangement guidance, presented as starting-point guidelines, not universal rules.

Not endorsed by Image-Line. No third-party VSTs, no copyrighted preset files, no audio samples.
Preset sections are interactive parameter guides: values you recreate manually in FL Studio.

## Tabs

- **Scales**: root + scale type selector (also Cmaj / Cmin shorthand), scale notes, degrees, intervals, step patterns, visual note layout.
- **Arrangement**: bar-based patterns for EDM, Rock, and Hip Hop as section tables with bar ranges and purpose. Labelled as common guidelines.
- **VST**: parameter guides for 3xOsc and Sytrus, with official manual links.
- **Audio Mixing**: FL Studio mixer guidance, dry/wet dB guideline ranges before MIDI-to-audio consolidation, stock mixer chain, with mixer manual link.

## References

- 3xOsc: https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/3x%20Osc.htm
- Sytrus: https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Sytrus.htm
- Mixer: https://www.image-line.com/fl-studio-learning/fl-studio-beta-online-manual/html/mixer_index.htm

These links are references. Content in this app is summarised in original wording, not copied from the manuals.

## Local run

Requires Python 3.11+.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Open http://localhost:8501

## Deploy on Streamlit Community Cloud (GitHub)

1. Push this repository to GitHub (public or private repo you control).
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click **New app**, select this repository and branch, set Main file path to `app.py`.
4. Click **Deploy**. Streamlit installs `requirements.txt` automatically.
5. Theme comes from `.streamlit/config.toml`, no extra setup needed.

Alternative GitHub-based options: fork the repo first, then deploy your fork the same way.

## Repository structure

```
app.py
requirements.txt
README.md
.streamlit/config.toml
data/
  __init__.py
  scales.py
  arrangements.py
  presets.py
  mixing.py
tests/
  test_data.py
```

## Dependencies

Lightweight: `streamlit` and `pandas` (pandas ships with Streamlit and is used only for the arrangement bar chart). See `requirements.txt`.
