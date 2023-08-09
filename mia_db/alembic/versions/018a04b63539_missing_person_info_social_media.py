"""missing_person_info_social_media

Revision ID: 018a04b63539
Revises: dee18c4b2176
Create Date: 2023-07-12 13:40:16.745407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '018a04b63539'
down_revision = 'dee18c4b2176'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE IF NOT EXISTS public.missing_person_info_social_media
        (
        mia_id integer NOT NULL,
        social_media_id integer NOT NULL,
        CONSTRAINT missing_person_info_social_media_pkey PRIMARY KEY (mia_id, social_media_id),
        CONSTRAINT fk_missing_person_info_social_media_social_media FOREIGN KEY (social_media_id)
            REFERENCES public.social_media (id) MATCH SIMPLE
            ON UPDATE NO ACTION
            ON DELETE NO ACTION
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE missing_person_info_social_media;
        """
    )
