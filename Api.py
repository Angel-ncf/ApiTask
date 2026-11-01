from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from DataBase.BD import db_connection
from DataBase.models.models import Task, TaskResponse
from DataBase.schemas.schema import task_schema

app = FastAPI()

tasks = db_connection.local.tasks

@app.post("/task/")
async def create_task(item: Task) -> TaskResponse:
    result = tasks.insert_one(item.model_dump())
    saved_task = tasks.find_one({"_id": result.inserted_id})
    if saved_task is None:
        raise HTTPException(status_code=500, detail="No se pudo recuperar la tarea creada")
    return task_schema(saved_task)

@app.get("/task/{name}")
async def get_task(name: str) -> TaskResponse:
    task = tasks.find_one({"name": name})
    if task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task_schema(task)

@app.put("/task/{name}")
async def update_task(name: str, item: Task) -> TaskResponse:
    result = tasks.replace_one({"name": name}, item.model_dump())
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    updated_task = tasks.find_one({"name": item.name})
    if updated_task is None:
        raise HTTPException(status_code=500, detail="No se pudo recuperar la tarea actualizada")
    return task_schema(updated_task)

@app.delete("/task/{name}")
async def delete_task(name: str):
    result = tasks.delete_one({"name": name})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"message": f"Task '{name}' deleted successfully"}

@app.get("/tasks/")
async def get_all_tasks() -> list[TaskResponse]:
    return [task_schema(task) for task in tasks.find()]