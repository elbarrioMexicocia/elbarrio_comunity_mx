# Comunity: Same-Day Economy Platform - Technical Implementation

## The Real Vision

**Comunity** = A real-time marketplace where people **broadcast their availability and location within a 5km radius**, enabling **same-day transactions instantly**.

**NOT** about check-ins or scheduled visits.
**IS** about immediate economic activity - right now, in your neighborhood.

---

## How It Works (The User Flow)

```
Maria (freelancer) opens app
  ↓
"I'm available for 3 hours, graphic design, $40/hour"
  ↓
Broadcasts to everyone within 5km
  ↓
Juan (needs a logo) sees her offer
  ↓
Contacts Maria immediately
  ↓
They meet nearby & complete work
  ↓
Same day, same location, real money
```

**Key**: No waiting, no scheduling, no promises. Real-time matching of supply & demand.

---

## Database Schema

```sql
-- Users
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  avatar_url VARCHAR(500),
  location GEOMETRY(Point, 4326),  -- Current location
  
  -- Reputation
  rating DECIMAL(3,2),
  reviews_count INTEGER DEFAULT 0,
  completion_rate DECIMAL(3,2),
  
  -- Stats
  transactions_count INTEGER DEFAULT 0,
  earnings_month DECIMAL(10,2) DEFAULT 0,
  
  -- Status
  is_online BOOLEAN DEFAULT false,
  last_seen TIMESTAMP,
  
  created_at TIMESTAMP
);

-- Current Broadcasts (what people are offering RIGHT NOW)
CREATE TABLE broadcasts (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL,
  
  -- What they're offering
  title VARCHAR(255),  -- "Freelance web design", "Need plumber"
  description TEXT,
  category VARCHAR(100),  -- 'service', 'item', 'job', 'request'
  
  -- Price
  price_text VARCHAR(255),  -- "$40/hour", "$300 project", "negotiable"
  
  -- Availability
  available_hours INTEGER,  -- How many hours available
  broadcast_until TIMESTAMP,  -- When this offer expires
  
  -- Location
  location GEOMETRY(Point, 4326),
  
  -- Stats
  views INTEGER DEFAULT 0,
  contacts_received INTEGER DEFAULT 0,
  
  created_at TIMESTAMP,
  expires_at TIMESTAMP,
  
  FOREIGN KEY(user_id) REFERENCES users(id)
);

-- Active Conversations (real-time messaging)
CREATE TABLE conversations (
  id SERIAL PRIMARY KEY,
  broadcast_id INTEGER,
  initiator_id INTEGER,  -- Person who contacted
  responder_id INTEGER,  -- Person with broadcast
  
  status VARCHAR(50),  -- 'active', 'completed', 'cancelled'
  
  created_at TIMESTAMP,
  completed_at TIMESTAMP,
  
  FOREIGN KEY(broadcast_id) REFERENCES broadcasts(id),
  FOREIGN KEY(initiator_id) REFERENCES users(id),
  FOREIGN KEY(responder_id) REFERENCES users(id)
);

-- Messages (real-time chat)
CREATE TABLE messages (
  id SERIAL PRIMARY KEY,
  conversation_id INTEGER,
  sender_id INTEGER,
  content TEXT,
  
  created_at TIMESTAMP,
  read_at TIMESTAMP,
  
  FOREIGN KEY(conversation_id) REFERENCES conversations(id),
  FOREIGN KEY(sender_id) REFERENCES users(id)
);

-- Completed Transactions
CREATE TABLE transactions (
  id SERIAL PRIMARY KEY,
  conversation_id INTEGER,
  
  -- Parties
  provider_id INTEGER,  -- Person offering
  client_id INTEGER,  -- Person requesting
  
  -- Details
  title VARCHAR(255),
  amount DECIMAL(10,2),
  category VARCHAR(100),
  
  -- Rating
  provider_rating INTEGER,  -- 1-5
  client_rating INTEGER,  -- 1-5
  provider_review TEXT,
  client_review TEXT,
  
  completed_at TIMESTAMP,
  created_at TIMESTAMP,
  
  FOREIGN KEY(conversation_id) REFERENCES conversations(id),
  FOREIGN KEY(provider_id) REFERENCES users(id),
  FOREIGN KEY(client_id) REFERENCES users(id)
);

-- Indexes for performance
CREATE INDEX idx_broadcasts_active ON broadcasts(user_id, broadcast_until) WHERE broadcast_until > NOW();
CREATE INDEX idx_broadcasts_location ON broadcasts USING GIST(location);
CREATE INDEX idx_users_location ON users USING GIST(location);
CREATE INDEX idx_conversations_user ON conversations(initiator_id, responder_id);
CREATE INDEX idx_transactions_user ON transactions(provider_id, client_id);
```

