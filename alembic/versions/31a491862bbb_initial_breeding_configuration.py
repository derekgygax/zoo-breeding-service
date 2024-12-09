"""initial breeding configuration

Revision ID: 31a491862bbb
Revises: 
Create Date: 2024-12-08 19:22:21.615645

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '31a491862bbb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('breeding',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('parent_1_id', sa.UUID(), nullable=False),
    sa.Column('parent_2_id', sa.UUID(), nullable=False),
    sa.Column('occurred_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('litter',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('breeding_id', sa.UUID(), nullable=True),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.Column('birth_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['breeding_id'], ['breeding.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('breeding_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('litter')
    op.drop_table('breeding')
    # ### end Alembic commands ###
