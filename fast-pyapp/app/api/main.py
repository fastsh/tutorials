from fastapi import FastAPI

from api.routers.v1 import users as users_v1
from api.routers.v1 import default 

app = FastAPI(title="Main API",)

app.include_router(default.router, prefix='/v1', tags=['default'])
app.include_router(users_v1.router, prefix='/v1', tags=['users'])
