"""add password field in User table

Revision ID: 20246f1a6fb7
Revises: 
Create Date: 2016-02-19 01:13:05.080357

"""

# revision identifiers, used by Alembic.
revision = '20246f1a6fb7'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('user', sa.Column('password', sa.String(128), nullable=False))


def downgrade():
    pass
