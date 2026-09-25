from src.utils.db import Base, engine
from fastapi import FastAPI
from src.tasks.models import TaskModel


Base.metadata.create_all(engine)
app = FastAPI(title= "Task management App")
