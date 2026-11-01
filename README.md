# Mini API de Tareas

API REST para gestionar tareas (crear, consultar, actualizar y eliminar), hecha con FastAPI y MongoDB.

## Tecnologías

- Python 3.10+
- FastAPI
- Pydantic v2
- PyMongo
- MongoDB Community Server

## Requisitos

- [Python](https://www.python.org/downloads/) 3.10 o superior
- [MongoDB Community Server](https://www.mongodb.com/try/download/community) corriendo en local (`mongodb://localhost:27017`)

## Instalación

```powershell
git clone <URL-DEL-REPOSITORIO>
cd Mini_Api_Proyecto

python -m venv venv
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

## Ejecución

Asegúrate de que el servicio de MongoDB esté activo y luego corre:

```powershell
uvicorn main:app --reload
```

- API: http://127.0.0.1:8000
- Documentación interactiva (Swagger): http://127.0.0.1:8000/docs

## Endpoints

> Ajusta esta tabla para que coincida con las rutas reales de tu `main.py`.

| Método | Ruta          | Descripción                  |
|--------|---------------|------------------------------|
| POST   | `/tasks`      | Crear una tarea              |
| GET    | `/tasks`      | Listar todas las tareas      |
| GET    | `/tasks/{id}` | Obtener una tarea por su id  |
| PUT    | `/tasks/{id}` | Actualizar una tarea         |
| DELETE | `/tasks/{id}` | Eliminar una tarea           |

## Ejemplo de uso

Crear una tarea (`POST /tasks`):

```json
{
  "name": "Estudiar FastAPI",
  "description": "Repasar path parameters y Pydantic",
  "hour": "18:00"
}
```

Respuesta:

```json
{
  "id": "6720f1c2a1b2c3d4e5f67890",
  "name": "Estudiar FastAPI",
  "description": "Repasar path parameters y Pydantic",
  "hour": "18:00"
}
```

## Estructura del proyecto

```
Mini_Api_Proyecto/
├── main.py          # Endpoints
├── DataBase/
│   ├── BD.py        # Conexión a MongoDB
│   ├── models/      # Modelos de Pydantic
│   └── schemas/     # Conversión de documentos de MongoDB a JSON
├── requirements.txt
└── README.md
```

## Próximos pasos

- Agregar autenticación con JWT
- Agregar un campo para marcar tareas como completadas
- Empaquetar con Docker
