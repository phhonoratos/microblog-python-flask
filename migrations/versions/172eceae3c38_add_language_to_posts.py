"""add language to posts

Revision ID: 172eceae3c38
Revises: 45d5c525b3ce
Create Date: 2021-12-16 19:44:03.148487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '172eceae3c38'
down_revision = '45d5c525b3ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
