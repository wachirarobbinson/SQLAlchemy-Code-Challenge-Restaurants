"""Description of changes

Revision ID: 952ec32c84a9
Revises: 049444a028bd
Create Date: 2023-09-09 11:19:49.638561

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '952ec32c84a9'
down_revision: Union[str, None] = '049444a028bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
