"""connections

Revision ID: f2959e2d25ef
Revises: 13de91b6e46d
Create Date: 2023-07-12 13:06:43.237569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2959e2d25ef'
down_revision = '13de91b6e46d'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE IF NOT EXISTS public.connections
        (
        id integer NOT NULL,
        guardians text COLLATE pg_catalog."default",
        siblings text COLLATE pg_catalog."default",
        family text COLLATE pg_catalog."default",
        children text COLLATE pg_catalog."default",
        friends text COLLATE pg_catalog."default",
        spouse text COLLATE pg_catalog."default",
        PRIMARY KEY (id)
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE connections
        """

    )
