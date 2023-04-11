"""add user table

Revision ID: 9908770869fa
Revises: 2af5793c9f15
Create Date: 2023-04-06 05:59:46.403176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9908770869fa'
down_revision = '2af5793c9f15'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
