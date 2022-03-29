"""create foto model

Revision ID: 9261c9b1d9cb
Revises: 
Create Date: 2022-03-28 14:33:23.394188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9261c9b1d9cb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('foto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slug', sa.String(length=80), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('foto')
    # ### end Alembic commands ###
