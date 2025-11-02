"""add user table

Revision ID: 324f85b5c849
Revises: 5349b9db1d6e
Create Date: 2025-11-02 19:19:23.142891

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '324f85b5c849'
down_revision: Union[str, Sequence[str], None] = '5349b9db1d6e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('email', sa.String(), nullable=False, unique=True),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                               server_default=sa.text('NOW()'), nullable=False),
                    # if primary key set above does not work, use the line below
                    # sa.PrimaryKeyConstraint('id')
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
    pass
