from pydantic import BaseModel, Field


class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=80)
    content: str = Field(..., min_length=1, max_length=400)
    category: str = Field(default="general", min_length=1, max_length=30)


class Note(BaseModel):
    id: int
    title: str
    content: str
    category: str


class HealthResponse(BaseModel):
    status: str
    version: str
