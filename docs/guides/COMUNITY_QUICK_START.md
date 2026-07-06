# Comunity Platform - Quick Start Guide

## 🚀 Get Started in 10 Minutes

### Prerequisites
```bash
# Install Python 3.12 for backend
python3.12 --version

# Install Docker Desktop for local PostGIS
docker --version

# Node.js is only needed for frontend tooling when frontend exists
node --version
```

---

## Phase 1: Local Setup (5 minutes)

### 1.1 Clone and Install
```bash
git clone https://github.com/yourusername/comunity.git
cd comunity
cd backend
python3.12 scripts/dev.py install
source .venv/bin/activate
cp .env.example .env
```

### 1.2 Start Local PostGIS
```bash
docker-compose up -d postgres
cd backend
source .venv/bin/activate
python scripts/dev.py migrate
```

### 1.3 Start Services
```bash
# Terminal 1: Backend
cd backend
source .venv/bin/activate
python scripts/dev.py run

# Terminal 2: Frontend
cd frontend && npm run dev
```

### 1.4 Hosted Database

Use Supabase for hosted PostgreSQL/PostGIS. Docker is only for local development and migration verification.

---

## Phase 2: Deploy to Railway (8 minutes)

### 2.1 Install & Login
```bash
npm install -g @railway/cli
railway login
```

### 2.2 Create Railway Project
```bash
cd comunity
railway init
```

### 2.3 Add Services
```bash
# Link to your repo
railway link <project-id>
```

### 2.4 Set Environment Variables
```bash
railway variables set ENVIRONMENT production
railway variables set DATABASE_URL <supabase-connection-url>
railway variables set JWT_SECRET $(openssl rand -hex 32)
railway variables set CLAUDE_API_KEY sk-...
```

### 2.5 Deploy Backend
```bash
railway up --detach

# Run migrations (one-time)
railway run alembic upgrade head
```

### 2.6 Deploy Frontend to Vercel
```bash
cd frontend
npm install -g vercel
vercel --prod
```

---

## Phase 3: Deferred AI Agents

AI matching workers are intentionally out of scope for the initial FastAPI scaffold. Add them after the core marketplace APIs exist and choose a Python-native queue/worker approach that fits the backend stack.

---

## Environment Variables

Create `.env` file:
```bash
# Server
ENVIRONMENT=development
PORT=5000

# Database
DATABASE_URL=postgresql+psycopg://comunity:desarrollo123@localhost:5432/comunity_dev

# Redis
REDIS_URL=redis://localhost:6379

# APIs
CLAUDE_API_KEY=sk-...
MAPBOX_TOKEN=pk-...
GOOGLE_MAPS_API_KEY=...

# Frontend
REACT_APP_API_URL=http://localhost:5000

# Security
JWT_SECRET=change_me_in_production
```

---

## File Structure
```
comunity/
├── backend/
│   ├── src/
│   │   ├── server.js
│   │   ├── db/
│   │   │   ├── migrations/
│   │   │   └── seed.js
│   │   ├── routes/
│   │   │   ├── listings.js
│   │   │   ├── users.js
│   │   │   └── matches.js
│   │   ├── agents/
│   │   │   ├── locationMatchingAgent.js
│   │   │   ├── recommendationAgent.js
│   │   │   └── qualityAgent.js
│   │   ├── workers/
│   │   │   ├── matching-worker.js
│   │   │   ├── recommendation-worker.js
│   │   │   └── quality-worker.js
│   │   └── events/
│   │       └── listingEvents.js
│   └── package.json
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   └── App.jsx
│   └── package.json
└── README.md
```

---

## Monitoring

### Check Agent Status
Agent workers are deferred. Use Railway logs for the backend service once deployed.

### View Metrics
```
http://localhost:5000/metrics

{
  "agents": {
    "matching_jobs_completed": 234,
    "matching_jobs_failed": 2,
    "avg_match_quality": 8.7,
    "avg_processing_time_ms": 2150
  }
}
```

---

## Troubleshooting

### Issue: Database Connection Error
```bash
# Check PostgreSQL is running
psql --version

# Verify connection string
psql $DATABASE_URL

# Check PostGIS is installed
psql comunity_local -c "SELECT PostGIS_version();"
```

### Issue: Redis Connection Error
```bash
# Check Redis is running
redis-cli ping
# Should return: PONG

# Check connection string
redis-cli -u $REDIS_URL ping
```

### Issue: Agent Not Matching
Agent matching is not part of the current backend scaffold.

### Issue: Matches Not Sending
Outbound notifications are not part of the current backend scaffold.

---

## Useful Commands

```bash
# Database
python scripts/dev.py migrate       # Run migrations
python scripts/dev.py migration-sql # Render migration SQL

# Development
python scripts/dev.py run  # Start backend
npm run dev:frontend       # Start frontend

# Production
uvicorn app.main:app --host 0.0.0.0 --port $PORT

# Testing
python scripts/dev.py check # Run backend checks

# Deployment
railway up --detach        # Deploy backend service

# Monitoring
railway logs               # Tail backend logs
```

---

## API Endpoints

### Listings
```bash
# Create listing
POST /api/listings
{
  "title": "Need plumber",
  "description": "Fix sink",
  "budget": 500,
  "skills_required": ["plumbing"],
  "location": {
    "latitude": 19.4326,
    "longitude": -99.1332
  }
}

# Get nearby listings
GET /api/listings/nearby?lat=19.43&lng=-99.13&radius=5

# Get matches for listing
GET /api/listings/:id/matches
```

### Users
```bash
# Get user profile
GET /api/users/:id

# Update profile
PUT /api/users/:id
{
  "skills": ["plumbing", "electrical"],
  "availability_hours": {"mon": "9-5"}
}

# Get user stats
GET /api/users/:id/stats
```

### Matches
```bash
# Get matches for user
GET /api/matches/user/:id

# Accept match
POST /api/matches/:id/accept

# Reject match
POST /api/matches/:id/reject
```

---

## Next Steps

1. ✅ Set up locally
2. ✅ Deploy to Railway
3. ✅ Enable AI agents
4. 📧 **Connect email service** (SendGrid)
5. 💳 **Add payments** (Stripe)
6. 🔔 **Enable push notifications** (Firebase)
7. 📊 **Set up analytics** (Mixpanel)
8. 🎨 **Customize branding**
9. 🚀 **Launch to beta users**

---

## Support

- **Docs**: https://docs.comunity.app
- **Issues**: https://github.com/yourusername/comunity/issues
- **Email**: support@comunity.app
- **Discord**: https://discord.gg/comunity

---

**Version**: 1.0.0
**Last Updated**: May 2025
