#modelo de datos de la base de datos de mongo db

from pydantic import BaseModel

class Task(BaseModel):
    name: str
    description: str
    hour: str

class TaskResponse(Task):
    id: str
