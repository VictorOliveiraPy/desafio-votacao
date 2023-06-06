from pydantic import BaseModel


class AgendaCreateInput(BaseModel):
    title: str
    description: str
