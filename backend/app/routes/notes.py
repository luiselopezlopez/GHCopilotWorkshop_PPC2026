from pathlib import Path

from fastapi import APIRouter, Depends, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.schemas import NoteCreate
from app.services.note_service import NoteService, get_note_service

router = APIRouter(tags=["notes"])
templates = Jinja2Templates(directory=str(Path(__file__).resolve().parent.parent / "templates"))


@router.get("/", response_class=HTMLResponse)
async def notes_home(
    request: Request,
    q: str = "",
    category: str = "all",
    note_service: NoteService = Depends(get_note_service),
) -> HTMLResponse:
    notes = note_service.list_notes(query=q, category=category)
    return templates.TemplateResponse(
        request,
        "notes.html",
        {
            "request": request,
            "notes": notes,
            "query": q,
            "category": category,
            "categories": note_service.available_categories(),
            "page_title": "Workshop Notes",
        },
    )


@router.post("/notes")
async def create_note(
    title: str = Form(...),
    content: str = Form(...),
    category: str = Form("general"),
    note_service: NoteService = Depends(get_note_service),
) -> RedirectResponse:
    note_service.add_note(
        NoteCreate(
            title=title,
            content=content,
            category=category,
        )
    )
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
