"""add foreign key to post table

Revision ID: b4dbe371cdc2
Revises: 9908770869fa
Create Date: 2023-04-11 05:35:08.904837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4dbe371cdc2'
down_revision = '9908770869fa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'],
                          remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