---

## Core APIs

### 1. Get Nearby People (The Homepage)

```javascript
// Get all active broadcasts within 5km
GET /api/broadcasts/nearby?lat=19.4326&lng=-99.1332&radius_km=5

Returns: [
  {
    id: 1,
    user: { id: 10, name: "Carlos", rating: 4.8, avatar: "..." },
    title: "Plumbing repairs",
    description: "Experienced plumber, same-day service",
    price: "$30/hour",
    category: "service",
    distance_km: 0.8,
    available_hours: 4,
    expires_in_minutes: 120,
    online: true
  },
  ...
]
```

### 2. Broadcast Your Availability

```javascript
// User announces they're available
POST /api/broadcasts
{
  title: "Freelance web design",
  description: "Design landing pages, logos, social media",
  category: "service",
  price_text: "$40/hour",
  available_hours: 3,
  location: { latitude: 19.4326, longitude: -99.1332 }
}

Returns:
{
  id: 42,
  broadcast_until: "2025-05-23T18:30:00Z",
  visible_to: 12,  // people in 5km
  status: "active"
}

// Broadcast auto-expires after available_hours
```

### 3. Contact Someone

```javascript
// User wants to connect with broadcaster
POST /api/conversations
{
  broadcast_id: 42,
  message: "Hi! I need a logo designed for my startup. Are you available right now?"
}

Returns:
{
  conversation_id: 156,
  status: "active",
  // WebSocket connection opens immediately for real-time chat
}
```

### 4. Real-Time Messaging

```javascript
// WebSocket for instant messaging
WS: /socket.io/conversations/{conversation_id}

socket.emit('message', {
  content: "Yes! I can start in 30 minutes. What style are you thinking?"
})

// Both users see messages instantly
// No delays, no email notifications
```

### 5. Complete Transaction

```javascript
// After work is done, mark complete
POST /api/transactions/complete
{
  conversation_id: 156,
  amount_paid: 150,
  rating: 5,
  review: "Amazing designer, finished in 2 hours!"
}

Returns:
{
  transaction_id: 999,
  provider_notified: true,
  payment_status: "pending"  // Payment processing
}
```

---

## Real-Time Features (WebSocket)

### Live Updates

```javascript
// User's location updates
socket.emit('location-update', { lat: 19.43, lng: -99.13 })
// App recalculates who's nearby, refreshes feed

// Someone broadcasts nearby
socket.on('new-broadcast', (broadcast) => {
  // Add to feed in real-time
  feedList.insertAdjacentHTML('afterbegin', broadcastHTML)
})

// Someone messages you
socket.on('new-message', (message) => {
  // Instant notification + chat update
  showNotification(`${message.sender} replied`)
})

// Broadcast expires
socket.on('broadcast-expired', (broadcastId) => {
  // Remove from feed
  document.getElementById(`broadcast-${broadcastId}`).remove()
})
```

---

## API Endpoints Summary

```
GET    /api/broadcasts/nearby              - Feed (people nearby)
GET    /api/broadcasts/trending            - Most popular/contacted
GET    /api/broadcasts/:id                 - Broadcast details

POST   /api/broadcasts                     - Create broadcast
PUT    /api/broadcasts/:id                 - Edit broadcast
DELETE /api/broadcasts/:id                 - Cancel broadcast

POST   /api/conversations                  - Start conversation
GET    /api/conversations                  - My conversations
GET    /api/conversations/:id              - Conversation details

GET    /api/messages/:conversation_id      - Chat history
POST   /api/messages/:conversation_id      - Send message

POST   /api/transactions/complete          - Mark work done
GET    /api/transactions                   - My transactions
GET    /api/user/stats                     - My earnings, ratings

GET    /api/user/profile                   - My profile
PUT    /api/user/profile                   - Edit profile
GET    /api/user/reviews                   - My reviews
```

