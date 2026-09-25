from fastapi import APIRouter, Depends
from src.tasks import controller
from src.tasks.dtos import TaskSchema
from src.utils.db import get_db

task_routes = APIRouter(prefix="/task")


@task_routes.post("/create")
def create_task(data:TaskSchema, db  = Depends(get_db)):
    return controller.create_task(data, db)

@task_routes.get("/all_tasks")
def get_all_task(db = Depends(get_db)):
    return controller.get_task(db)

@task_routes.get("/one_task/{task_id}")
def get_one_task(task_id:int, db = Depends(get_db)):
    return controller.get_one_task(db,task_id)