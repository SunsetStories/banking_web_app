"""account num to int

Revision ID: ed414da76afe
Revises: 6f1c4ba81c56
Create Date: 2023-06-04 21:36:40.590879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed414da76afe'
down_revision = '6f1c4ba81c56'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('accounts_table', schema=None) as batch_op:
        batch_op.alter_column('account_num',
               existing_type=sa.BIGINT(),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('accounts_table', schema=None) as batch_op:
        batch_op.alter_column('account_num',
               existing_type=sa.Integer(),
               type_=sa.BIGINT(),
               existing_nullable=False,
               autoincrement=True)

    # ### end Alembic commands ###
