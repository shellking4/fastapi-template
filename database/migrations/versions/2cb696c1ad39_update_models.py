"""update models

Revision ID: 2cb696c1ad39
Revises: 0780eaa309cc
Create Date: 2023-06-28 08:01:04.219185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2cb696c1ad39'
down_revision = '0780eaa309cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'lead', ['phone_work'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'lead', type_='unique')
    # ### end Alembic commands ###
