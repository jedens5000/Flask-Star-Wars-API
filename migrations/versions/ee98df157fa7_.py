"""empty message

Revision ID: ee98df157fa7
Revises: d325cde4b144
Create Date: 2022-05-10 23:21:09.572733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee98df157fa7'
down_revision = 'd325cde4b144'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('species', sa.Column('homeplanet', sa.String(length=120), nullable=False))
    op.add_column('species', sa.Column('avg_height', sa.String(length=120), nullable=False))
    op.add_column('species', sa.Column('avg_lifespan', sa.String(length=120), nullable=False))
    op.add_column('species', sa.Column('imgurl', sa.String(length=120), nullable=False))
    op.add_column('vehicles', sa.Column('imgurl', sa.String(length=120), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vehicles', 'imgurl')
    op.drop_column('species', 'imgurl')
    op.drop_column('species', 'avg_lifespan')
    op.drop_column('species', 'avg_height')
    op.drop_column('species', 'homeplanet')
    # ### end Alembic commands ###