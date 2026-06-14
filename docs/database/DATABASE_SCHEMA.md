# 🗄️ Comunity - Database Schema

## Índice

1. [Diagrama ER](#diagrama-er)
2. [Tablas Principales](#tablas-principales)
3. [Relaciones](#relaciones)
4. [Índices](#índices)
5. [Queries Comunes](#queries-comunes)
6. [Migraciones](#migraciones)

---

## DIAGRAMA ER

```
┌─────────────────────┐
│      USERS          │
├─────────────────────┤
│ id (PK)             │
│ email               │
│ phone               │
│ name                │
│ avatar_url          │
│ bio                 │
│ location (Point)    │
│ is_online           │
│ rating              │
│ created_at          │
└─────────────────────┘
        │
        ├──────────────┬──────────────┬──────────────┐
        │              │              │              │
        ▼              ▼              ▼              ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ BROADCASTS   │ │CONVERSATIONS │ │TRANSACTIONS  │ │RATINGS       │
├──────────────┤ ├──────────────┤ ├──────────────┤ ├──────────────┤
│ id (PK)      │ │ id (PK)      │ │ id (PK)      │ │ id (PK)      │
│ user_id (FK) │ │ user_1 (FK)  │ │ user_1 (FK)  │ │ rater_id(FK) │
│ title        │ │ user_2 (FK)  │ │ user_2 (FK)  │ │ rated_id(FK) │
│ description  │ │ status       │ │ amount       │ │ rating       │
│ category     │ │ created_at   │ │ type         │ │ review       │
│ price        │ │ updated_at   │ │ status       │ │ created_at   │
│ location     │ └──────────────┘ │ created_at   │ └──────────────┘
│ available_h  │        │          └──────────────┘
│ expires_at   │        │
│ created_at   │        ▼
└──────────────┘ ┌──────────────┐
       │         │   MESSAGES   │
       │         ├──────────────┤
       ▼         │ id (PK)      │
┌──────────────┐ │ conv_id (FK) │
│  CATEGORIES  │ │ sender_id(FK)│
├──────────────┤ │ content      │
│ id (PK)      │ │ created_at   │
│ name         │ │ read_at      │
│ icon         │ └──────────────┘
└──────────────┘
```

---

## TABLAS PRINCIPALES

### 1. USERS

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  
  -- Identidad
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20) UNIQUE,
  name VARCHAR(255) NOT NULL,
  
  -- Autenticación
  password_hash VARCHAR(255) NOT NULL,
  salt VARCHAR(255),
  
  -- Perfil
  avatar_url VARCHAR(500),
  bio TEXT,
  user_type VARCHAR(50), -- 'buyer', 'seller', 'both'
  
  -- Ubicación
  location GEOMETRY(Point, 4326),
  address VARCHAR(500),
  latitude DECIMAL(10, 8),
  longitude DECIMAL(11, 8),
  
  -- Estatus
  is_online BOOLEAN DEFAULT false,
  last_seen TIMESTAMP,
  is_verified BOOLEAN DEFAULT false,
  is_active BOOLEAN DEFAULT true,
  
  -- Reputación
  rating DECIMAL(3, 2) DEFAULT 0,
  reviews_count INTEGER DEFAULT 0,
  completion_rate DECIMAL(3, 2) DEFAULT 0,
  transactions_count INTEGER DEFAULT 0,
  earnings_total DECIMAL(12, 2) DEFAULT 0,
  earnings_month DECIMAL(12, 2) DEFAULT 0,
  
  -- Preferencias
  preferred_categories VARCHAR(255)[], -- Array
  notification_settings JSONB,
  
  -- Metadata
  device_token VARCHAR(500), -- Para push notifications
  device_type VARCHAR(50), -- 'ios', 'android', 'web'
  last_ip_address VARCHAR(45),
  
  -- Timestamps
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  deleted_at TIMESTAMP
);

-- Índices
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_phone ON users(phone);
CREATE INDEX idx_users_location ON users USING GIST(location);
CREATE INDEX idx_users_is_online ON users(is_online);
CREATE INDEX idx_users_created_at ON users(created_at);
```

### 2. BROADCASTS

```sql
CREATE TABLE broadcasts (
  id SERIAL PRIMARY KEY,
  
  -- Relaciones
  user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  
  -- Contenido
  title VARCHAR(255) NOT NULL,
  description TEXT,
  category VARCHAR(100) NOT NULL,
  type VARCHAR(50), -- 'food', 'service', 'item', 'job', 'request', 'class'
  
  -- Precios y disponibilidad
  price_text VARCHAR(255), -- "$40/hora", "$300 proyecto", "negociable"
  price_min DECIMAL(10, 2),
  price_max DECIMAL(10, 2),
  available_hours INTEGER,
  broadcast_until TIMESTAMP NOT NULL,
  
  -- Ubicación
  location GEOMETRY(Point, 4326) NOT NULL,
  address VARCHAR(500),
  latitude DECIMAL(10, 8),
  longitude DECIMAL(11, 8),
  
  -- Estadísticas
  views INTEGER DEFAULT 0,
  contacts_received INTEGER DEFAULT 0,
  
  -- Estatus
  status VARCHAR(50) DEFAULT 'active', -- 'active', 'paused', 'expired', 'completed'
  
  -- Imágenes
  images VARCHAR(500)[],
  main_image VARCHAR(500),
  
  -- Metadata
  tags VARCHAR(100)[],
  custom_fields JSONB, -- Para campos adicionales por categoría
  
  -- Timestamps
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  expires_at TIMESTAMP
);

-- Índices
CREATE INDEX idx_broadcasts_user ON broadcasts(user_id);
CREATE INDEX idx_broadcasts_location ON broadcasts USING GIST(location);
CREATE INDEX idx_broadcasts_category ON broadcasts(category);
CREATE INDEX idx_broadcasts_type ON broadcasts(type);
CREATE INDEX idx_broadcasts_status ON broadcasts(status);
CREATE INDEX idx_broadcasts_expires ON broadcasts(broadcast_until);
CREATE INDEX idx_broadcasts_created ON broadcasts(created_at);
```

### 3. CONVERSATIONS

```sql
CREATE TABLE conversations (
  id SERIAL PRIMARY KEY,
  
  -- Relaciones
  broadcast_id INTEGER REFERENCES broadcasts(id) ON DELETE SET NULL,
  initiator_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  responder_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  
  -- Contexto
  offer_title VARCHAR(255),
  offer_category VARCHAR(100),
  
  -- Estatus
  status VARCHAR(50) DEFAULT 'active', -- 'active', 'completed', 'cancelled', 'archived'
  
  -- Metadata
  last_message_at TIMESTAMP,
  initiator_read_at TIMESTAMP,
  responder_read_at TIMESTAMP,
  
  -- Timestamps
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  completed_at TIMESTAMP
);

-- Índices
CREATE INDEX idx_conversations_initiator ON conversations(initiator_id);
CREATE INDEX idx_conversations_responder ON conversations(responder_id);
CREATE INDEX idx_conversations_broadcast ON conversations(broadcast_id);
CREATE INDEX idx_conversations_status ON conversations(status);
CREATE INDEX idx_conversations_created ON conversations(created_at);
```

### 4. MESSAGES

```sql
CREATE TABLE messages (
  id SERIAL PRIMARY KEY,
  
  -- Relaciones
  conversation_id INTEGER NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
  sender_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  
  -- Contenido
  content TEXT NOT NULL,
  message_type VARCHAR(50) DEFAULT 'text', -- 'text', 'image', 'location', 'offer'
  
  -- Attachments
  attachment_url VARCHAR(500),
  attachment_type VARCHAR(50), -- 'image', 'document', 'location'
  
  -- Estatus de lectura
  is_read BOOLEAN DEFAULT false,
  read_at TIMESTAMP,
  
  -- Timestamps
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices
CREATE INDEX idx_messages_conversation ON messages(conversation_id);
CREATE INDEX idx_messages_sender ON messages(sender_id);
CREATE INDEX idx_messages_created ON messages(created_at);
CREATE INDEX idx_messages_is_read ON messages(is_read);
```

### 5. TRANSACTIONS

```sql
CREATE TABLE transactions (
  id SERIAL PRIMARY KEY,
  
  -- Relaciones
  conversation_id INTEGER REFERENCES conversations(id),
  broadcast_id INTEGER REFERENCES broadcasts(id),
  buyer_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  seller_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  
  -- Detalles de transacción
  title VARCHAR(255) NOT NULL,
  description TEXT,
  category VARCHAR(100),
  
  -- Dinero
  amount DECIMAL(10, 2) NOT NULL,
  currency VARCHAR(3) DEFAULT 'USD',
  commission_amount DECIMAL(10, 2),
  commission_rate DECIMAL(5, 2) DEFAULT 5,
  net_amount DECIMAL(10, 2),
  
  -- Pagos
  payment_method VARCHAR(50), -- 'cash', 'escrow', 'stripe', 'transfer'
  payment_status VARCHAR(50) DEFAULT 'pending', -- 'pending', 'completed', 'failed', 'refunded'
  stripe_payment_id VARCHAR(255),
  
  -- Escrow
  escrow_status VARCHAR(50), -- 'pending', 'held', 'released', 'disputed'
  escrow_released_at TIMESTAMP,
  
  -- Información de entrega
  delivery_address VARCHAR(500),
  delivery_date DATE,
  delivery_time TIME,
  delivery_completed BOOLEAN DEFAULT false,
  delivery_completed_at TIMESTAMP,
  
  -- Calificaciones
  buyer_rating INTEGER, -- 1-5
  seller_rating INTEGER, -- 1-5
  buyer_review TEXT,
  seller_review TEXT,
  buyer_rated_at TIMESTAMP,
  seller_rated_at TIMESTAMP,
  
  -- Estatus general
  status VARCHAR(50) DEFAULT 'pending', -- 'pending', 'confirmed', 'in_progress', 'completed', 'cancelled', 'disputed'
  
  -- Metadata
  custom_fields JSONB,
  
  -- Timestamps
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  completed_at TIMESTAMP
);

-- Índices
CREATE INDEX idx_transactions_buyer ON transactions(buyer_id);
CREATE INDEX idx_transactions_seller ON transactions(seller_id);
CREATE INDEX idx_transactions_conversation ON transactions(conversation_id);
CREATE INDEX idx_transactions_status ON transactions(status);
CREATE INDEX idx_transactions_payment_status ON transactions(payment_status);
CREATE INDEX idx_transactions_created ON transactions(created_at);
```

### 6. RATINGS

```sql
CREATE TABLE ratings (
  id SERIAL PRIMARY KEY,
  
  -- Relaciones
  transaction_id INTEGER REFERENCES transactions(id),
  rater_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  rated_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  
  -- Calificación
  rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
  review TEXT,
  
  -- Categorías de rating
  communication_rating INTEGER,
  professionalism_rating INTEGER,
  timeliness_rating INTEGER,
  value_rating INTEGER,
  
  -- Metadata
  is_verified_transaction BOOLEAN DEFAULT false,
  helpful_count INTEGER DEFAULT 0,
  unhelpful_count INTEGER DEFAULT 0,
  
  -- Estatus
  is_public BOOLEAN DEFAULT true,
  is_flagged BOOLEAN DEFAULT false,
  
  -- Timestamps
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices
CREATE INDEX idx_ratings_rater ON ratings(rater_id);
CREATE INDEX idx_ratings_rated ON ratings(rated_id);
CREATE INDEX idx_ratings_transaction ON ratings(transaction_id);
CREATE INDEX idx_ratings_created ON ratings(created_at);
```

### 7. USER_INTERESTS

```sql
CREATE TABLE user_interests (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  category VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_user_interests_user ON user_interests(user_id);
CREATE INDEX idx_user_interests_category ON user_interests(category);
```

### 8. SAVED_OFFERS

```sql
CREATE TABLE saved_offers (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  broadcast_id INTEGER NOT NULL REFERENCES broadcasts(id) ON DELETE CASCADE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_saved_offers_user ON saved_offers(user_id);
CREATE INDEX idx_saved_offers_broadcast ON saved_offers(broadcast_id);
UNIQUE(user_id, broadcast_id);
```

### 9. NOTIFICATIONS

```sql
CREATE TABLE notifications (
  id SERIAL PRIMARY KEY,
  
  -- Relaciones
  user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  
  -- Contenido
  title VARCHAR(255) NOT NULL,
  content TEXT,
  notification_type VARCHAR(100), -- 'message', 'offer_match', 'rating', 'payment', 'milestone'
  
  -- Target
  target_id INTEGER, -- conversation_id, broadcast_id, etc
  target_type VARCHAR(50), -- 'conversation', 'broadcast', 'transaction'
  
  -- Estatus
  is_read BOOLEAN DEFAULT false,
  read_at TIMESTAMP,
  
  -- Delivery
  delivery_channels VARCHAR(50)[], -- 'push', 'email', 'sms', 'in_app'
  
  -- Timestamps
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_notifications_user ON notifications(user_id);
CREATE INDEX idx_notifications_is_read ON notifications(is_read);
CREATE INDEX idx_notifications_created ON notifications(created_at);
```

### 10. ACTIVITY_LOG

```sql
CREATE TABLE activity_log (
  id SERIAL PRIMARY KEY,
  
  -- Usuario que realiza acción
  user_id INTEGER NOT NULL REFERENCES users(id),
  
  -- Acción
  action VARCHAR(100), -- 'created_broadcast', 'contacted_user', 'completed_transaction'
  action_type VARCHAR(50), -- 'create', 'update', 'delete', 'view'
  
  -- Target
  target_id INTEGER,
  target_type VARCHAR(100),
  
  -- Metadata
  metadata JSONB,
  ip_address VARCHAR(45),
  user_agent TEXT,
  
  -- Timestamps
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_activity_log_user ON activity_log(user_id);
CREATE INDEX idx_activity_log_action ON activity_log(action);
CREATE INDEX idx_activity_log_created ON activity_log(created_at);
```

---

## RELACIONES

### User → Broadcasts
- Un usuario puede tener múltiples broadcasts
- Cuando se elimina un usuario, sus broadcasts se eliminan
- Relación: 1:N

### User → Conversations
- Un usuario participa en múltiples conversaciones
- Puede ser initiator o responder
- Relación: N:N

### Broadcast → Conversations
- Un broadcast puede tener múltiples conversaciones
- Relación: 1:N

### Conversation → Messages
- Una conversación tiene múltiples mensajes
- Los mensajes se eliminan si la conversación se elimina
- Relación: 1:N

### Conversation → Transactions
- Una conversación puede resultar en una transacción
- Relación: 0..1:1

### Transaction → Ratings
- Una transacción puede generar múltiples ratings (buyer y seller)
- Relación: 1:N

### User → Ratings
- Un usuario puede recibir múltiples ratings
- Un usuario puede dar múltiples ratings
- Relación: N:N

---

## ÍNDICES

### Performance Índices

```sql
-- Búsqueda rápida por ubicación
CREATE INDEX idx_users_location ON users USING GIST(location);
CREATE INDEX idx_broadcasts_location ON broadcasts USING GIST(location);

-- Búsquedas de status
CREATE INDEX idx_broadcasts_status ON broadcasts(status);
CREATE INDEX idx_conversations_status ON conversations(status);
CREATE INDEX idx_transactions_status ON transactions(status);

-- Búsquedas por usuario
CREATE INDEX idx_broadcasts_user ON broadcasts(user_id);
CREATE INDEX idx_conversations_initiator ON conversations(initiator_id);
CREATE INDEX idx_conversations_responder ON conversations(responder_id);
CREATE INDEX idx_transactions_buyer ON transactions(buyer_id);
CREATE INDEX idx_transactions_seller ON transactions(seller_id);

-- Búsquedas de tiempo
CREATE INDEX idx_broadcasts_created ON broadcasts(created_at);
CREATE INDEX idx_messages_created ON messages(created_at);
CREATE INDEX idx_transactions_created ON transactions(created_at);

-- Búsquedas por estado
CREATE INDEX idx_messages_is_read ON messages(is_read);
CREATE INDEX idx_notifications_is_read ON notifications(is_read);
CREATE INDEX idx_broadcasts_expires ON broadcasts(broadcast_until);
```

---

## QUERIES COMUNES

### 1. Buscar ofertas dentro de 5km

```sql
SELECT 
  b.*,
  u.name,
  u.avatar_url,
  u.rating,
  ST_Distance(b.location::geography, 
    ST_SetSRID(ST_Point($1, $2), 4326)::geography) / 1000 as distance_km
FROM broadcasts b
JOIN users u ON b.user_id = u.id
WHERE 
  ST_DWithin(
    b.location::geography,
    ST_SetSRID(ST_Point($1, $2), 4326)::geography,
    5000 -- 5km en metros
  )
  AND b.status = 'active'
  AND b.broadcast_until > NOW()
ORDER BY distance_km ASC
LIMIT 50;
```

### 2. Buscar por categoría

```sql
SELECT * FROM broadcasts
WHERE 
  category = $1
  AND status = 'active'
  AND broadcast_until > NOW()
ORDER BY created_at DESC;
```

### 3. Obtener chat history

```sql
SELECT 
  m.*,
  u.name,
  u.avatar_url
FROM messages m
JOIN users u ON m.sender_id = u.id
WHERE m.conversation_id = $1
ORDER BY m.created_at ASC;
```

### 4. Obtener rating del usuario

```sql
SELECT 
  AVG(rating) as avg_rating,
  COUNT(*) as total_ratings,
  COUNT(CASE WHEN rating = 5 THEN 1 END) as five_star,
  COUNT(CASE WHEN rating = 4 THEN 1 END) as four_star,
  COUNT(CASE WHEN rating < 4 THEN 1 END) as low_rating
FROM ratings
WHERE rated_id = $1;
```

### 5. Ganancias del mes

```sql
SELECT 
  SUM(net_amount) as total_earnings,
  COUNT(*) as transaction_count,
  AVG(net_amount) as avg_transaction
FROM transactions
WHERE 
  seller_id = $1
  AND status = 'completed'
  AND DATE_TRUNC('month', completed_at) = DATE_TRUNC('month', NOW());
```

### 6. Búsqueda por palabra clave

```sql
SELECT 
  b.*,
  u.name,
  u.avatar_url,
  u.rating,
  TS_RANK(to_tsvector(b.title || ' ' || b.description), 
    to_tsquery($2)) as relevance
FROM broadcasts b
JOIN users u ON b.user_id = u.id
WHERE 
  to_tsvector(b.title || ' ' || b.description) @@ to_tsquery($2)
  AND b.status = 'active'
ORDER BY relevance DESC;
```

---

## MIGRACIONES

### Migration 001: Create Users Table

```sql
-- up
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20) UNIQUE,
  name VARCHAR(255) NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  avatar_url VARCHAR(500),
  bio TEXT,
  location GEOMETRY(Point, 4326),
  is_online BOOLEAN DEFAULT false,
  rating DECIMAL(3, 2) DEFAULT 0,
  reviews_count INTEGER DEFAULT 0,
  completion_rate DECIMAL(3, 2) DEFAULT 0,
  transactions_count INTEGER DEFAULT 0,
  earnings_total DECIMAL(12, 2) DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  deleted_at TIMESTAMP
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_location ON users USING GIST(location);

-- down
DROP TABLE IF EXISTS users CASCADE;
```

### Migration 002: Create Broadcasts Table

```sql
-- up
CREATE TABLE broadcasts (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  category VARCHAR(100) NOT NULL,
  type VARCHAR(50),
  price_text VARCHAR(255),
  available_hours INTEGER,
  broadcast_until TIMESTAMP NOT NULL,
  location GEOMETRY(Point, 4326) NOT NULL,
  views INTEGER DEFAULT 0,
  contacts_received INTEGER DEFAULT 0,
  status VARCHAR(50) DEFAULT 'active',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  expires_at TIMESTAMP
);

CREATE INDEX idx_broadcasts_user ON broadcasts(user_id);
CREATE INDEX idx_broadcasts_location ON broadcasts USING GIST(location);
CREATE INDEX idx_broadcasts_status ON broadcasts(status);

-- down
DROP TABLE IF EXISTS broadcasts CASCADE;
```

### Migration 003: Create Conversations & Messages

```sql
-- up
CREATE TABLE conversations (
  id SERIAL PRIMARY KEY,
  broadcast_id INTEGER REFERENCES broadcasts(id),
  initiator_id INTEGER NOT NULL REFERENCES users(id),
  responder_id INTEGER NOT NULL REFERENCES users(id),
  status VARCHAR(50) DEFAULT 'active',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  completed_at TIMESTAMP
);

CREATE TABLE messages (
  id SERIAL PRIMARY KEY,
  conversation_id INTEGER NOT NULL REFERENCES conversations(id),
  sender_id INTEGER NOT NULL REFERENCES users(id),
  content TEXT NOT NULL,
  is_read BOOLEAN DEFAULT false,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_conversations_initiator ON conversations(initiator_id);
CREATE INDEX idx_conversations_responder ON conversations(responder_id);
CREATE INDEX idx_messages_conversation ON messages(conversation_id);

-- down
DROP TABLE IF EXISTS messages CASCADE;
DROP TABLE IF EXISTS conversations CASCADE;
```

### Migration 004: Create Transactions & Ratings

```sql
-- up
CREATE TABLE transactions (
  id SERIAL PRIMARY KEY,
  conversation_id INTEGER REFERENCES conversations(id),
  broadcast_id INTEGER REFERENCES broadcasts(id),
  buyer_id INTEGER NOT NULL REFERENCES users(id),
  seller_id INTEGER NOT NULL REFERENCES users(id),
  title VARCHAR(255) NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  commission_amount DECIMAL(10, 2),
  net_amount DECIMAL(10, 2),
  payment_method VARCHAR(50),
  payment_status VARCHAR(50) DEFAULT 'pending',
  status VARCHAR(50) DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  completed_at TIMESTAMP
);

CREATE TABLE ratings (
  id SERIAL PRIMARY KEY,
  transaction_id INTEGER REFERENCES transactions(id),
  rater_id INTEGER NOT NULL REFERENCES users(id),
  rated_id INTEGER NOT NULL REFERENCES users(id),
  rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
  review TEXT,
  is_verified_transaction BOOLEAN DEFAULT false,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_transactions_buyer ON transactions(buyer_id);
CREATE INDEX idx_transactions_seller ON transactions(seller_id);
CREATE INDEX idx_ratings_rater ON ratings(rater_id);
CREATE INDEX idx_ratings_rated ON ratings(rated_id);

-- down
DROP TABLE IF EXISTS ratings CASCADE;
DROP TABLE IF EXISTS transactions CASCADE;
```

---

## BACKUP Y RESTORE

### Backup
```bash
pg_dump -U comunity -h localhost comunity_dev > backup_$(date +%Y%m%d).sql
```

### Restore
```bash
psql -U comunity -h localhost comunity_dev < backup_20250613.sql
```

---

## MONITOREO

### Ver tamaño de tablas
```sql
SELECT 
  relname as tabla,
  pg_size_pretty(pg_total_relation_size(relid)) as tamaño
FROM pg_stat_user_tables
ORDER BY pg_total_relation_size(relid) DESC;
```

### Ver queries lentas
```sql
SELECT 
  query,
  calls,
  total_time,
  mean_time
FROM pg_stat_statements
WHERE mean_time > 100
ORDER BY mean_time DESC;
```

---

**Última actualización**: Junio 2025
**Versión Schema**: 1.0
**PostgreSQL**: 13+
**PostGIS**: 3.0+
