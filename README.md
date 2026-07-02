# GitHub Copilot Hands-on Lab

Repositorio base para una sesion practica de 2 horas sobre GitHub Copilot.

## Objetivos

- Hacer onboard de un codebase local con GitHub Copilot.
- Usar Ask, Plan y Agent para diagnosticar y corregir un bug real.
- Entender y aplicar prompts, instructions, skills y agents para añadir una feature nueva con un estilo de desarrollo estandar.

## Estructura

- `backend/`: aplicacion web monolitica de notas con FastAPI y HTML renderizado en servidor.
- `resources/`: plantillas de prompt, instructions, skill y agent que el alumno movera durante el laboratorio 2.
- `docs/`: runbooks del alumno e instructor.
- `deck/`: guion de slides y demo.

## Flujo de la sesion

1. Preparar entorno y validar prerequisitos.
2. Hacer onboard del codebase y diagnosticar un bug de arranque con Ask.
3. Preparar un plan de correccion con Plan y ejecutarlo con Agent.
4. Mover a `.github/` y preparar customizaciones para añadir persistencia SQLite en archivo local.

## Arranque rapido

### Aplicacion web

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
uvicorn app.main:app --app-dir backend --reload
```

### Tests

```powershell
pytest backend\tests
```
