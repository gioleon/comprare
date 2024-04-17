"""modification_business_entity

Revision ID: d45c95831fc5
Revises: e680b2fb859a
Create Date: 2024-04-06 11:42:49.212329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd45c95831fc5'
down_revision = 'e680b2fb859a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'business', 
        sa.Column(
            'email', 
            sa.String,
            unique=True,
            nullable=False
        )
    )
    
    op.add_column(
        'business', 
        sa.Column(
            'password', 
            sa.LargeBinary,
            unique=False,
            nullable=False
        )
    )


def downgrade() -> None:
    op.drop_column('business', 'email')
    
    op.drop_column('business', 'password')
