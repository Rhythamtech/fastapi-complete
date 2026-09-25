from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel

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
    