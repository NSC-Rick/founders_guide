"""
Voice Interface — ElevenLabs Placeholder Hook
-----------------------------------------------
Will enable voice input (transcription) and voice output (TTS)
for a hands-free conversational experience.

Future: integrate ElevenLabs API and browser microphone access.
"""


def speak(text: str, voice_id: str = "default") -> bool:
    """
    PLACEHOLDER — synthesize text to speech via ElevenLabs.

    Future:
    - Call ElevenLabs TTS API
    - Stream audio back to the browser
    - Support custom voice selection
    """
    return False


def transcribe_audio(audio_bytes: bytes) -> str:
    """
    PLACEHOLDER — transcribe recorded audio to text.

    Future:
    - Accept audio from st_audiorec or browser MediaRecorder
    - Send to Whisper / ElevenLabs STT
    - Return transcription string
    """
    return ""


def is_voice_available() -> bool:
    """
    PLACEHOLDER — check if voice services are configured.

    Future: verify ELEVENLABS_API_KEY is present.
    """
    return False
