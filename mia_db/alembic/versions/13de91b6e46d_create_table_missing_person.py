"""CREATE TABLE missing_person

Revision ID: 13de91b6e46d
Revises: 
Create Date: 2023-07-11 10:20:40.788053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13de91b6e46d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE IF NOT EXISTS public.missing_person_info
        (
        mia_id SERIAL PRIMARY KEY,
        name text COLLATE pg_catalog."default" NOT NULL,
        age integer NOT NULL,
        description character varying COLLATE pg_catalog."default" NOT NULL,
        alias character varying COLLATE pg_catalog."default",
        email character varying COLLATE pg_catalog."default",
        phone_number VARCHAR(20),
        last_sighting date
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE missing_person_info
        """

    )
        
