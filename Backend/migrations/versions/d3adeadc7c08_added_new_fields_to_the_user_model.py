"""Added new fields to the User model

Revision ID: d3adeadc7c08
Revises: df68bc956c38
Create Date: 2024-12-25 00:57:31.023659

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd3adeadc7c08'
down_revision = 'df68bc956c38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('first_name', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('last_name', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('date_of_birth', sa.Date(), nullable=True))
        batch_op.add_column(sa.Column('gender', sa.String(length=10), nullable=False))
        batch_op.add_column(sa.Column('weight', sa.Float(), nullable=False))
        batch_op.add_column(sa.Column('height', sa.Float(), nullable=False))
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(length=120),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(length=80),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('password_hash',
               existing_type=mysql.VARCHAR(length=512),
               type_=sa.String(length=128),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=128),
               type_=mysql.VARCHAR(length=512),
               nullable=True)
        batch_op.alter_column('username',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=80),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=120),
               existing_nullable=False)
        batch_op.drop_column('height')
        batch_op.drop_column('weight')
        batch_op.drop_column('gender')
        batch_op.drop_column('date_of_birth')
        batch_op.drop_column('last_name')
        batch_op.drop_column('first_name')

    # ### end Alembic commands ###
