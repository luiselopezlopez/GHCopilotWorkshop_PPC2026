import json

from app.schemas import Note, NoteCreate

SEED_NOTES_JSON = """
{
  "notes": [
    {
      "id": 1,
      "title": "Preparar agenda del workshop",
      "content": "Definir tiempos de labs y checkpoints del docente.",
      "category": "workshop"
    },
    {
      "id": 2,
      "title": "Revisar demo local",
      "content": "Comprobar que la aplicacion arranca y que se pueden crear notas.",
      "category": "demo"
    }
  ]
}
"""


class NoteService:
    def __init__(self) -> None:
        self._notes: list[Note] = []
        self._next_id = 1

    def load_initial_notes(self) -> None:
        if self._notes:
            return

        payload = json.loads(SEED_NOTES_JSON)

        # Workshop bug: payload is a dict with a "notes" key, but the code
        # below treats it as if it were already a list of note dictionaries.
        for item in payload:
            note = Note(**item)
            self._notes.append(note)
            self._next_id = max(self._next_id, note.id + 1)

    def list_notes(self, query: str = "", category: str = "all") -> list[Note]:
        filtered = self._notes

        if category != "all":
            filtered = [note for note in filtered if note.category == category]

        if query:
            normalized_query = query.lower()
            filtered = [
                note
                for note in filtered
                if normalized_query in note.title.lower()
                or normalized_query in note.content.lower()
            ]

        return filtered

    def available_categories(self) -> list[str]:
        categories = sorted({note.category for note in self._notes})
        return ["all", *categories]

    def add_note(self, note: NoteCreate) -> Note:
        created_note = Note(
            id=self._next_id,
            title=note.title,
            content=note.content,
            category=note.category,
        )
        self._notes.append(created_note)
        self._next_id += 1
        return created_note


note_service = NoteService()


def get_note_service() -> NoteService:
    return note_service
