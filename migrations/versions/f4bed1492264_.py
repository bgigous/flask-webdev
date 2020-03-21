"""Add slug in Composition

Revision ID: f4bed1492264
Revises: ff49bee8f46c
Create Date: 2020-03-18 21:12:02.783173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4bed1492264'
down_revision = 'ff49bee8f46c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('compositions', sa.Column('slug', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('compositions', 'slug')
    # ### end Alembic commands ###