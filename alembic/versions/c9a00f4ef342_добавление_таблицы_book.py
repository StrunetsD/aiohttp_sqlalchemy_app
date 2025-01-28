"""Добавление таблицы book

Revision ID: c9a00f4ef342
Revises: 77ca230f7975
Create Date: 2025-01-26 09:52:27.427708

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9a00f4ef342'
down_revision: Union[str, None] = '77ca230f7975'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
