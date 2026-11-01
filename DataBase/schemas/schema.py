def task_schema(task) -> dict:
    return {
        "id": str(task["_id"]),
        "name": str(task["name"]),
        "description": str(task["description"]),
        "hour": str(task["hour"]),
    }
