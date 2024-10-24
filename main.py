"""modules"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

tasks = []

class Task(BaseModel):
    """Task Object inheriting from BaseModel"""
    title: str
    description: str = ""

@app.post("/tasks/")
def create_task(task: Task):
    """create_task endpoint"""
    tasks.append(task)
    return {"Message": "Task added successfully!"}

@app.get("/tasks/", response_model=List[Task])
def get_tasks():
    """get_tasks endpoint"""
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if 0 <= task_id < len(tasks):
        return tasks[task_id]
    else:
        raise HTTPException(status_code=404, detail="Task: Not found!")

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    if 0 <= task_id < len(tasks):
        tasks[task_id] = updated_task
        return updated_task
    else:
        raise HTTPException(status_code=404, detail="Task: Not found!")

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    if 0 <= task_id < len(tasks):
        deleted_task = tasks.pop(task_id)
        return deleted_task
    else:
        raise HTTPException(status_code=404, detail="Task not found!")