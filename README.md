# The Founder's Guide — v0.1 Shell

> *Every business begins with a conversation.*

A conversational AI experience for entrepreneurs. Not a business planning tool — a thoughtful dialogue that helps founders gain clarity, build confidence, and discover their next step.

---

## Running the app

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Hidden pages

| URL param | Page |
|---|---|
| `?page=principles` | Design philosophy |

## Architecture

```
app.py                    ← Entry point & router
pages/
  landing.py              ← Hero + CTA + feature cards
  conversation.py         ← Conversation interface
  principles.py           ← Hidden design philosophy page
components/
  conversation/
    engine.py             ← AI engine hook (placeholder)
  journey/
    sidebar.py            ← Journey sidebar (hidden)
    timeline.py           ← Founder timeline (hidden)
  ui/
    helpers.py            ← Shared UI utilities
    voice.py              ← ElevenLabs voice hook (placeholder)
memory/
  founder_memory.py       ← Founder memory store (placeholder)
prompts/                  ← Prompt templates (future)
summaries/
  session_summary.py      ← Session summary hook (placeholder)
styles/
  main.css                ← All styling
assets/                   ← Images, fonts (future)
```

## Placeholder hooks

All future integrations have stub modules ready:

- **AI Conversation Engine** → `components/conversation/engine.py`
- **ElevenLabs Voice** → `components/ui/voice.py`
- **Founder Memory** → `memory/founder_memory.py`
- **Session Summaries** → `summaries/session_summary.py`
- **Journey Engine** → `components/journey/sidebar.py` + `timeline.py`

---

*Design philosophy: Conversation before calculation.*
