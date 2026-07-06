---
name: comunity-backend
description: Work on the Comunity FastAPI backend safely. Use when changing files under backend/, editing Alembic migrations, touching the minimal marketplace schema, running local PostGIS verification, or preparing Railway backend deployment configuration.
---

# Comunity Backend 

## Overview

Use this skill to preserve the backend's intentionally small first iteration. The backend is a FastAPI service deployed to Railway, with PostgreSQL/PostGIS and Alembic migrations.

## Non-Obvious Context

- Do not use `npm run` for backend work. Use Python commands from `backend/`.
- Prefer `python scripts/dev.py <task>` from an activated backend virtualenv for repeatable workflows.
- Use Python 3.12 to create the virtualenv. Railway should be configured with `RAILPACK_PYTHON_VERSION=3.12`.
- Keep app deployment Docker-free for now. `docker-compose.yml` is only for local dependencies.
- Use Supabase for hosted PostgreSQL/PostGIS. Do not add Railway Postgres unless the deployment plan changes.
- Local PostGIS uses `postgis/postgis:16-3.4` with `platform: linux/amd64` because `postgis/postgis:latest` did not run on Apple Silicon.
- `broadcasts` means the initial job/opportunity post table.

## Backend Commands

Run commands from `backend/`:

```bash
python3.12 scripts/dev.py install      # create .venv and install dev deps
source .venv/bin/activate
python scripts/dev.py run              # local API on :5000
python scripts/dev.py test             # pytest
python scripts/dev.py lint             # ruff
python scripts/dev.py check            # pytest + ruff + Alembic SQL render
python scripts/dev.py hook-install     # install pre-commit hooks
python scripts/dev.py hook-run         # run pre-commit hooks against all files
python scripts/dev.py migrate          # alembic upgrade head
python scripts/dev.py migration-sql    # render migration SQL only
```

If not using the task runner, use module form inside the venv: `python -m pytest`, `python -m ruff check .`, `python -m alembic upgrade head`, and `python -m uvicorn app.main:app ...`.

## Schema Rules

The current migration should stay minimal unless product scope expands:

- Keep iteration-1 tables: `users`, `broadcasts`, `conversations`, `messages`.
- Do not add `transactions`, `ratings`, `saved_offers`, `notifications`, or `activity_log` until their workflows exist.
- Do not add presence/device fields such as `is_online`, `device_token`, or `last_ip_address` until something maintains them.
- Keep `users.user_type` as the role field. Current values are `business_owner`, `worker`, and `admin`.
- Keep location search PostGIS-ready: `broadcasts.location GEOMETRY(Point, 4326)` with a GiST index.

## Verification Workflow

Before finishing backend changes:

1. Activate the backend venv.
2. Run `python scripts/dev.py check`.
3. Run `python scripts/dev.py hook-run` when hook config or lintable Python files changed.
4. If migrations changed, start local PostGIS from repo root: `docker-compose up -d postgres`.
5. Run `python scripts/dev.py migrate`.
6. Verify the app readiness path can connect to the DB when relevant.

If Docker access fails due sandboxing, rerun Docker commands with escalation. If localhost DB access fails due sandboxing, rerun the Python migration/readiness command with escalation.

## Railway Defaults

Use Railway source builds rather than Docker:

- Root directory: `backend/`
- Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
- Health check path: `/health`
- `DATABASE_URL=<Supabase pooled or direct connection URL>`
- `RAILPACK_PYTHON_VERSION=3.12`
