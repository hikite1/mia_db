"""missing_person_info_current_locations

Revision ID: dee18c4b2176
Revises: 30711bfac491
Create Date: 2023-07-12 13:36:36.305744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dee18c4b2176'
down_revision = '30711bfac491'
branch_labels = None
depends_on = None


def upgrade():
            op.execute(
            """
            CREATE TABLE IF NOT EXISTS public.missing_person_info_current_locations
            (
            mia_id integer NOT NULL,
            current_locations_id integer NOT NULL,
            CONSTRAINT missing_person_info_current_locations_pkey PRIMARY KEY (mia_id, current_locations_id),
            CONSTRAINT fk_missing_person_info_current_locations_current_locations FOREIGN KEY (current_locations_id)
                REFERENCES public.current_locations (id) MATCH SIMPLE
                ON UPDATE NO ACTION
                ON DELETE NO ACTION
            );
            """
        )


def downgrade():
            op.execute(
                """
                DROP TABLE missing_person_info_current_locations;
                """
            )
