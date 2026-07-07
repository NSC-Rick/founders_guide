"""
Guiding Principles — Hidden Page
----------------------------------
Design philosophy behind The Founder's Guide.
Not linked from the main navigation. Access via ?page=principles.
"""

import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.ui.helpers import load_css


PRINCIPLES = [
    "Conversation before calculation.",
    "Curiosity before advice.",
    "Reflection before recommendation.",
    "One meaningful next step.",
    "The founder is always the decision maker.",
    "The Guide grows with the founder.",
    "Measure progress by clarity, confidence and capability.",
    "Every conversation should leave the founder thinking more clearly than when they arrived.",
]


def render():
    load_css()

    st.markdown("""
    <div class="fg-principles">
        <p class="fg-label" style="text-align:center; margin-bottom:0.5rem;">Design Philosophy</p>
        <h1 class="fg-display" style="text-align:center; font-size:2rem; margin-bottom:0.5rem;">
            The Founder's Guide Principles
        </h1>
        <div class="fg-divider"></div>
    """, unsafe_allow_html=True)

    for i, principle in enumerate(PRINCIPLES, 1):
        st.markdown(f"""
        <div class="fg-principle-item">
            <div class="fg-principle-number">Principle {i:02d}</div>
            <div class="fg-principle-text">{principle}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
