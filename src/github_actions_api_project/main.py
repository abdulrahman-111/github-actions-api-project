from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

    app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str


class Task(TaskCreate):
    id: int
    completed: bool = False


tasks: list[Task] = []
next_id = 1


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    global next_id

    new_task = Task(
        id=next_id,
        title=task.title,
        completed=False,
    )

    tasks.append(new_task)
    next_id += 1

    return new_task


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")