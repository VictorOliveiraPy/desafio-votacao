"""create_associate_agenda_vote_table

Revision ID: 39727fde959f
Revises: 
Create Date: 2023-06-05 23:21:56.512959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "39727fde959f"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "associates",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "agendas",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("associate_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["associate_id"],
            ["associates.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "votes",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("associate_id", sa.Integer(), nullable=True),
        sa.Column("agenda_id", sa.Integer(), nullable=True),
        sa.Column("vote", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["associate_id"],
            ["associates.id"],
        ),
        sa.ForeignKeyConstraint(
            ["agenda_id"],
            ["agendas.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("votes")
    op.drop_table("agendas")
    op.drop_table("associates")
