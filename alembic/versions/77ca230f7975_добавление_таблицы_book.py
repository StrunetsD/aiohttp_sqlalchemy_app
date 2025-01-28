"""Добавление таблицы book

Revision ID: 77ca230f7975
Revises: 1fd45ee953e4
Create Date: 2025-01-25 16:02:38.098699

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '77ca230f7975'
down_revision: Union[str, None] = '1fd45ee953e4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
