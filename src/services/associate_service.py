from sqlalchemy.orm import Session

from src.repository.sqlalchemy.associate_repository import AssociateRepository


class AssociateService:
    def __init__(self):
        self.associate_repository = AssociateRepository()

    def create_associate(self, name, db: Session):
        try:
            associate = self.associate_repository.create_associate(name, db)
            return associate
        except Exception as exception:
            raise exception
