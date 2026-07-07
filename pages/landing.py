"""
Landing Page
"""

import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.ui.helpers import load_css, spacer


def render():
    load_css()

    # ── Hero ──────────────────────────────────────────────────────────────────
    st.markdown("""
    <div class="fg-hero">
        <p class="fg-label">Welcome</p>
        <h1 class="fg-display">The Founder's Guide</h1>
        <p class="fg-tagline">Every business begins with a conversation.</p>
        <div class="fg-divider"></div>
        <p class="fg-hero-body">
            Whether your idea is still on a napkin or you've been thinking about it for years,
            this is a place to explore it.
        </p>
        <div style="text-align:left; max-width:420px; margin: 0 auto;">
            <p class="fg-body" style="margin-bottom:0.6rem; color:#5C6B4A; font-weight:500;">Together we'll:</p>
            <p class="fg-body">✦ &nbsp;Clarify your vision</p>
            <p class="fg-body">✦ &nbsp;Explore opportunities</p>
            <p class="fg-body">✦ &nbsp;Challenge assumptions</p>
            <p class="fg-body">✦ &nbsp;Discover your next step</p>
        </div>
        <div class="fg-divider"></div>
        <p class="fg-body" style="max-width:480px; text-align:center;">
            This isn't about judging your idea.<br>
            It's about helping you become a stronger founder.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ── CTA Button ────────────────────────────────────────────────────────────
    col1, col2, col3 = st.columns([1.2, 1.6, 1.2])
    with col2:
        if st.button("Begin the Conversation", key="cta_begin", use_container_width=True):
            st.session_state["page"] = "conversation"
            st.rerun()

    spacer("3rem")

    # ── Feature cards ─────────────────────────────────────────────────────────
    st.markdown("""
    <div class="fg-card-row">
        <div class="fg-card">
            <div class="fg-card-icon">🌱</div>
            <div class="fg-card-title">Explore</div>
            <div class="fg-card-body">
                Develop your idea through thoughtful conversation.
            </div>
        </div>
        <div class="fg-card">
            <div class="fg-card-icon">🔍</div>
            <div class="fg-card-title">Discover</div>
            <div class="fg-card-body">
                Identify opportunities, risks and unanswered questions.
            </div>
        </div>
        <div class="fg-card">
            <div class="fg-card-icon">📈</div>
            <div class="fg-card-title">Grow</div>
            <div class="fg-card-body">
                Build confidence one conversation at a time.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    spacer("4rem")
