"""add fk to posts

Revision ID: b8ecd8268408
Revises: b4395764e36d
Create Date: 2025-11-30 20:35:13.515973

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b8ecd8268408'
down_revision: Union[str, Sequence[str], None] = 'b4395764e36d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key(
        'posts_owner_id_fkey',
        'posts', 'users',
        ['owner_id'], ['id'],
        ondelete='CASCADE'
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('posts_owner_id_fkey', 'posts', type_='foreignkey')
    op.drop_column('posts', 'owner_id')
    pass
