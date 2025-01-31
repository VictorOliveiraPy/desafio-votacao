
from src.repository.sqlalchemy.models.associate import Associate

from src.exceptions.exception import AssociateCreationError, AssociateNotFoundError


class AssociateRepository:
    def create_associate(self, name: str, session) -> Associate:
        try:
            associate = Associate()
            associate.name = name
            session.add(associate)
            session.commit()
            return associate
        except Exception as exception:
            session.rollback()
            raise AssociateCreationError("Failed to create associate") from exception

    def get_associate(self, associate_id: int, session) -> Associate:
        associate = session.query(Associate).filter_by(id=associate_id).first()
        if not associate:
            return None
        return associate

