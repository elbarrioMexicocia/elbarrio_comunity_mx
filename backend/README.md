# Comunity Backend

Initial FastAPI scaffold for the Comunity informal job marketplace.

## Local Setup

Use Python 3.12 for the backend virtualenv. Railway should use the same major/minor version.

```bash
cd backend
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env
```

Or use the backend task runner:

```bash
cd backend
python3.12 scripts/dev.py install
source .venv/bin/activate
cp .env.example .env
```

Start local PostGIS from the repository root. Docker is for local dependencies only; hosted database environments should use Supabase.

```bash
docker-compose up -d postgres
```

Run migrations:

```bash
cd backend
source .venv/bin/activate
python scripts/dev.py migrate
```

Run the API:

```bash
cd backend
source .venv/bin/activate
python scripts/dev.py run
```

Health endpoints:

- `GET /health`: app liveness, no database dependency.
- `GET /ready`: database readiness.

## Tests

```bash
cd backend
source .venv/bin/activate
python scripts/dev.py check
```

## Git Hooks

This repo uses `pre-commit` for the backend lint hook, similar to Husky in npm projects.

```bash
cd backend
source .venv/bin/activate
python scripts/dev.py hook-install
python scripts/dev.py hook-run
```

## Railway

Use Railway's source builder for the FastAPI service. Do not add an app Dockerfile until there is a concrete runtime need. Use Supabase for the hosted PostgreSQL/PostGIS database.

Recommended service config:

- Root directory: `backend/`
- Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
- Health check path: `/health`
- `RAILPACK_PYTHON_VERSION=3.12`
- `DATABASE_URL=<Supabase pooled or direct connection URL>`

Run migrations after wiring `DATABASE_URL`:

```bash
railway run alembic upgrade head
```

## Iteration 1 Schema

The first migration creates only the tables needed for the initial marketplace flow:

- `users`
- `broadcasts`
- `conversations`
- `messages`

Deferred until product workflows need them: transactions, ratings, saved offers, notifications, activity logs, device state, presence, images, and analytics counters.
