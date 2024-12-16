"""Recreate migrations

Revision ID: 118cac78c59a
Revises: 8c287402d49f
Create Date: 2024-12-12 21:08:19.637977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '118cac78c59a'
down_revision = '8c287402d49f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_order')
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('shipping_address', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('billing_address', sa.String(length=255), nullable=False))
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DATETIME(), nullable=True))
        batch_op.drop_column('billing_address')
        batch_op.drop_column('shipping_address')

    op.create_table('_alembic_tmp_order',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('shipping_address', sa.VARCHAR(length=255), nullable=False),
    sa.Column('billing_address', sa.VARCHAR(length=255), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('total_price', sa.FLOAT(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###