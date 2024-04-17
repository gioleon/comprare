"""drop_cols_latitude_longitude_in_business

Revision ID: f0aaaef45f15
Revises: d45c95831fc5
Create Date: 2024-04-12 07:42:46.361161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0aaaef45f15'
down_revision = 'd45c95831fc5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column('business', 'latitude')
    op.drop_column('business', 'longitude')


def downgrade() -> None:
    op.add_column(
        'business', 
        sa.Column(
            'latitude', 
            sa.Float,
            unique=False,
            nullable=False
        )
    )
    
    op.add_column(
        'business', 
        sa.Column(
            'longitude', 
            sa.Float,
            unique=False,
            nullable=False
        )
    )