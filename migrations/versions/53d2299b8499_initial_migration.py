from alembic import op
import sqlalchemy as sa

"""
Migração inicial - Criação das tabelas Associate, Agenda e Vote
"""


# Identificador da revisão
revision = 'initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('associates',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_table('agendas',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(), nullable=True),
                    sa.Column('description', sa.String(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_table('votes',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('associate_id', sa.Integer(), nullable=True),
                    sa.Column('agenda_id', sa.Integer(), nullable=True),
                    sa.Column('vote', sa.String(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.ForeignKeyConstraint(['agenda_id'], ['agendas.id'], ),
                    sa.ForeignKeyConstraint(['associate_id'], ['associates.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('votes')
    op.drop_table('agendas')
    op.drop_table('associates')
