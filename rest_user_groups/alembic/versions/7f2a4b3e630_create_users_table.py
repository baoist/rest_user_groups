"""create users table

Revision ID: 7f2a4b3e630
Revises: fc1bcc255a4
Create Date: 2015-12-08 21:59:19.187249

"""

# revision identifiers, used by Alembic.
revision = '7f2a4b3e630'
down_revision = 'fc1bcc255a4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(50), nullable=False),
        sa.Column('last_name', sa.String(50), nullable=False),
        sa.Column('userid', sa.String(50), nullable=False, unique=True),
        sa.Column('group_id', sa.Integer, sa.ForeignKey('groups.id')),
    )


def downgrade():
    op.drop_table('users')
