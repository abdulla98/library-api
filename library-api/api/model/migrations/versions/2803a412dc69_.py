"""empty message

Revision ID: 2803a412dc69
Revises: 
Create Date: 2020-06-09 22:38:47.554009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2803a412dc69'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('author_id')
    )
    op.create_table('student',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('birthdate', sa.String(length=50), nullable=False),
    sa.Column('gender', sa.String(length=10), nullable=False),
    sa.Column('student_class', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('student_id')
    )
    op.create_table('book',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('pagecount', sa.Integer(), nullable=True),
    sa.Column('book_authorId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_authorId'], ['author.author_id'], ),
    sa.PrimaryKeyConstraint('book_id')
    )
    op.create_table('borrow',
    sa.Column('borrow_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('taken_date', sa.String(length=50), nullable=False),
    sa.Column('brought_date', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.book_id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.student_id'], ),
    sa.PrimaryKeyConstraint('borrow_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('borrow')
    op.drop_table('book')
    op.drop_table('student')
    op.drop_table('author')
    # ### end Alembic commands ###
