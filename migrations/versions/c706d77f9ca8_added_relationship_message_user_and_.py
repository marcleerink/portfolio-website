"""added relationship message - user and timestamp message

Revision ID: c706d77f9ca8
Revises: 1db8792a7c5d
Create Date: 2022-04-07 13:20:28.617694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c706d77f9ca8'
down_revision = '1db8792a7c5d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('timestamp', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('message', 'timestamp')
    # ### end Alembic commands ###
