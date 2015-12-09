"""create groups table

Revision ID: fc1bcc255a4
Revises: None
Create Date: 2015-12-08 21:59:12.632870

"""

# revision identifiers, used by Alembic.
revision = 'fc1bcc255a4'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'groups',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
    )


def downgrade():
    op.drop_table('groups')
