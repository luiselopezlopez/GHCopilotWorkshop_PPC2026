# Troubleshooting

## Backend no arranca

- Comprueba el entorno virtual.
- Reinstala `backend/requirements.txt`.
- Ejecuta `python -m compileall backend`.
- Revisa el traceback de `uvicorn app.main:app --app-dir backend --reload`.

## El test de la pagina principal falla

- Revisa `backend/app/main.py`, `backend/app/routes/notes.py` y `backend/app/services/note_service.py`.
- Comprueba que el servicio pueda cargar las notas iniciales.
- Revisa que la plantilla `backend/app/templates/notes.html` exista.

## El formulario no crea notas

- Comprueba que `python-multipart` este instalado.
- Revisa la ruta `POST /notes`.
- Comprueba que el redirect vuelve a `/`.

## Customizaciones no se disparan

- Revisa el `description`.
- Revisa `applyTo` en las instructions.
- Asegurate de que el fichero esta en la carpeta correcta dentro de `.github/`.
- Si acabas de empezar el laboratorio 2, comprueba primero que los archivos hayan sido copiados desde `resources/` a `.github/`.
