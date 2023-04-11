"""add last few columns to posts table

Revision ID: 7ddd1b0159ab
Revises: b4dbe371cdc2
Create Date: 2023-04-11 05:44:19.004833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ddd1b0159ab'
down_revision = 'b4dbe371cdc2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='True'),)

    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
