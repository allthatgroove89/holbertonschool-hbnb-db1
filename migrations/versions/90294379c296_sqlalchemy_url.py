"""sqlalchemy url

Revision ID: 90294379c296
Revises:
Create Date: 2024-07-04 20:07:45.307169

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '90294379c296'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(120), unique=True, nullable=False)
   )

def downgrade() -> None:
    op.drop_table('user')
