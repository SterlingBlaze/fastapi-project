"""create posts table

Revision ID: 09d2180248ef
Revises: 468c38d7e482
Create Date: 2025-11-02 18:57:52.850147

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '09d2180248ef'
down_revision: Union[str, Sequence[str], None] = '468c38d7e482'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
