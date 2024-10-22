"""modules"""
from fastapi import FastAPI
from pydantic import BaseModel

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
