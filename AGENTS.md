# AGENTS.md

## What this repo is

A personal grab-bag of small, self-contained Python reference snippets and notes.
It is not an application or a library: there is no package, build step, or shared code between folders.

## Layout

- One top-level folder per topic or library (e.g. `nicegui/`, `sql/`, `standard-lib/`, `message_brokers/rabbitmq/`).
- Each example is usually a single runnable script, sometimes with a `README.md` or `*.md` notes file next to it.
- A few folders are mini-projects with their own `requirements.txt`, `Dockerfile`, or `compose.yml` (e.g. `docker/sample_app/`, `flask-sample-app/`, `nicegui/trial_gantt_chart_app/`).

## Running things

- Python virtual environment lives in `.venv/` at the repo root.
- Root `requirements.txt` covers the common dependencies. Some folders have their own `requirements.txt`; install that one when working in that folder.
- Run examples directly, e.g. `python nicegui/tts.py`.
- Tests only exist under `pytest/`: run with `pytest pytest/`.

## Conventions for adding or changing examples

- Keep examples small, focused, and runnable on their own. Prefer one concept per file.
- Put new examples in the matching topic folder, or create a new folder for a new topic.
- Name files descriptively (`<thing>_example.py`, `simple_<thing>.py`, `common_methods.py`).
- Don't introduce shared modules or cross-folder imports.
- If an example needs a new third-party dependency, add it to the nearest `requirements.txt`.
- Notes and explanations go in a Markdown file beside the code.
- Don't commit secrets. Use an `env.example` or config sample instead (see `configs/` and `docker/sample_app/`).
