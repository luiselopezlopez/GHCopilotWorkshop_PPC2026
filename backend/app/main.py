from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.routes.notes import router as notes_router
from app.services.note_service import get_note_service


@asynccontextmanager
async def lifespan(_: FastAPI):
    get_note_service().load_initial_notes()
    yield

app = FastAPI(
    title="Workshop Notes",
    description="Small monolithic notes app used in the GitHub Copilot workshop.",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "healthy", "version": "0.1.0"}


app.include_router(notes_router)
