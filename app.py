"""
The Founder's Guide — v0.1 Shell
----------------------------------
Entry point. Handles page routing via session state.
All business logic lives in components/; UI in pages/.
"""

import streamlit as st

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="The Founder's Guide",
    page_icon="🌱",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Session state defaults ────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state["page"] = "landing"

# ── Query param routing (e.g. ?page=principles for hidden page) ───────────────
params = st.query_params
if "page" in params:
    allowed_hidden = {"principles"}
    requested = params["page"]
    if requested in allowed_hidden:
        st.session_state["page"] = requested

# ── Router ────────────────────────────────────────────────────────────────────
page = st.session_state["page"]

if page == "landing":
    from pages.landing import render
    render()

elif page == "conversation":
    from pages.conversation import render
    render()

elif page == "principles":
    from pages.principles import render
    render()

else:
    # Fallback — should never reach here
    st.session_state["page"] = "landing"
    st.rerun()
