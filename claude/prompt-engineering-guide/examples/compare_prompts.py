"""A tiny, runnable demonstration of vague vs. clear prompting.

This doesn't call a real model — `mock_respond` simulates, in a rough,
illustrative way, how response quality tends to change with prompt
clarity, so you can run this file with no API key and see the shape of
the effect described in chapters/01-clear-and-direct.md.

Run with: python examples/compare_prompts.py
"""

WEAK_PROMPT = "Write a product description for these headphones."

CLEAR_PROMPT = """Write a 2-sentence product description for these wireless
headphones, for a listing on an outdoor-gear site. Emphasize battery life
and weather resistance — our customers are hikers and trail runners, not
audiophiles."""


def mock_respond(prompt: str) -> str:
    """Illustrative only: a real model's actual output would come from an
    API call. This just shows how the same request, made vaguely vs.
    clearly, tends to shift a response's specificity."""
    if "outdoor-gear" in prompt and "hikers" in prompt:
        return (
            "Built for the trail: 40-hour battery life and an IP67 "
            "weatherproof shell mean these headphones keep up whether "
            "you're logging miles or waiting out a downpour at camp."
        )
    return (
        "These headphones offer great sound quality, a sleek design, "
        "and a comfortable fit for everyday listening."
    )


if __name__ == "__main__":
    print("=== Weak prompt ===")
    print(WEAK_PROMPT)
    print("\n--> ", mock_respond(WEAK_PROMPT))

    print("\n=== Clear prompt ===")
    print(CLEAR_PROMPT)
    print("\n--> ", mock_respond(CLEAR_PROMPT))
