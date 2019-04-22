"""stocks table

Revision ID: aeee2aa4ad8f
Revises: 
Create Date: 2019-04-21 16:27:53.284552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aeee2aa4ad8f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stocks',
                    sa.Column('isin', sa.String(), nullable=False),
                    sa.Column('name', sa.String(), nullable=True),
                    sa.Column('symbol', sa.String(), nullable=True),
                    sa.Column('currency', sa.String(), nullable=True),
                    sa.Column('sector', sa.String(), nullable=True),
                    sa.Column('yahoo_ticker', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('isin')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stocks')
    # ### end Alembic commands ###
