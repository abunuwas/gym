"""empty message

Revision ID: 23008694660d
Revises: 
Create Date: 2017-10-06 15:31:32.663057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23008694660d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exercise',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('set',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('exercise', sa.Integer(), nullable=True),
    sa.Column('repetitions', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('weight_unit', sa.String(), nullable=True),
    sa.Column('performance', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['exercise'], ['exercise.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('set')
    op.drop_table('user')
    op.drop_table('exercise')
    # ### end Alembic commands ###