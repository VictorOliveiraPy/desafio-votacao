"""adding updated at and created_at 

Revision ID: 13b8e371b9eb
Revises: 39727fde959f
Create Date: 2023-06-05 23:33:12.177489

"""
from alembic import op
import sqlalchemy as sa
import datetime


# revision identifiers, used by Alembic.
revision = "13b8e371b9eb"
down_revision = "39727fde959f"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "associates",
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            default=datetime.datetime.utcnow,
        ),
    )
    op.add_column(
        "associates",
        sa.Column(
            "updated_at",
            sa.DateTime(),
            nullable=False,
            default=datetime.datetime.utcnow,
            onupdate=datetime.datetime.utcnow,
        ),
    )

    op.add_column(
        "agendas",
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            default=datetime.datetime.utcnow,
        ),
    )
    op.add_column(
        "agendas",
        sa.Column(
            "updated_at",
            sa.DateTime(),
            nullable=False,
            default=datetime.datetime.utcnow,
            onupdate=datetime.datetime.utcnow,
        ),
    )

    op.add_column(
        "votes",
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            default=datetime.datetime.utcnow,
        ),
    )
    op.add_column(
        "votes",
        sa.Column(
            "updated_at",
            sa.DateTime(),
            nullable=False,
            default=datetime.datetime.utcnow,
            onupdate=datetime.datetime.utcnow,
        ),
    )


def downgrade() -> None:
    op.drop_column("vote", "updated_at")
    op.drop_column("vote", "created_at")

    op.drop_column("agenda", "updated_at")
    op.drop_column("agenda", "created_at")

    op.drop_column("associates", "updated_at")
    op.drop_column("associates", "created_at")
