from contextlib import asynccontextmanager

from fastapi import FastAPI

from routes import router
from services import get_generator


@asynccontextmanager
async def lifespan(app: FastAPI):
    get_generator()
    yield


app = FastAPI(title="GPT-2 Text Generation API", version="1.0.0", lifespan=lifespan)

app.include_router(router)
