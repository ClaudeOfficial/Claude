# Chapter 2: Multishot prompting (using examples)

Examples are often more effective than more instructions. If you can show
2–3 examples of exactly the input/output pattern you want, the model can
infer format, tone, and edge-case handling that would take paragraphs to
spell out otherwise.

## A minimal example

**Task:** classify support tickets by urgency.

```
Classify each ticket as LOW, MEDIUM, or HIGH urgency.

Ticket: "Love the app! Small typo on the pricing page."
Urgency: LOW

Ticket: "Getting a 500 error when I try to check out."
Urgency: HIGH

Ticket: "How do I change my email on file?"
Urgency: MEDIUM

Ticket: "{new ticket text}"
Urgency:
```

Three examples establish the label vocabulary, the tone of the input
(customer-facing text, not clean structured data), and roughly where the
line between categories falls — all without a paragraph of rules.

## Choosing good examples

- Cover the edge cases you actually care about, not just the easy middle
- Keep the *format* of each example identical so the pattern is obvious
- If your examples disagree with each other even slightly, the model will
  pick up on the inconsistency — review them as carefully as you'd review
  a teammate's work

## When examples aren't enough

For genuinely novel edge cases outside your examples, pair multishot
prompting with an explicit fallback instruction: "If a ticket doesn't
clearly match any of these patterns, default to MEDIUM and explain why in
one sentence."
