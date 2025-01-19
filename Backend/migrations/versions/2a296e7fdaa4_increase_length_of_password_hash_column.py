"""Increase length of password_hash column

Revision ID: 2a296e7fdaa4
Revises: 07651735695c
Create Date: 2024-12-25 23:24:15.454124
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2a296e7fdaa4'
down_revision = '07651735695c'
branch_labels = None
depends_on = None


def upgrade():
    # Alter the length of the password_hash column
    op.alter_column('users', 'password_hash',
                    type_=sa.String(256),  # New length for the column
                    existing_type=sa.String(128),
                    existing_nullable=False)


def downgrade():
    # Revert the length of the password_hash column to the previous size
    op.alter_column('users', 'password_hash',
                    type_=sa.String(128),  # Reverting back to 128
                    existing_type=sa.String(256),
                    existing_nullable=False)
