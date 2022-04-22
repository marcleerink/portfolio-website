"""empty message

Revision ID: 3fcaebd13ba3
Revises: 11ab5f02542e
Create Date: 2022-04-22 18:55:39.167551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fcaebd13ba3'
down_revision = '11ab5f02542e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slug', sa.String(length=80), nullable=True),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('content', sa.String(length=10000), nullable=True),
    sa.Column('link', sa.String(length=260), nullable=True),
    sa.Column('code_link', sa.String(length=260), nullable=True),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.Column('image_url', sa.String(length=260), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('projects')
    # ### end Alembic commands ###
