"""change password type to string just for developemnt

Revision ID: 42f0a5a70b22
Revises: f0aaaef45f15
Create Date: 2024-04-12 10:15:08.972407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42f0a5a70b22'
down_revision = 'f0aaaef45f15'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('business', 'password', existing_type=sa.LargeBinary, type_=sa.String(20))


def downgrade() -> None:
   op.alter_column('business', 'password', existing_type=sa.String(20), type_=sa.LargeBinary)
