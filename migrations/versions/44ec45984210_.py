"""support multiple video formats

Revision ID: 44ec45984210
Revises: 89adeec916e0
Create Date: 2018-11-01 15:51:44.234359

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '44ec45984210'
down_revision = '89adeec916e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('gif_location', sa.String(length=128), nullable=True))
    op.add_column('video', sa.Column('mp4_location', sa.String(length=128), nullable=True))
    op.add_column('video', sa.Column('webm_location', sa.String(length=128), nullable=True))
    op.drop_column('video', 'location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('location', mysql.VARCHAR(length=128), nullable=True))
    op.drop_column('video', 'webm_location')
    op.drop_column('video', 'mp4_location')
    op.drop_column('video', 'gif_location')
    # ### end Alembic commands ###
