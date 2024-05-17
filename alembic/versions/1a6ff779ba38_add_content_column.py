"""add content column

Revision ID: 1a6ff779ba38
Revises: 467edba263d7
Create Date: 2024-05-17 11:22:02.263802

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a6ff779ba38'
down_revision: Union[str, None] = '467edba263d7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
