# Comunity Platform - Quick Start Guide

## 🚀 Get Started in 10 Minutes

### Prerequisites
```bash
# Install Node.js 18+
node --version

# Install PostgreSQL
brew install postgresql  # macOS
# or get it from postgresql.org

# Install Redis
brew install redis  # macOS
# or get it from redis.io
```

---

## Phase 1: Local Setup (5 minutes)

### 1.1 Clone and Install
```bash
git clone https://github.com/yourusername/comunity.git
cd comunity
npm install
```

### 1.2 Create Database
```bash
# Start PostgreSQL
postgres -D /usr/local/var/postgres

# In another terminal
createdb comunity_local
psql comunity_local

# Enable extensions
CREATE EXTENSION postgis;
CREATE EXTENSION pgvector;
\q
```

### 1.3 Start Services
```bash
# Terminal 1: Backend
npm run dev

# Terminal 2: Frontend
cd frontend && npm run dev

# Terminal 3: Redis (if not running as service)
redis-server

# Terminal 4: AI Agent Workers
npm run agents:start
```

### 1.4 Seed Data
```bash
npm run db:seed
# Opens http://localhost:3000
```

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
# Add PostgreSQL
railway add --postgres

# Add Redis
railway add --redis

# Link to your repo
railway link <project-id>
```

### 2.4 Set Environment Variables
```bash
railway variables set NODE_ENV production
railway variables set JWT_SECRET $(openssl rand -hex 32)
railway variables set CLAUDE_API_KEY sk-...
```

### 2.5 Deploy Backend
```bash
railway up --detach

# Run migrations (one-time)
railway run npm run db:migrate
railway run npm run db:seed
```

### 2.6 Deploy Frontend to Vercel
```bash
cd frontend
npm install -g vercel
vercel --prod
```

---

## Phase 3: Enable AI Agents

### 3.1 Copy Agent Code
Create these files:

**agents/locationMatchingAgent.js**
```javascript
const { Anthropic } = require("@anthropic-ai/sdk");
const pool = require("../db");

class LocationMatchingAgent {
  constructor() {
    this.client = new Anthropic();
    this.model = "claude-opus-4.6";
  }

  async matchListing(listingId) {
    const listing = await pool.query(
      "SELECT * FROM listings WHERE id = $1",
      [listingId]
    );

    const nearbyUsers = await pool.query(`
      SELECT u.id, u.name, u.skills, u.email,
        ST_Distance(u.location, $1::geometry) / 1000 as km
      FROM users u
      WHERE ST_DWithin(u.location, $1::geometry, 5000)
      AND u.id != $2
      ORDER BY km ASC
      LIMIT 20
    `, [listing.rows[0].location, listing.rows[0].user_id]);

    const candidates = nearbyUsers.rows.filter(u => 
      this.hasMatchingSkills(u, listing.rows[0])
    );

    for (const candidate of candidates.slice(0, 5)) {
      const response = await this.client.messages.create({
        model: this.model,
        max_tokens: 300,
        messages: [{
          role: "user",
          content: `Generate a match score (1-10) and brief message for:
            Job: ${listing.rows[0].title}
            Candidate: ${candidate.name}, Skills: ${candidate.skills.join(", ")}`
        }]
      });

      // Save match & send notification
      await pool.query(
        `INSERT INTO matches (listing_id, user_id, ai_reasoning) 
         VALUES ($1, $2, $3)`,
        [listingId, candidate.id, response.content[0].text]
      );

      console.log(`✓ Matched ${candidate.name}`);
    }
  }

  hasMatchingSkills(user, listing) {
    const userSkills = new Set(user.skills.map(s => s.toLowerCase()));
    return listing.skills_required.some(s => 
      userSkills.has(s.toLowerCase())
    );
  }
}

module.exports = LocationMatchingAgent;
```

**workers/matching-worker.js**
```javascript
const Queue = require("bull");
const LocationMatchingAgent = require("../agents/locationMatchingAgent");

const matchingQueue = new Queue("matching", process.env.REDIS_URL);
const agent = new LocationMatchingAgent();

matchingQueue.process(async (job) => {
  console.log(`Matching listing ${job.data.listingId}...`);
  return await agent.matchListing(job.data.listingId);
});

// Trigger when listing is created
const eventEmitter = require("../events");
eventEmitter.on("listing.created", async (listing) => {
  await matchingQueue.add(
    { listingId: listing.id },
    { delay: 5000 }
  );
});

module.exports = matchingQueue;
```

### 3.2 Start Agent Workers
```bash
# In package.json, add:
"agents:start": "node workers/matching-worker.js"

# Then run:
npm run agents:start
```

### 3.3 Test Agents
```bash
# Create test listing
curl -X POST http://localhost:5000/api/listings \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Need a Plumber",
    "description": "Fix kitchen sink",
    "budget": 500,
    "skills_required": ["plumbing"],
    "location": { "latitude": 19.4326, "longitude": -99.1332 }
  }'

# Agent automatically matches nearby users
```

---

## Environment Variables

Create `.env` file:
```bash
# Server
NODE_ENV=development
PORT=5000

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/comunity_local

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
```bash
# View job queue
npm run queue:dashboard

# Check Redis
redis-cli info

# Monitor logs
tail -f logs/agents.log
```

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
```bash
# Check Redis queue
redis-cli --rdb /tmp/dump.rdb

# View job logs
npm run queue:logs

# Verify API key
echo $CLAUDE_API_KEY

# Test Claude API directly
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $CLAUDE_API_KEY" \
  -H "content-type: application/json" \
  -d '{"model":"claude-opus-4.6","max_tokens":100,"messages":[{"role":"user","content":"test"}]}'
```

### Issue: Matches Not Sending
```bash
# Check email config
npm run test:email

# Verify SendGrid API
curl https://api.sendgrid.com/v3/mail/send \
  -X POST \
  -H "Authorization: Bearer $SENDGRID_API_KEY" \
  -H "Content-Type: application/json"
```

---

## Useful Commands

```bash
# Database
npm run db:migrate          # Run migrations
npm run db:rollback        # Undo last migration
npm run db:seed            # Load sample data
npm run db:reset           # Wipe & recreate

# Development
npm run dev                # Start backend
npm run dev:frontend       # Start frontend
npm run agents:start       # Start AI workers

# Production
npm run build              # Build for production
npm start                  # Start server
npm run agents:prod        # Start workers in production

# Testing
npm test                   # Run tests
npm run test:agents        # Test AI agents
npm run test:matching      # Test matching algorithm

# Deployment
npm run deploy:railway     # Deploy to Railway
npm run deploy:heroku      # Deploy to Heroku

# Monitoring
npm run metrics            # Show metrics
npm run logs               # Tail logs
npm run queue:status       # Check job queue
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
