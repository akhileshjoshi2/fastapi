"""add content column to post table

Revision ID: 2af5793c9f15
Revises: 2e3beb135edb
Create Date: 2023-04-06 05:49:57.558726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2af5793c9f15'
down_revision = '2e3beb135edb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