---

## Key Technical Decisions

### 1. Broadcasts Auto-Expire

```javascript
// Broadcasts auto-expire when available_hours pass
// No need to manually turn off
// Example: 3-hour availability = expires in 3 hours
scheduled_cleanup_job_every_minute = async () => {
  await pool.query(
    `UPDATE broadcasts SET expired_at = NOW() 
     WHERE broadcast_until < NOW() AND expired_at IS NULL`
  )
  
  // Notify users their broadcast expired
  // Suggest they post a new one
}
```

### 2. 5km is the ONLY radius (in most cities)

```javascript
// Hard-coded 5km radius
// Only adjust for very large cities (Mexico City, São Paulo, etc.)
const DEFAULT_RADIUS = 5; // km

// City-specific (optional):
const CITY_RADIUS = {
  'Mexico City': 8,
  'São Paulo': 8,
  'Buenos Aires': 6
};
```

### 3. Real-Time Location Tracking (Privacy Respectful)

```javascript
// User's location updates every 30 seconds
navigator.geolocation.watchPosition((position) => {
  // Only send to server if moved >100 meters
  if (distance > 100) {
    socket.emit('location-update', position)
  }
}, {
  enableHighAccuracy: false,  // Less battery drain
  timeout: 30000,
  maximumAge: 30000
})

// Location only stored while user is active
// Cleared when they go offline
```

### 4. Payment Integration (Optional, Not Required)

```javascript
// Transactions can be cash (local, same-day)
// OR escrow (for safety)

// Escrow flow:
// 1. Client initiates transaction
// 2. Amount held by Comunity (via Stripe)
// 3. Both parties confirm completion
// 4. Money released to provider
// 5. Comunity takes 5-10% commission

POST /api/payment/request-escrow
{
  conversation_id: 156,
  amount: 150,
  currency: "USD"
}

// For cash transactions: no escrow, no commission
// Trust-based system with reviews
```

---

## Frontend Implementation

### React Hook for Broadcasts

```javascript
// Hook to fetch nearby broadcasts
const useNearbyBroadcasts = () => {
  const [broadcasts, setBroadcasts] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Get location
    navigator.geolocation.getCurrentPosition(async (position) => {
      const { latitude, longitude } = position.coords

      // Fetch nearby broadcasts
      const response = await fetch(
        `/api/broadcasts/nearby?lat=${latitude}&lng=${longitude}`
      )

      const data = await response.json()
      setBroadcasts(data)
      setLoading(false)

      // Watch for new broadcasts
      socket.on('new-broadcast', (broadcast) => {
        if (isNearby(broadcast, latitude, longitude)) {
          setBroadcasts(prev => [broadcast, ...prev])
        }
      })
    })
  }, [])

  return { broadcasts, loading }
}
```

### Creating a Broadcast

```javascript
const BroadcastForm = () => {
  const [offering, setOffering] = useState('')
  const [price, setPrice] = useState('')
  const [hours, setHours] = useState(2)

  const handleBroadcast = async () => {
    const position = await getLocation()

    const response = await fetch('/api/broadcasts', {
      method: 'POST',
      body: JSON.stringify({
        title: offering,
        price_text: price,
        available_hours: hours,
        location: {
          latitude: position.coords.latitude,
          longitude: position.coords.longitude
        }
      })
    })

    if (response.ok) {
      showNotification(`Visible to ${response.data.visible_to} people`)
      // Form resets
      setOffering('')
      setPrice('')
    }
  }

  return (
    <div>
      <input 
        value={offering}
        onChange={e => setOffering(e.target.value)}
        placeholder="What are you offering?"
      />
      <input 
        value={price}
        onChange={e => setPrice(e.target.value)}
        placeholder="Price?"
      />
      <input 
        type="number"
        value={hours}
        onChange={e => setHours(e.target.value)}
        placeholder="Hours available?"
      />
      <button onClick={handleBroadcast}>
        Broadcast to 5km Radius
      </button>
    </div>
  )
}
```

---

## Business Model

### Revenue Streams

