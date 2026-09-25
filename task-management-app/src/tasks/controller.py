from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException

def create_task(data:TaskSchema, db : Session):
    data = data.model_dump()
    new_task  = TaskModel(title = data["title"],
                        description = data["description"],
                        is_completed = data["is_completed"])
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return {
        "status" :"task created successfully..",
        "data" : new_task
    }
    
    
def get_task(db:Session):
    tasks = db.query(TaskModel).all()
    
    return {
        "status" : "All Tasks data",
        "data":tasks
    }
    
    
def get_one_task(db:Session , task_id: int):
    one_task = db.query(TaskModel).get(task_id)
    
    if not one_task:
        raise HTTPException(404, "Task ID is incorrect.")
    
    return {"status": "Task fetched successfully.", "data":one_task}