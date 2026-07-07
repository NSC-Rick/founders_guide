"""
Founder Journey Timeline — Hidden Placeholder
-----------------------------------------------
Displays milestone moments in the founder's journey.
Currently hidden. Will surface as the founder progresses.

Future: persist milestones to Founder Memory and render visually.
"""

MILESTONE_TEMPLATES = [
    {"id": "first_idea",       "label": "First Idea",             "icon": "💡"},
    {"id": "customer_convos",  "label": "Customer Interviews",    "icon": "🎯"},
    {"id": "first_model",      "label": "First Financial Model",  "icon": "💰"},
    {"id": "launch",           "label": "Launch",                 "icon": "🚀"},
    {"id": "first_customer",   "label": "First Customer",         "icon": "😊"},
    {"id": "first_employee",   "label": "First Employee",         "icon": "👥"},
]


def record_milestone(milestone_id: str, notes: str = "") -> dict:
    """
    PLACEHOLDER — record a milestone for the founder.

    Future: write to Founder Memory with timestamp and session reference.
    """
    return {"id": milestone_id, "notes": notes, "recorded": False}


def render_timeline(milestones: list, visible: bool = False):
    """
    HIDDEN — not called yet.

    Future: render a visual timeline with earned and upcoming milestones.
    """
    pass


def get_milestones(founder_id: str) -> list:
    """
    PLACEHOLDER — retrieve milestones for a founder.

    Future: query Founder Memory store.
    """
    return []
