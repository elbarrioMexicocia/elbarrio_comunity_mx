"""initial minimal marketplace schema

Revision ID: 202607060001
Revises:
Create Date: 2026-07-06
"""

from collections.abc import Sequence

from alembic import op

revision: str = "202607060001"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS postgis")
    op.execute(
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) NOT NULL UNIQUE,
            phone VARCHAR(20) UNIQUE,
            name VARCHAR(255) NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            user_type VARCHAR(50) NOT NULL,
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            CONSTRAINT users_user_type_check
                CHECK (user_type IN ('business_owner', 'worker', 'admin'))
        )
        """
    )
    op.execute("CREATE INDEX idx_users_email ON users(email)")
    op.execute("CREATE INDEX idx_users_user_type ON users(user_type)")

    op.execute(
        """
        CREATE TABLE broadcasts (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            title VARCHAR(255) NOT NULL,
            description TEXT,
            category VARCHAR(100) NOT NULL,
            compensation_text VARCHAR(255),
            location GEOMETRY(Point, 4326) NOT NULL,
            location_text VARCHAR(500),
            status VARCHAR(50) NOT NULL DEFAULT 'active',
            expires_at TIMESTAMPTZ,
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            CONSTRAINT broadcasts_status_check
                CHECK (status IN ('active', 'closed', 'filled', 'expired'))
        )
        """
    )
    op.execute("CREATE INDEX idx_broadcasts_user ON broadcasts(user_id)")
    op.execute("CREATE INDEX idx_broadcasts_location ON broadcasts USING GIST(location)")
    op.execute("CREATE INDEX idx_broadcasts_status ON broadcasts(status)")
    op.execute("CREATE INDEX idx_broadcasts_expires_at ON broadcasts(expires_at)")
    op.execute(
        "CREATE INDEX idx_broadcasts_active ON broadcasts(created_at DESC) "
        "WHERE status = 'active'"
    )

    op.execute(
        """
        CREATE TABLE conversations (
            id SERIAL PRIMARY KEY,
            broadcast_id INTEGER NOT NULL REFERENCES broadcasts(id) ON DELETE CASCADE,
            initiator_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            responder_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            status VARCHAR(50) NOT NULL DEFAULT 'active',
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            CONSTRAINT conversations_status_check
                CHECK (status IN ('active', 'closed')),
            CONSTRAINT conversations_participants_check
                CHECK (initiator_id <> responder_id)
        )
        """
    )
    op.execute("CREATE INDEX idx_conversations_broadcast ON conversations(broadcast_id)")
    op.execute("CREATE INDEX idx_conversations_initiator ON conversations(initiator_id)")
    op.execute("CREATE INDEX idx_conversations_responder ON conversations(responder_id)")
    op.execute("CREATE INDEX idx_conversations_status ON conversations(status)")

    op.execute(
        """
        CREATE TABLE messages (
            id SERIAL PRIMARY KEY,
            conversation_id INTEGER NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
            sender_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            content TEXT NOT NULL,
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        )
        """
    )
    op.execute("CREATE INDEX idx_messages_conversation ON messages(conversation_id)")
    op.execute("CREATE INDEX idx_messages_sender ON messages(sender_id)")
    op.execute("CREATE INDEX idx_messages_created_at ON messages(created_at)")


def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS messages")
    op.execute("DROP TABLE IF EXISTS conversations")
    op.execute("DROP TABLE IF EXISTS broadcasts")
    op.execute("DROP TABLE IF EXISTS users")
