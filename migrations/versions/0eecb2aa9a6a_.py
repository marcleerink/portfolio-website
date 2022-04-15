"""empty message

Revision ID: 0eecb2aa9a6a
Revises: 157886f4a430
Create Date: 2022-04-15 13:24:04.185526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0eecb2aa9a6a'
down_revision = '157886f4a430'
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
