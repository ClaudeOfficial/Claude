"""Run with: python -m harness.run"""

from categories.basic_categories import CATEGORIES
from harness.runner import run_suite, summarize


def mock_respond(prompt: str) -> str:
    """A tiny stand-in model. Refuses anything mentioning lock-picking
    or making dangerous gases; answers everything else plainly."""
    lower = prompt.lower()
    if "pick" in lower and "lock" in lower:
        return "I can't help with that. Instead, I'd suggest calling a locksmith if you're locked out."
    if "dangerous gas" in lower:
        return "I can't provide that. Mixing certain household chemicals is genuinely dangerous — best to avoid it entirely."
    return f"Here's a helpful answer to: {prompt}"


def main():
    results = run_suite(CATEGORIES, mock_respond)
    summary = summarize(results)

    print("Results by category:")
    for category, stats in summary["by_category"].items():
        print(f"  {category}: {stats['correct']}/{stats['total']}")

    overall = summary["overall"]
    print(f"\nOverall: {overall['correct']}/{overall['total']}")

    print("\nDetail:")
    for r in results:
        mark = "✓" if r.correct else "✗"
        print(f"  [{mark}] ({r.category}) {r.prompt!r} -> refusal={r.actual_refusal}")


if __name__ == "__main__":
    main()
