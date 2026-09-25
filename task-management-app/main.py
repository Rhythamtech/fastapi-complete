from src.utils.db import Base, engine
from fastapi import FastAPI
from src.tasks.router import task_routes

Base.metadata.create_all(engine)
app = FastAPI(title= "Task management App")

app.include_router(task_routes)