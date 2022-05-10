"""empty message

Revision ID: 031615c865e8
Revises: d121e9fea492
Create Date: 2022-05-10 00:48:59.012967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '031615c865e8'
down_revision = 'd121e9fea492'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('population', table_name='Planets')
    op.drop_index('population_2', table_name='Planets')
    op.drop_index('surface_water', table_name='Planets')
    op.drop_index('surface_water_2', table_name='Planets')
    op.drop_index('terrain', table_name='Planets')
    op.drop_index('terrain_2', table_name='Planets')
    op.drop_index('url', table_name='Planets')
    op.drop_index('url_2', table_name='Planets')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('url_2', 'Planets', ['url'], unique=False)
    op.create_index('url', 'Planets', ['url'], unique=False)
    op.create_index('terrain_2', 'Planets', ['terrain'], unique=False)
    op.create_index('terrain', 'Planets', ['terrain'], unique=False)
    op.create_index('surface_water_2', 'Planets', ['surface_water'], unique=False)
    op.create_index('surface_water', 'Planets', ['surface_water'], unique=False)
    op.create_index('population_2', 'Planets', ['population'], unique=False)
    op.create_index('population', 'Planets', ['population'], unique=False)
    # ### end Alembic commands ###
