"""
Conversation Engine — Placeholder Hook
---------------------------------------
Future: Replace placeholder responses with live AI (e.g. OpenAI, Anthropic).
This module will own all prompt construction, response streaming,
and context window management.
"""

import time
import random


# ── Placeholder opening prompt ────────────────────────────────────────────────

OPENING_MESSAGE = (
    "Every business starts somewhere. "
    "Tell me about the business you're thinking about."
)


# ── Placeholder responses ─────────────────────────────────────────────────────

_PLACEHOLDER_RESPONSES = [
    "That's a genuinely interesting direction. What draws you to this particular idea — is it something you've experienced personally, or did you spot a gap somewhere?",
    "I'm curious — when you imagine this working really well, what does a day in that business look like for you?",
    "It sounds like there's real energy behind this. Who do you picture as the person who needs what you're building the most?",
    "Let's slow down here for a second. What's the assumption you feel least certain about right now?",
    "That's a meaningful problem to solve. Have you had any conversations with people who face this challenge today?",
    "Tell me more about the 'why now' — what makes this the right moment for an idea like this?",
    "I notice you mentioned [topic]. Is that the core of the idea, or more of a starting point for something bigger?",
    "What would it look like if this worked beyond your wildest expectations? Paint me a picture.",
    "Every founder reaches a moment of doubt. What's the version of doubt you're carrying about this right now?",
    "That's a strong instinct. What evidence, even small evidence, have you already seen that points you in this direction?",
]


# ── Public interface ──────────────────────────────────────────────────────────

def get_response(user_message: str, conversation_history: list) -> str:
    """
    PLACEHOLDER — returns a thoughtful-sounding response.

    Future implementation:
    - Build prompt from conversation_history + user_message
    - Call AI provider (OpenAI / Anthropic / etc.)
    - Stream tokens back to UI
    - Log exchange to Founder Memory
    """
    time.sleep(0.8)  # simulate latency
    return random.choice(_PLACEHOLDER_RESPONSES)


def get_opening_message() -> str:
    """Return the first message shown to the founder."""
    return OPENING_MESSAGE


def build_system_prompt(founder_context: dict) -> str:
    """
    PLACEHOLDER — construct a system prompt from founder memory.

    Future: Load founder profile, prior sessions, journey stage.
    """
    return ""


def stream_response(user_message: str, conversation_history: list):
    """
    PLACEHOLDER — generator for token streaming.

    Future: yield tokens as they arrive from the AI provider.
    """
    response = get_response(user_message, conversation_history)
    for word in response.split():
        yield word + " "
        time.sleep(0.04)
