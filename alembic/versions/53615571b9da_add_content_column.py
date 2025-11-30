"""add content column

Revision ID: 53615571b9da
Revises: f5a5c0a6fc54
Create Date: 2025-11-30 14:21:16.054590

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '53615571b9da'
down_revision: Union[str, Sequence[str], None] = 'f5a5c0a6fc54'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
