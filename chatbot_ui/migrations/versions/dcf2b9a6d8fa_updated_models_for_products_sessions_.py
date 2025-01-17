"""Updated models for products, sessions, and chat logs

Revision ID: dcf2b9a6d8fa
Revises: 
Create Date: 2024-12-26 11:53:27.797882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcf2b9a6d8fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sessions',
    sa.Column('session_id', sa.String(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('session_id')
    )
    op.create_table('chat_logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('session_id', sa.String(), nullable=True),
    sa.Column('message', sa.Text(), nullable=False),
    sa.Column('sender', sa.String(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['session_id'], ['sessions.session_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('chat_logs')
    op.drop_table('sessions')
    # ### end Alembic commands ###
