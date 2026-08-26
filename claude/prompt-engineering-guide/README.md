# Prompt Engineering Guide

A practical, example-driven guide to writing effective prompts for language
models — clarity, examples, chain-of-thought, structure, and system
prompts. Every chapter leads with runnable-in-your-head examples rather
than abstract advice.

## Table of contents

1. [Being clear and direct](chapters/01-clear-and-direct.md)
2. [Multishot prompting with examples](chapters/02-multishot-examples.md)
3. [Chain of thought](chapters/03-chain-of-thought.md)
4. [XML tags for structure](chapters/04-xml-tags.md)
5. [System prompts and role assignment](chapters/05-system-prompts.md)

## See it in action

`examples/compare_prompts.py` is a small, dependency-free script that
illustrates how a vague vs. a clear prompt tends to shift response
specificity — using a mock responder so it runs with no API key:

```bash
python examples/compare_prompts.py
```

## Who this is for

Anyone writing prompts for an LLM-backed feature, script, or agent — not
just researchers. The techniques here are deliberately low-tech: no
frameworks, no special tooling, just how to phrase a request so the model
has the best shot at getting it right the first time.

## License

MIT — see [LICENSE](LICENSE).
