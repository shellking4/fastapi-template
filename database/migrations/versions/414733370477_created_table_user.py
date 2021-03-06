"""created table user

Revision ID: 414733370477
Revises: 
Create Date: 2022-03-08 11:52:32.842853

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '414733370477'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('roles', sa.ARRAY(sa.Enum('GHOST', 'ADMIN', 'MANAGER', 'USER', name='userrole', native_enum=False)), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
