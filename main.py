"""modules"""
from fastapi import FastAPI
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

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    """get_tasks endpoint"""
    return tasks
