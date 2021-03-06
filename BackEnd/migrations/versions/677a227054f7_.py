"""empty message

Revision ID: 677a227054f7
Revises: 
Create Date: 2018-11-23 15:44:34.989946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '677a227054f7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('elective',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('electiveNo', sa.Integer(), nullable=True),
    sa.Column('courseName', sa.String(length=100), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('teacher', sa.String(length=30), nullable=True),
    sa.Column('specialization', sa.String(length=30), nullable=True),
    sa.Column('prerequisites', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_elective_courseName'), 'elective', ['courseName'], unique=False)
    op.create_index(op.f('ix_elective_description'), 'elective', ['description'], unique=False)
    op.create_index(op.f('ix_elective_prerequisites'), 'elective', ['prerequisites'], unique=False)
    op.create_index(op.f('ix_elective_specialization'), 'elective', ['specialization'], unique=False)
    op.create_index(op.f('ix_elective_teacher'), 'elective', ['teacher'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usn', sa.String(length=64), nullable=True),
    sa.Column('sem', sa.String(length=120), nullable=True),
    sa.Column('interets', sa.Text(), nullable=True),
    sa.Column('cgpa', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_cgpa'), 'user', ['cgpa'], unique=False)
    op.create_index(op.f('ix_user_interets'), 'user', ['interets'], unique=False)
    op.create_index(op.f('ix_user_sem'), 'user', ['sem'], unique=False)
    op.create_index(op.f('ix_user_usn'), 'user', ['usn'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_usn'), table_name='user')
    op.drop_index(op.f('ix_user_sem'), table_name='user')
    op.drop_index(op.f('ix_user_interets'), table_name='user')
    op.drop_index(op.f('ix_user_cgpa'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_elective_teacher'), table_name='elective')
    op.drop_index(op.f('ix_elective_specialization'), table_name='elective')
    op.drop_index(op.f('ix_elective_prerequisites'), table_name='elective')
    op.drop_index(op.f('ix_elective_description'), table_name='elective')
    op.drop_index(op.f('ix_elective_courseName'), table_name='elective')
    op.drop_table('elective')
    # ### end Alembic commands ###
