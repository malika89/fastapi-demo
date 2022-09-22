"""first commit

Revision ID: 261bac893099
Revises: 
Create Date: 2022-09-21 15:58:32.681347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '261bac893099'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('leavetype',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('has_common', sa.BOOLEAN(), nullable=True),
    sa.Column('has_indefinite', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_leavetype_id'), 'leavetype', ['id'], unique=False)
    op.create_index(op.f('ix_leavetype_name'), 'leavetype', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_leavetype_name'), table_name='leavetype')
    op.drop_index(op.f('ix_leavetype_id'), table_name='leavetype')
    op.drop_table('leavetype')
    # ### end Alembic commands ###