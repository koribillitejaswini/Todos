from fastapi import FastAPI, Request, status
from .models import Base
from .database import engine
from .routers import auth, todos, admin, user
# from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()

Base.metadata.create_all(bind = engine)

# templates = Jinja2Templates(directory = "TODOApp/templates")

app.mount("/static",StaticFiles(directory = "TODOApp/static"), name = "static")

@app.get("/")
def test(request: Request):
    return RedirectResponse(url = "/todos/todo-page", status_code = status.HTTP_302_FOUND)

@app.get("/healthy")
async def health_check():
    return {"Status": "Healthy"}

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(user.router)