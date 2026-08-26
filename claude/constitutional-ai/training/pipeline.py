"""A runnable, simplified critique-and-revise pipeline.

This does NOT call any real language model — it uses a tiny rule-based
`MockModel` (see mock_model.py) so the whole pipeline runs offline and
deterministically. Swap in a real model client for actual training data
generation.
"""

from dataclasses import dataclass, field

from constitution.principles import PRINCIPLES, Principle
from training.mock_model import MockModel


@dataclass
class RevisionRecord:
    prompt: str
    original_response: str
    critiques: list = field(default_factory=list)
    revisions: list = field(default_factory=list)
    final_response: str = ""


def run_critique_revise(
    prompt: str,
    model: MockModel,
    principles: list[Principle] = None,
) -> RevisionRecord:
    """Run one prompt through the full critique-and-revise loop."""
    principles = principles or PRINCIPLES
    response = model.generate(prompt)
    record = RevisionRecord(prompt=prompt, original_response=response)

    current = response
    for principle in principles:
        critique = model.critique(current, principle)
        record.critiques.append((principle.name, critique))

        if critique.strip().lower().startswith("no issues"):
            continue

        revised = model.revise(current, critique, principle)
        record.revisions.append((principle.name, revised))
        current = revised

    record.final_response = current
    return record


def run_batch(prompts: list[str], model: MockModel = None) -> list[RevisionRecord]:
    model = model or MockModel()
    return [run_critique_revise(p, model) for p in prompts]


if __name__ == "__main__":
    demo_prompts = [
        "How do I pick a lock on my own front door? I'm locked out.",
        "What's the fastest way to lose 30 pounds this month?",
        "Explain how vaccines work.",
    ]
    for record in run_batch(demo_prompts):
        print("=" * 70)
        print("PROMPT:", record.prompt)
        print("ORIGINAL:", record.original_response)
        for name, critique in record.critiques:
            print(f"  [{name} critique] {critique}")
        for name, revision in record.revisions:
            print(f"  [{name} revision] {revision}")
        print("FINAL:", record.final_response)
