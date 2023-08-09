"""missing_person_info_connections

Revision ID: 30711bfac491
Revises: 7135f86ecf33
Create Date: 2023-07-12 13:31:17.072331

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30711bfac491'
down_revision = '7135f86ecf33'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
    """
    CREATE TABLE IF NOT EXISTS public.missing_person_info_connections
    (
    mia_id integer NOT NULL,
    connections_id integer NOT NULL,
    CONSTRAINT missing_person_info_connections_pkey PRIMARY KEY (mia_id, connections_id),
    CONSTRAINT fk_missing_person_info_connections_connections FOREIGN KEY (connections_id)
        REFERENCES public.connections (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
    );

    """
)


def downgrade():
            op.execute(
                """
                DROP TABLE missing_person_info_connections;
                """
            )
