# ReAct Agent — Groq + GPT-OSS-120B

Python port of the Coursera guided project **"Automated Reasoning with GPT Assistant API: ReAct Agents"**.
The course builds a GPT-4 support agent in Node/TS on OpenAI's Assistants API. This repo rebuilds it with:

- **LLM:** Groq `openai/gpt-oss-120b` via the `openai` Python SDK (OpenAI-compatible endpoint)
- **Backend:** Python + FastAPI, managed with `uv`
- **Frontend:** React + TypeScript (later phase)

Groq has no Assistants API (no threads/runs/hosted retrieval), so the ReAct loop — reason → call tool → observe → answer — is written explicitly.

## Scope

| Phase | What | Status |
|---|---|---|
| 1 | CLI agent: chat loop + ReAct loop | env ready |
| 2 | Tools: stock price (`yfinance`), document search (BM25) | todo |
| 3 | FastAPI endpoints for threads/messages | todo |
| 4 | React chat UI with ReAct trace + token cost | todo |

Out of scope: auth, database, embeddings.

## Setup

Requires [uv](https://docs.astral.sh/uv/) and a [Groq API key](https://console.groq.com).

```bash
echo "GROQ_API_KEY=your_key" > .env
cd backend
uv sync
uv run main.py
```

## Layout

```
.env              # GROQ_API_KEY (gitignored)
backend/
  pyproject.toml  # deps: openai, python-dotenv, yfinance
  main.py         # entry point (CLI)
frontend/         # phase 4
```
