---
name: comunity-backend
description: Work on the Comunity FastAPI backend safely. Use when changing files under backend/, editing Alembic migrations, working on Supabase Auth or JWT validation, touching the minimal marketplace schema, running the local Supabase stack, or preparing Railway backend deployment configuration.
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
- The Supabase CLI owns local Auth, Postgres/PostGIS, and Mailpit. `docker-compose.yml` contains only Redis; do not add a standalone Postgres service.
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

## Supabase Auth Rules

- Preserve the FastAPI `/api/auth/*` interface; proxy Supabase Auth's public HTTP endpoints with `httpx`, not a persistent `supabase-py` client.
- Use only `SUPABASE_URL` and `SUPABASE_PUBLISHABLE_KEY`. Never add a service-role key or a shared custom JWT secret to FastAPI.
- Do not log passwords, OTPs, access tokens, refresh tokens, or upstream Auth response bodies.
- Keep `public.users.id UUID REFERENCES auth.users(id) ON DELETE CASCADE`. The security-definer signup trigger must use an empty search path, require metadata `name`, and reject public `admin` registration.
- Enable RLS on marketplace tables without `anon` or `authenticated` policies; FastAPI accesses them through its direct database connection.
- Validate access JWTs locally from JWKS (cache at most ten minutes), including allowed asymmetric algorithm, issuer, `aud=authenticated`, expiry, UUID `sub`, and `role=authenticated`. Load `is_active` and `user_type` from `public.users`; JWT metadata is not authorization data.
- Keep generic register, resend, and recovery responses to avoid account enumeration. Map invalid login credentials and refresh tokens to `401`; invalid or expired OTPs to `400`; unverified and inactive users to `403`; rate limits to `429` with `Retry-After`.

## Verification Workflow

Before finishing backend changes:

1. Activate the backend venv.
2. Run `python scripts/dev.py check`.
3. Run `python scripts/dev.py hook-run` when hook config or lintable Python files changed.
4. If migrations changed, start the local platform from repo root: `supabase start`, then copy the values from `supabase status` into `backend/.env`.
5. Run `python scripts/dev.py migrate`; this applies Alembic's application schema after the Supabase platform schema exists.
6. Verify the app readiness path can connect to the DB when relevant. Run Auth integration tests separately; normal unit tests must use mocked Supabase transport and not require the local stack.

`supabase start` requires a running Docker daemon. If Docker access fails due sandboxing, rerun the CLI command with escalation; if Docker Desktop is not running, report that local integration remains unverified. If localhost DB access fails due sandboxing, rerun the Python migration/readiness command with escalation.

## Railway Defaults

Use Railway source builds rather than Docker:

- Root directory: `backend/`
- Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
- Health check path: `/health`
- `DATABASE_URL=<Supabase pooled or direct connection URL>`
- `SUPABASE_URL=<Supabase project URL>`
- `SUPABASE_PUBLISHABLE_KEY=<Supabase publishable/anon key>`
- `RAILPACK_PYTHON_VERSION=3.12`

For hosted Auth, configure six-digit email OTPs, a 12-character password minimum,
one-hour access JWTs, default refresh-token rotation, an asymmetric signing key (ES256
preferred), and Resend custom SMTP with link tracking disabled.
