# red-team-eval-harness

A small, runnable harness for scoring a model's responses against labeled
prompt categories (should-refuse vs. should-help), using a simple keyword
refusal detector. Ships with a mock model so `python -m harness.run` works
offline with no dependencies.

## Quickstart

```bash
git clone https://github.com/YOUR_USERNAME/red-team-eval-harness
cd red-team-eval-harness
PYTHONPATH=. python -m harness.run
```

```
Results by category:
  clearly_benign: 3/3
  borderline_should_help: 2/2
  should_refuse_or_redirect: 2/2

Overall: 7/7
```

## How it works

1. `categories/basic_categories.py` defines `(prompt, should_refuse)` pairs, grouped by category
2. `harness/runner.py` calls a `respond(prompt) -> str` function for each prompt and checks whether the response looks like a refusal
3. `harness/run.py` wires a mock model into the runner and prints a per-category and overall score

## Plugging in a real model

Replace `mock_respond` in `harness/run.py` with a function that calls your
actual model, keeping the same `(prompt: str) -> str` signature — nothing
else needs to change.

## Project structure

```
categories/
  basic_categories.py   # labeled prompt sets
harness/
  runner.py               # scoring logic
  run.py                   # entry point wiring a model into the runner
reports/
  TEMPLATE.md               # template for writing up eval run results
```

## License

MIT — see [LICENSE](LICENSE).
