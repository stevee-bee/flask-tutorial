"""empty message

Revision ID: 950e3c515c0b
Revises: a563b5df99a2
Create Date: 2021-09-26 05:49:52.298953

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '950e3c515c0b'
down_revision = 'a563b5df99a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
