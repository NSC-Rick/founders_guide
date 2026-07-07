"""
Conversation Page — ElevenLabs Conversational AI
--------------------------------------------------
Uses st.components.v1.html() so the <script> tag executes
and the <elevenlabs-convai> custom element registers correctly.
st.markdown strips scripts; only components.html preserves them.

Future integration hooks are noted in Python comments only.
"""

import streamlit as st
import streamlit.components.v1 as components
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.ui.helpers import load_css, spacer

AGENT_ID = "agent_4501kwy01rrxev8bwvb3mqvmk5zn"


# ── ElevenLabs iframe HTML ────────────────────────────────────────────────────

def _agent_html() -> str:
    """
    Full HTML document rendered inside an iframe via st.components.v1.html().
    The script executes here, registers the custom element, and the widget renders.
    Fonts and colors mirror the parent page tokens for a seamless look.
    """
    return f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500&display=swap');

  * {{ box-sizing: border-box; margin: 0; padding: 0; }}

  html, body {{
    background: transparent;
    font-family: 'Inter', -apple-system, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    padding: 1rem;
  }}

  elevenlabs-convai {{
    --el-brand:           #5C6B4A;
    --el-brand-hover:     #4A5639;
    --el-background:      #FFFFFF;
    --el-border-radius:   9999px;
    --el-font-family:     'Inter', -apple-system, sans-serif;
    --el-text-primary:    #1A1916;
    --el-text-secondary:  #7A746A;
    --el-border-color:    #E8E4DC;
    display: block;
  }}
</style>
</head>
<body>
  <elevenlabs-convai agent-id="{AGENT_ID}"></elevenlabs-convai>
  <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async></script>
</body>
</html>
"""


# ── Main render ───────────────────────────────────────────────────────────────

def render():
    load_css()

    # HOOK: Founder Memory — load founder profile here before rendering

    # ── Back navigation ───────────────────────────────────────────────────────
    spacer("1.75rem")
    st.markdown('<div class="fg-back-btn">', unsafe_allow_html=True)
    if st.button("← Back", key="back_btn"):
        st.session_state["page"] = "landing"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Page header ───────────────────────────────────────────────────────────
    st.markdown("""
    <div class="fg-convo-header">
        <div class="fg-convo-title">The Founder's Guide</div>
        <div class="fg-convo-subtitle">A place to think out loud.</div>
    </div>
    <div class="fg-convo-divider"></div>
    """, unsafe_allow_html=True)

    spacer("1rem")

    # ── Opening prompt ────────────────────────────────────────────────────────
    st.markdown("""
    <div class="fg-agent-prompt">
        <p class="fg-agent-question">Every business starts somewhere.</p>
        <p class="fg-agent-question-sub">Tell me about the business you're thinking about.</p>
    </div>
    """, unsafe_allow_html=True)

    spacer("0.5rem")

    # ── ElevenLabs Conversational AI Agent ────────────────────────────────────
    # Rendered via components.html so the <script> executes inside an iframe.
    # HOOK: Conversation Summary — wire session_end event from widget here
    # HOOK: Journey Engine — analyse transcript on session close
    # HOOK: Session Reflection — surface open questions post-conversation
    # HOOK: Financial Modeler — trigger when financial topics detected
    # HOOK: Business Concept Builder — structure idea when concept solidifies
    components.html(_agent_html(), height=180, scrolling=False)

    spacer("3rem")

    # HOOK: Journey Sidebar — render_sidebar(unlocked=False)
    # HOOK: Founder Timeline — render_timeline(visible=False)
