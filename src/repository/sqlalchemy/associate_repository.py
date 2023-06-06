from src.repository.sqlalchemy.models.associate import Associate
from src.exceptions.exception import AssociateCreationError


class AssociateRepository:
    def create_associate(self, name: str, session) -> Associate:
        try:
            associate = Associate(name=name)
            session.add(associate)
            session.commit()
            return associate
        except Exception as exception:
            session.rollback()
            raise AssociateCreationError("Failed to create associate") from exception
