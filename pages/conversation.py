"""
Conversation Page — ElevenLabs Conversational AI
--------------------------------------------------
The ElevenLabs agent is the heart of this page.
All surrounding structure exists to frame a calm, inviting experience.

Future integration points are marked with # HOOK comments.
"""

import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.ui.helpers import load_css, spacer

AGENT_ID = "agent_4501kwy01rrxev8bwvb3mqvmk5zn"


# ── ElevenLabs widget HTML ────────────────────────────────────────────────────

def _elevenlabs_widget() -> str:
    """
    Returns the ElevenLabs ConvAI embed wrapped in a native-feeling shell.
    The script tag is included once here; Streamlit deduplicates across reruns.
    """
    return f"""
    <div class="fg-agent-shell">

        <!-- Opening prompt — sets the conversational tone -->
        <div class="fg-agent-prompt">
            <p class="fg-agent-question">
                Every business starts somewhere.
            </p>
            <p class="fg-agent-question-sub">
                Tell me about the business you're thinking about.
            </p>
        </div>

        <!-- ElevenLabs ConvAI Agent — focal point of the page -->
        <div class="fg-agent-stage">
            <elevenlabs-convai agent-id="{AGENT_ID}"></elevenlabs-convai>
        </div>

        <!-- HOOK: Founder Memory — capture + persist session context -->
        <!-- HOOK: Conversation Summary — summarise after session ends -->
        <!-- HOOK: Journey Engine — detect stage from conversation content -->
        <!-- HOOK: Session Reflection — surface questions for founder to sit with -->
        <!-- HOOK: Financial Modeler — trigger when financial topics emerge -->
        <!-- HOOK: Business Concept Builder — structure idea as concept matures -->

    </div>

    <!-- ElevenLabs widget script — loaded once -->
    <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
    """


# ── Main render ───────────────────────────────────────────────────────────────

def render():
    load_css()

    # ── Back navigation ───────────────────────────────────────────────────────
    col_back, col_mid, col_right = st.columns([1, 5, 1])
    with col_back:
        spacer("1.75rem")
        if st.button("← Back", key="back_btn"):
            st.session_state["page"] = "landing"
            st.rerun()

    # ── Page header ───────────────────────────────────────────────────────────
    st.markdown("""
    <div class="fg-convo-header">
        <div class="fg-convo-title">The Founder's Guide</div>
        <div class="fg-convo-subtitle">A place to think out loud.</div>
    </div>
    <div class="fg-convo-divider"></div>
    """, unsafe_allow_html=True)

    spacer("1.5rem")

    # ── ElevenLabs agent ──────────────────────────────────────────────────────
    st.markdown(_elevenlabs_widget(), unsafe_allow_html=True)

    spacer("4rem")

    # ── Hidden journey components (ready, not yet rendered) ───────────────────
    # from components.journey.sidebar import render_sidebar
    # from components.journey.timeline import render_timeline
    # render_sidebar(unlocked=False)
    # render_timeline(visible=False)
