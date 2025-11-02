"""create posts table

Revision ID: 468c38d7e482
Revises: 
Create Date: 2025-11-02 18:52:10.073310

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '468c38d7e482'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False)
    )
    pass

# ,
#         sa.Column('content', sa.String(), nullable=False),
#         sa.Column('published', sa.Boolean(), server_default='TRUE', nullable=False),
#         sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()'), nullable=False),
#         sa.Column('owner_id', sa.Integer(), nullable=False),
#         sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ondelete='CASCADE'),
def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('posts')
    pass
