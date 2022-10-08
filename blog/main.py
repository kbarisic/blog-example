import uvicorn
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import user, blog, auth

app = FastAPI()


models.Base.metadata.create_all(engine)


app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=9000)
