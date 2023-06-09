"""added constructor and insert role static method

Revision ID: 64fd5e4299f2
Revises: d677e360a68f
Create Date: 2023-05-29 21:14:00.088841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64fd5e4299f2'
down_revision = 'd677e360a68f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roles_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('default', sa.Boolean(), nullable=True))
        batch_op.create_index(batch_op.f('ix_roles_table_default'), ['default'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roles_table', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_roles_table_default'))
        batch_op.drop_column('default')

    # ### end Alembic commands ###
