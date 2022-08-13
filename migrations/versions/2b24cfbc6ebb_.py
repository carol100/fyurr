"""empty message

Revision ID: 2b24cfbc6ebb
Revises: f7c3cff84047
Create Date: 2022-08-13 17:57:30.142118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b24cfbc6ebb'
down_revision = 'f7c3cff84047'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('genres', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venues', 'genres')
    # ### end Alembic commands ###
