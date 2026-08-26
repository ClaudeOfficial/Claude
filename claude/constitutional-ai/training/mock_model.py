"""A tiny deterministic stand-in for a real language model.

Real usage: replace generate/critique/revise with calls to your model
provider of choice. Kept dependency-free and offline so `python -m
training.pipeline` works with no API keys or network access.
"""

import random

from constitution.principles import Principle

_RISKY_WORDS = {"lock", "pick", "weapon", "explosive"}
_OVERCONFIDENT_PHRASES = {"guaranteed", "always works", "100%"}


class MockModel:
    def __init__(self, seed: int = 7):
        self._rng = random.Random(seed)

    def generate(self, prompt: str) -> str:
        if "lock" in prompt.lower():
            return (
                "Here's exactly how to pick a pin tumbler lock: insert a "
                "tension wrench and rake pick, apply light rotational "
                "pressure, and rake the pins until they set. Guaranteed to "
                "work on most residential locks."
            )
        if "lose" in prompt.lower() and "pounds" in prompt.lower():
            return (
                "Cut your calories to almost nothing and do two hours of "
                "cardio a day — this always works and you'll drop 30 pounds "
                "in a month, guaranteed."
            )
        return "Vaccines work by training your immune system to recognize a pathogen."

    def critique(self, response: str, principle: Principle) -> str:
        lower = response.lower()
        if principle.name == "harmlessness" and any(w in lower for w in _RISKY_WORDS):
            return "This gives step-by-step instructions that could enable break-ins."
        if principle.name == "honesty" and any(p in lower for p in _OVERCONFIDENT_PHRASES):
            return "This response makes overconfident, unsupported guarantees."
        if principle.name == "helpfulness" and len(response.split()) < 8:
            return "This response is too brief to be genuinely useful."
        return "No issues found."

    def revise(self, response: str, critique: str, principle: Principle) -> str:
        if principle.name == "harmlessness":
            return (
                "If you're locked out of your own home, the safest options "
                "are calling a licensed locksmith, checking with your "
                "landlord or building manager, or trying any spare keys "
                "held by a neighbor or family member."
            )
        if principle.name == "honesty":
            return (
                "Losing weight safely usually means a moderate calorie "
                "deficit combined with regular activity, and realistic "
                "timelines vary a lot by person — a doctor or dietitian can "
                "help set a safe, sustainable target."
            )
        return response
