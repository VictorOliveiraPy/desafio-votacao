from pydantic import BaseModel


class AssociateCreateInput(BaseModel):
    name: str
