from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import settings

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class SessionMakerWrapper(object):
    session: Session = None

    def __init__(self) -> None:
        self.session: Session = SessionLocal()

    def __enter__(self):
        return self.session

    def __exit__(self, type, value, traceback):
        self.session.close()