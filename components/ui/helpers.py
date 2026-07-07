"""
UI Helpers — Shared utilities for rendering.
"""

import os
import streamlit as st


def load_css():
    """Inject the main stylesheet into the Streamlit app."""
    css_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        "styles",
        "main.css",
    )
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def spacer(height: str = "2rem"):
    """Render a vertical spacer."""
    st.markdown(f'<div style="height:{height};"></div>', unsafe_allow_html=True)


def centered_button(label: str, key: str) -> bool:
    """Render a centered CTA button. Returns True when clicked."""
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        return st.button(label, key=key, use_container_width=True)
