"""empty message

Revision ID: 46aa3b378095
Revises: None
Create Date: 2017-05-04 15:06:14.561825

"""

# revision identifiers, used by Alembic.
revision = '46aa3b378095'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('time',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('everyday', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('time')
    ### end Alembic commands ###
