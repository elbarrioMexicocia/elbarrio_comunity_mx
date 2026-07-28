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

Start the local Supabase stack from the repository root. It provides Auth,
Postgres/PostGIS, and Mailpit; Docker Compose now contains only Redis.

```bash
supabase start
docker-compose up -d redis
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
- `SUPABASE_URL=<hosted project URL>`
- `SUPABASE_PUBLISHABLE_KEY=<hosted publishable/anon key>`
- `SUPABASE_JWT_ISSUER=<hosted project URL>/auth/v1` (optional override)

Configure the hosted Supabase Auth project with email confirmation, six-digit OTPs,
12-character minimum passwords, one-hour JWTs, and default refresh-token rotation.
Use an asymmetric signing key (ES256 preferred) so the API can validate access tokens
from the project JWKS without a shared JWT secret.
Configure Resend as Supabase custom SMTP (disable link tracking); SMTP credentials do
not belong in Railway. Local messages are available in Mailpit after `supabase start`.

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

Run `supabase start`, copy the local values from `supabase status` into
`backend/.env`, then apply the application migration with `python scripts/dev.py
migrate`. The Supabase CLI owns platform schemas; Alembic owns only the public
marketplace schema.

Deferred until product workflows need them: transactions, ratings, saved offers, notifications, activity logs, device state, presence, images, and analytics counters.
