"""
Session Summary — Placeholder Hook
-------------------------------------
Generates a short summary at the end of each conversation.
Helps the founder reflect and gives The Guide continuity.

Future: AI-generated summaries stored in Founder Memory.
"""


def generate_summary(conversation_history: list) -> dict:
    """
    PLACEHOLDER — summarize a completed session.

    Future: call AI to produce:
      - Key topics explored
      - Insights surfaced
      - Questions to sit with
      - Suggested next step
    """
    return {
        "topics": [],
        "insights": [],
        "open_questions": [],
        "next_step": None,
    }


def format_summary_for_display(summary: dict) -> str:
    """
    PLACEHOLDER — format a summary for the founder-facing UI.
    """
    return ""


def save_summary(founder_id: str, summary: dict) -> bool:
    """
    PLACEHOLDER — persist summary to Founder Memory.
    """
    return False
