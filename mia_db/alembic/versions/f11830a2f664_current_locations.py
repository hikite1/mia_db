"""current_locations

Revision ID: f11830a2f664
Revises: f2959e2d25ef
Create Date: 2023-07-12 13:22:27.377159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f11830a2f664'
down_revision = 'f2959e2d25ef'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE IF NOT EXISTS public.current_locations
        (
        id integer NOT NULL,
        addresses character varying COLLATE pg_catalog."default",
        employers character varying COLLATE pg_catalog."default",
        hangouts character varying COLLATE pg_catalog."default",
        PRIMARY KEY (id)
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE current_locations
        """

    )
