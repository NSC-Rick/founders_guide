"""
Journey Sidebar — Hidden Component
------------------------------------
This component tracks the founder's progression through key stages.
Currently hidden. Will unlock naturally as conversations deepen.

Future: render conditionally when journey_stage > 0.
"""

JOURNEY_STAGES = [
    {"id": "concept",     "label": "Business Concept",      "icon": "💡"},
    {"id": "validation",  "label": "Market Validation",     "icon": "🎯"},
    {"id": "financial",   "label": "Financial Foundations", "icon": "💰"},
    {"id": "planning",    "label": "Business Planning",     "icon": "📋"},
    {"id": "funding",     "label": "Funding",               "icon": "🏦"},
    {"id": "launch",      "label": "Launch",                "icon": "🚀"},
    {"id": "growth",      "label": "Growth",                "icon": "📈"},
    {"id": "leadership",  "label": "Leadership",            "icon": "👥"},
]


def render_sidebar(current_stage: str = "concept", unlocked: bool = False):
    """
    HIDDEN — not called yet.

    Future: import streamlit and render sidebar when unlocked=True.
    Highlights current_stage and dims future stages.
    """
    pass


def get_current_stage(conversation_history: list) -> str:
    """
    PLACEHOLDER — determine journey stage from conversation context.

    Future: analyze conversation to detect which stage the founder is in.
    """
    return "concept"
