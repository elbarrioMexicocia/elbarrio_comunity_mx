"""initial Supabase-backed marketplace schema

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
        CREATE TABLE public.users (
            id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
            email VARCHAR(255) NOT NULL UNIQUE,
            phone VARCHAR(20),
            name VARCHAR(255) NOT NULL,
            user_type VARCHAR(50) NOT NULL,
            is_active BOOLEAN NOT NULL DEFAULT TRUE,
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            CONSTRAINT users_user_type_check
                CHECK (user_type IN ('business_owner', 'worker', 'admin'))
        )
        """
    )
    op.execute("CREATE INDEX idx_users_user_type ON public.users(user_type)")
    op.execute(
        """
        CREATE FUNCTION public.handle_auth_user_signup()
        RETURNS TRIGGER
        LANGUAGE plpgsql
        SECURITY DEFINER
        SET search_path = ''
        AS $$
        DECLARE
            profile_name TEXT := NEW.raw_user_meta_data ->> 'name';
            profile_type TEXT := NEW.raw_user_meta_data ->> 'user_type';
            profile_phone TEXT := NULLIF(NEW.raw_user_meta_data ->> 'phone', '');
        BEGIN
            IF profile_name IS NULL OR btrim(profile_name) = '' THEN
                RAISE EXCEPTION 'signup name is required';
            END IF;
            IF profile_type NOT IN ('business_owner', 'worker') THEN
                RAISE EXCEPTION 'public signup role is invalid';
            END IF;
            INSERT INTO public.users (id, email, name, phone, user_type)
            VALUES (NEW.id, NEW.email, btrim(profile_name), profile_phone, profile_type);
            RETURN NEW;
        END;
        $$;
        CREATE TRIGGER on_auth_user_created
            AFTER INSERT ON auth.users
            FOR EACH ROW EXECUTE FUNCTION public.handle_auth_user_signup();
        """
    )
    op.execute(
        """
        CREATE TABLE public.broadcasts (
            id SERIAL PRIMARY KEY,
            user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
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
    op.execute("CREATE INDEX idx_broadcasts_user ON public.broadcasts(user_id)")
    op.execute("CREATE INDEX idx_broadcasts_location ON public.broadcasts USING GIST(location)")
    op.execute("CREATE INDEX idx_broadcasts_status ON public.broadcasts(status)")
    op.execute("CREATE INDEX idx_broadcasts_expires_at ON public.broadcasts(expires_at)")
    op.execute(
        "CREATE INDEX idx_broadcasts_active ON public.broadcasts(created_at DESC) "
        "WHERE status = 'active'"
    )
    op.execute(
        """
        CREATE TABLE public.conversations (
            id SERIAL PRIMARY KEY,
            broadcast_id INTEGER NOT NULL REFERENCES public.broadcasts(id) ON DELETE CASCADE,
            initiator_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
            responder_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
            status VARCHAR(50) NOT NULL DEFAULT 'active',
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            CONSTRAINT conversations_status_check CHECK (status IN ('active', 'closed')),
            CONSTRAINT conversations_participants_check CHECK (initiator_id <> responder_id)
        )
        """
    )
    op.execute("CREATE INDEX idx_conversations_broadcast ON public.conversations(broadcast_id)")
    op.execute("CREATE INDEX idx_conversations_initiator ON public.conversations(initiator_id)")
    op.execute("CREATE INDEX idx_conversations_responder ON public.conversations(responder_id)")
    op.execute("CREATE INDEX idx_conversations_status ON public.conversations(status)")
    op.execute(
        """
        CREATE TABLE public.messages (
            id SERIAL PRIMARY KEY,
            conversation_id INTEGER NOT NULL REFERENCES public.conversations(id) ON DELETE CASCADE,
            sender_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
            content TEXT NOT NULL,
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        )
        """
    )
    op.execute("CREATE INDEX idx_messages_conversation ON public.messages(conversation_id)")
    op.execute("CREATE INDEX idx_messages_sender ON public.messages(sender_id)")
    op.execute("CREATE INDEX idx_messages_created_at ON public.messages(created_at)")
    for table in ("users", "broadcasts", "conversations", "messages"):
        op.execute(f"ALTER TABLE public.{table} ENABLE ROW LEVEL SECURITY")


def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS public.messages")
    op.execute("DROP TABLE IF EXISTS public.conversations")
    op.execute("DROP TABLE IF EXISTS public.broadcasts")
    op.execute("DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users")
    op.execute("DROP FUNCTION IF EXISTS public.handle_auth_user_signup()")
    op.execute("DROP TABLE IF EXISTS public.users")
