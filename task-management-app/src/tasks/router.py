from fastapi import APIRouter, Depends, status
from src.tasks import controller
from src.tasks.dtos import TaskSchema, TaskResponseSchema
from src.utils.db import get_db
from sqlalchemy.orm import Session
from src.utils.helper import is_authenticated
from src.user.models import UserModel
from typing import List

task_routes = APIRouter(prefix="/task")


@task_routes.post("/create", response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED)
def create_task(data:TaskSchema, db : Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return controller.create_task(data, db)

@task_routes.get("/all_tasks",response_model=List[TaskResponseSchema] ,status_code=status.HTTP_200_OK)
def get_all_task(db : Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return controller.get_task(db)

@task_routes.get("/one_task/{task_id}", response_model=TaskResponseSchema, status_code= status.HTTP_200_OK)
def get_one_task(task_id:int, db : Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return controller.get_one_task(db,task_id)

@task_routes.put("/update_task/{task_id}",response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED)
def update_task(body : TaskSchema, task_id:int,db : Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return controller.update_task(body,task_id,db)

@task_routes.delete("/delete_task/{task_id}",response_model=None, status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int,db : Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return controller.update_task(task_id,db)