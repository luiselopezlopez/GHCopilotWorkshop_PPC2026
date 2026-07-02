# Setup

## Prerequisitos locales

- Python 3.11 o superior
- VS Code con GitHub Copilot y GitHub Copilot Chat
- Navegador web

## Prerequisitos de extensiones

- GitHub Copilot
- GitHub Copilot Chat
- Python

## Comandos de preparacion

Ejecuta exactamente estos comandos desde la raiz del repo:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
python -m compileall backend
pytest backend\tests\test_notes_page.py
```

La ultima orden debe fallar al inicio del workshop. Ese fallo es intencional y se usa en el Laboratorio 1.

Si quieres reproducir el error de arranque de forma manual:

```powershell
uvicorn app.main:app --app-dir backend --reload
```

## Checklist previa

1. Clona o abre este repo en VS Code.
2. Crea un entorno virtual y instala `backend/requirements.txt`.
3. Comprueba que `python -m compileall backend` funciona.
4. Comprueba que `uvicorn app.main:app --app-dir backend --reload` actualmente falla al arrancar.
5. Guarda el error porque se usara en el Laboratorio 1.

## Variables de entorno

### Aplicacion

Copia `backend/.env.example` y define:

- `NOTES_APP_TITLE`: titulo visible de la aplicacion.

## Validaciones minimas antes de empezar la sesion

### Validacion del starter defectuoso

```powershell
python -m compileall backend
pytest backend\tests\test_notes_page.py
```

## Fallback del instructor

Si algun alumno se atasca en el Laboratorio 1, el instructor debe tener preparado:

- una copia del traceback de arranque,
- la explicacion precisa de la causa raiz,
- el diff minimo que corrige el problema.
