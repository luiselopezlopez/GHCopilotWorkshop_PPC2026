# Lab 1 Solution Reference

## Problema

La app falla durante el startup porque `NoteService.load_initial_notes()` trata el payload JSON completo como si fuera una lista de notas, cuando en realidad es un diccionario con una clave `notes`.

## Sintoma visible

Traceback esperado:

```text
TypeError: app.schemas.Note() argument after ** must be a mapping, not str
```

## Archivo afectado

- `backend/app/services/note_service.py`

## Arreglo minimo esperado

Sustituir este bloque:

```python
for item in payload:
    note = Note(**item)
```

Por este:

```python
for item in payload["notes"]:
    note = Note(**item)
```

## Validacion

```powershell
pytest backend\tests\test_notes_page.py
```

## Validacion adicional opcional

```powershell
uvicorn app.main:app --app-dir backend --reload
```
