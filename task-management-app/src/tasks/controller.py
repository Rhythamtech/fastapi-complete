from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from src.user.models import UserModel
from fastapi import HTTPException

def create_task(data:TaskSchema, db : Session, user : UserModel):
    data = data.model_dump()
    new_task  = TaskModel(title = data["title"],
                        description = data["description"],
                        is_completed = data["is_completed"],
                        user_id = user.id )
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return new_task
    
    
def get_task(db:Session, user : UserModel):
    tasks = db.query(TaskModel).filter(TaskModel.user_id == user.id).all()
    
    return tasks
    
    
def get_one_task(db:Session, task_id: int, user: UserModel):
    one_task = db.query(TaskModel).get(task_id)

    if not one_task:
        raise HTTPException(404, "Task ID is incorrect.")

    if one_task.user_id != user.id:
        raise HTTPException(401, "You are not authorized to view this task.")

    return one_task


def update_task(body:TaskSchema, task_id : int, db:Session, user : UserModel):

    one_task = db.query(TaskModel).get(task_id)
        
    if not one_task:
        raise HTTPException(404, "Task ID is incorrect.")
    
    if one_task.user_id != user.id:
        raise HTTPException(401, "You are not authorize to update Task.")
    
    # one_task.title = body.title
    # one_task.description = body.description
    # one_task.is_completed = body.is_completed
    
    data =  body.model_dump()
    
    for field, value in data.items():
        setattr(one_task,field,value)
    
    db.add(one_task)
    db.commit()
    db.refresh(one_task)
    
    return one_task
    
def delete_task(task_id : int, db:Session, user : UserModel):
    one_task = db.query(TaskModel).get(task_id)
        
    if not one_task:
        raise HTTPException(404, "Task ID is incorrect.")
    
    if one_task.user_id != user.id:
            raise HTTPException(401, "You are not authorize to Delete Task.")
        
    db.delete(one_task)
    db.commit()
    
    return None