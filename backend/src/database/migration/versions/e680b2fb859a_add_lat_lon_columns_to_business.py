"""add_lat_lon_columns_to_business

Revision ID: e680b2fb859a
Revises: 
Create Date: 2024-03-28 00:24:42.087196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e680b2fb859a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
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


def downgrade() -> None:
    pass
