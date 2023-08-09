"""social_media

Revision ID: 7135f86ecf33
Revises: f11830a2f664
Create Date: 2023-07-12 13:28:04.506936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7135f86ecf33'
down_revision = 'f11830a2f664'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
    """
    CREATE TABLE IF NOT EXISTS public.social_media
    (
    id integer NOT NULL,
    facebook text COLLATE pg_catalog."default",
    instagram text COLLATE pg_catalog."default",
    others character varying COLLATE pg_catalog."default",
    snapchat text COLLATE pg_catalog."default",
    PRIMARY KEY (id)
    );
    """
)


def downgrade():
    op.execute(
        """
        DROP TABLE social_media;
        """
    )
