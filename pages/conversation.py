"""
Conversation Page
"""

import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.ui.helpers import load_css, spacer
from components.conversation.engine import get_response, get_opening_message
from components.ui.voice import is_voice_available


# ── Session state initialisation ──────────────────────────────────────────────

def _init_state():
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "guide", "content": get_opening_message()}
        ]
    if "input_mode" not in st.session_state:
        st.session_state["input_mode"] = "type"
    if "thinking" not in st.session_state:
        st.session_state["thinking"] = False


# ── Message rendering ─────────────────────────────────────────────────────────

def _render_messages():
    for msg in st.session_state["messages"]:
        role  = msg["role"]
        text  = msg["content"]
        is_guide = role == "guide"

        align_class  = "fg-msg-guide"  if is_guide else "fg-msg-founder"
        bubble_class = "fg-bubble-guide" if is_guide else "fg-bubble-founder"
        sender_label = "The Guide" if is_guide else "You"

        st.markdown(f"""
        <div class="fg-msg {align_class}">
            <span class="fg-msg-sender">{sender_label}</span>
            <div class="fg-bubble {bubble_class}">{text}</div>
        </div>
        """, unsafe_allow_html=True)

    if st.session_state.get("thinking"):
        st.markdown("""
        <div class="fg-msg fg-msg-guide">
            <span class="fg-msg-sender">The Guide</span>
            <div class="fg-thinking">
                <div class="fg-dot"></div>
                <div class="fg-dot"></div>
                <div class="fg-dot"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ── Input handling ────────────────────────────────────────────────────────────

def _handle_submit(user_text: str):
    if not user_text.strip():
        return

    st.session_state["messages"].append({"role": "founder", "content": user_text.strip()})
    st.session_state["thinking"] = True
    st.rerun()


def _generate_response():
    """Called on the rerun after thinking=True to produce the AI reply."""
    history = st.session_state["messages"]
    last_user_msg = next(
        (m["content"] for m in reversed(history) if m["role"] == "founder"), ""
    )
    reply = get_response(last_user_msg, history)
    st.session_state["messages"].append({"role": "guide", "content": reply})
    st.session_state["thinking"] = False


# ── Main render ───────────────────────────────────────────────────────────────

def render():
    load_css()
    _init_state()

    # If we were in "thinking" state on last render, generate now
    if st.session_state.get("thinking"):
        _generate_response()
        st.rerun()

    # ── Header ────────────────────────────────────────────────────────────────
    col_back, col_title, col_spacer = st.columns([1, 4, 1])
    with col_back:
        spacer("1.5rem")
        if st.button("← Back", key="back_btn"):
            st.session_state["page"] = "landing"
            st.rerun()

    st.markdown("""
    <div class="fg-convo-header">
        <div class="fg-convo-title">The Founder's Guide</div>
        <div class="fg-convo-subtitle">A place to think out loud.</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Message area ──────────────────────────────────────────────────────────
    st.markdown('<div class="fg-message-area">', unsafe_allow_html=True)
    _render_messages()
    st.markdown('</div>', unsafe_allow_html=True)

    spacer("5rem")

    # ── Input mode toggle ─────────────────────────────────────────────────────
    voice_available = is_voice_available()
    mode = st.session_state["input_mode"]

    toggle_cols = st.columns([2, 1, 1, 2])
    with toggle_cols[1]:
        voice_style = "background:#EEF1EA;border-color:#5C6B4A;color:#5C6B4A;font-weight:500;" if mode == "voice" else ""
        st.markdown(
            f'<div style="text-align:center;padding:0.35rem 0.75rem;border-radius:100px;'
            f'border:1px solid #E8E4DC;font-size:0.85rem;color:#7A746A;{voice_style}">🎤 Talk</div>',
            unsafe_allow_html=True,
        )
        if voice_available and st.button("🎤 Talk", key="mode_voice", use_container_width=True):
            st.session_state["input_mode"] = "voice"
            st.rerun()
        elif not voice_available:
            st.caption("Voice coming soon")

    with toggle_cols[2]:
        type_style = "background:#EEF1EA;border-color:#5C6B4A;color:#5C6B4A;font-weight:500;" if mode == "type" else ""
        st.markdown(
            f'<div style="text-align:center;padding:0.35rem 0.75rem;border-radius:100px;'
            f'border:1px solid #E8E4DC;font-size:0.85rem;color:#7A746A;{type_style}">⌨ Type</div>',
            unsafe_allow_html=True,
        )

    spacer("0.5rem")

    # ── Text input ────────────────────────────────────────────────────────────
    with st.form(key="message_form", clear_on_submit=True):
        input_col, btn_col = st.columns([5, 1])
        with input_col:
            user_input = st.text_input(
                label="",
                placeholder="Share what's on your mind…",
                label_visibility="collapsed",
                key="user_input_field",
            )
        with btn_col:
            spacer("0.35rem")
            submitted = st.form_submit_button("Send")

        if submitted and user_input:
            _handle_submit(user_input)

    spacer("2rem")

    # ── Hidden components (Journey Sidebar + Timeline) ────────────────────────
    # Sidebar and timeline are imported but not rendered until unlocked.
    # from components.journey.sidebar import render_sidebar
    # from components.journey.timeline import render_timeline
    # render_sidebar(unlocked=False)
    # render_timeline(visible=False)
