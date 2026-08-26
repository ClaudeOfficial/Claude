# Claude's GitHub — repo package

This zip contains 6 real, local git repositories with genuine commit
history and working, tested code. Each one is a normal `.git` repo — clone
it, run it, push it wherever you like.

## What's inside

| Folder | What it is |
|---|---|
| `claude-anthropic/` | The special profile-README repo (rename to match your GitHub username to have it render on your profile page) |
| `constitutional-ai/` | A working critique-and-revise training loop (Python, stdlib only) |
| `claude-code/` | A working CLI tool: summarize/search/replace across a codebase (Node.js) |
| `model-context-protocol/` | A working tool-registration client/server pair (Python, stdlib only) |
| `prompt-engineering-guide/` | A 5-chapter written guide with a runnable example script |
| `red-team-eval-harness/` | A working eval-scoring harness with a mock model (Python, stdlib only) |

Every repo has real commit history (`git log` in each), a README, a LICENSE,
and code that actually runs — none of this is placeholder text.

## How to push these to your own GitHub account

For each repo you want to publish:

```bash
cd constitutional-ai        # or whichever repo
git remote add origin https://github.com/YOUR_USERNAME/constitutional-ai.git
git branch -M main
git push -u origin main
```

You'll need to have already created an empty repo of that name on
GitHub.com first (or use `gh repo create constitutional-ai --public --source=. --push`
if you have the GitHub CLI installed).

## Special note on the profile repo

GitHub renders a repo's README on your profile page automatically **only
if the repo is named exactly the same as your username** and is public.
So if your GitHub username is `jane-doe`, you'd do:

```bash
cd claude-anthropic
git remote add origin https://github.com/jane-doe/jane-doe.git
git push -u origin main
```

(You'll obviously want to edit the README's content first — it's currently
written in Claude's voice as a demo.)

## Verifying everything still works after you unzip

```bash
cd constitutional-ai && PYTHONPATH=. python3 evals/test_pipeline.py
cd ../claude-code && node tests/index.test.js
cd ../model-context-protocol && PYTHONPATH=. python3 sdk/python/test_protocol.py
cd ../red-team-eval-harness && PYTHONPATH=. python3 -m harness.run
cd ../prompt-engineering-guide && python3 examples/compare_prompts.py
```

All five should pass/run cleanly with zero external dependencies —
Python 3 and Node.js are the only requirements.
