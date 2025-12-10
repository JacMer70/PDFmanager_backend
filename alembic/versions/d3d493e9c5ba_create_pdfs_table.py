"""create pdfs table

Revision ID: d3d493e9c5ba
Revises: 
Create Date: 2025-12-10 10:28:31.770845

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd3d493e9c5ba'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'pdfs',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('name', sa.Text, nullable=False),
        sa.Column('file', sa.Text, nullable=False),
        sa.Column('selected', sa.Boolean, nullable=False, default=False)
    )

def downgrade():
    op.drop_table('pdfs')
