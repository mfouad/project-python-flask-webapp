"""empty message

Revision ID: 605fb965dcff
Revises: 
Create Date: 2018-07-11 02:17:50.461821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '605fb965dcff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('done', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tasks')
    # ### end Alembic commands ###
