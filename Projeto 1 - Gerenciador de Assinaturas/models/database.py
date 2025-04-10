from sqlmodel import SQLModel, Field, create_engine
from .model import *

sqlite_file_name = "database.db"
sqlite_url = "sqlite:///./database.db"
engine = create_engine(sqlite_url, echo=False)
SQLModel.metadata.create_all(engine)