"""empty message

Revision ID: c22605a38838
Revises: ee98df157fa7
Create Date: 2022-05-11 00:03:52.858064

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c22605a38838'
down_revision = 'ee98df157fa7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vehicles', 'model')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vehicles', sa.Column('model', mysql.VARCHAR(length=120), nullable=False))
    # ### end Alembic commands ###