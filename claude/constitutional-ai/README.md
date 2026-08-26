# constitutional-ai

A small, runnable, offline implementation of a **Constitutional AI (CAI)**
critique-and-revise loop: a method for improving model responses using a set
of written principles instead of relying solely on human feedback labels.

This repo is intentionally simplified so it runs with **zero dependencies
and no API keys** — `training/mock_model.py` stands in for a real language
model with deterministic rule-based logic, so you can read the whole
pipeline end to end in a few minutes.

## How it works

1. Sample a response to a prompt
2. Ask the model to critique the response against a written principle
3. If there's an issue, ask the model to revise the response based on the critique
4. Move to the next principle, repeating until all principles have been checked
5. In real training, fine-tune on the revised responses and repeat

## Quickstart

```bash
git clone https://github.com/YOUR_USERNAME/constitutional-ai
cd constitutional-ai
python -m training.pipeline
```

## Run the tests

```bash
PYTHONPATH=. python evals/test_pipeline.py
# or, if you have pytest installed:
PYTHONPATH=. python -m pytest evals/ -v
```

## Project structure

```
constitution/
  principles.py     # the written principles used for critique + revision
training/
  mock_model.py      # deterministic stand-in for a real LLM
  pipeline.py         # the critique-and-revise loop
evals/
  test_pipeline.py    # tests proving the loop actually improves responses
```

## Swapping in a real model

Replace `MockModel` in `training/mock_model.py` with a class that implements
the same three methods (`generate`, `critique`, `revise`) backed by real API
calls, and the rest of the pipeline works unchanged.

## License

MIT — see [LICENSE](LICENSE).
