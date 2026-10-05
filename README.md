# Codex Engineering Demo

A tiny FastAPI application used to demonstrate agentic software engineering.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

## Test

```bash
pytest -q
```

On Windows, create and activate a virtual environment before installing dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q
```