1. **Commission on Escrow Transactions** (5-10%)
   - User initiates escrow payment
   - Comunity holds money
   - Takes percentage on completion

2. **Premium Features** (Optional)
   - Featured broadcast ($1-2/hour boost visibility)
   - Advanced analytics for providers
   - Verified badge subscription

3. **Payment Processing** (If using cards)
   - Stripe integration = 2.2% + $0.30
   - Comunity can add 1-2% on top

### Example Economics

```
100 active users, 50 transactions/day

Scenario A: 20% use escrow ($200 avg)
- Commission 5% = $200 = $200/day = $6,000/month

Scenario B: 10% use escrow + premium features
- Commission = $100/day
- Premium = $100/day
- Total = $200/day = $6,000/month

At scale (10K users, 5K transactions/day):
- Commission-only = $100,000+/month
```

---

## Safety & Trust System

### Reputation System

```sql
-- Calculate provider rating
SELECT 
  AVG(provider_rating) as avg_rating,
  COUNT(*) as transactions,
  COUNT(CASE WHEN provider_rating >= 4 THEN 1 END)::float / COUNT(*) as satisfaction
FROM transactions
WHERE provider_id = $1
  AND completed_at > NOW() - INTERVAL '90 days'
```

### Fraud Prevention

```javascript
// Flag suspicious broadcasts
const flagSuspicious = async (broadcast) => {
  // Check 1: Brand new user?
  if (user.created_at > now() - 1_hour) {
    return flag("New user")
  }

  // Check 2: Unrealistic price?
  if (broadcast.price < 5 || broadcast.price > 500) {
    return flag("Unusual pricing")
  }

  // Check 3: Multiple broadcasts in minutes?
  if (recentBroadcasts(user) > 5) {
    return flag("Spam pattern")
  }

  // Check 4: User reported before?
  if (user.reports > 3) {
    return flag("Multiple reports")
  }

  return clean
}
```

---

## Deployment Architecture

```
Users                    WebSocket (real-time)
  ↓
Vercel (React)  ←→  Railway (FastAPI/Python)
(Frontend)              (Backend API)
                              ↓
                        PostgreSQL
                        + PostGIS
                        + Redis
                        
                        Bull Queue
                        (broadcast cleanup)
```

**Broadcast Cleanup Job** (runs every minute):

```javascript
// Mark expired broadcasts
setInterval(async () => {
  await pool.query(`
    UPDATE broadcasts 
    SET status = 'expired'
    WHERE broadcast_until < NOW() 
    AND status = 'active'
  `)
}, 60000)
```

---

## Gamification (Optional)

```
🔥 Streak: Contact 3 people in a week
💰 Earner: Make $500 in a month
⭐ Trusted: 4.8+ rating
🚀 Active: 10+ transactions
👥 Community Star: Help 5 people
```

---

## MVP Features (Build First)

- [ ] User auth + location
- [ ] Broadcast creation (5 minutes max)
- [ ] Feed of nearby broadcasts
- [ ] Real-time messaging
- [ ] Rating system
- [ ] User profiles with stats

## Phase 2 Features

- [ ] Payment escrow integration
- [ ] Advanced search/filters
- [ ] Broadcast scheduling (for later)
- [ ] Portfolio/work gallery
- [ ] Premium features
- [ ] Analytics dashboard

## Phase 3 Features

- [ ] Mobile app (iOS/Android)
- [ ] AI recommendations
- [ ] Verification system
- [ ] Insurance partnerships
- [ ] Background checks
- [ ] Multi-city support

---

## What Makes This Different

✅ **Same-Day Economy** - Real transactions happen NOW
✅ **Real-Time** - WebSocket instant messaging, no delays
✅ **Local** - 5km hyperlocal, not global
✅ **Simple** - No project management, no proposals, no schedules
✅ **Trust-Based** - Reputation system replaces contracts
✅ **For Everyone** - Services, items, jobs, requests all in one place

---

## Next Steps

1. Set up PostgreSQL + PostGIS
2. Build FastAPI backend with PostGIS-backed marketplace APIs
3. Deploy to Railway
4. Build React frontend
5. Deploy to Vercel
6. Launch with 50 local users
7. Iterate based on real usage

---

**This is the real vision: Real people, real locations, real money, same day.**
