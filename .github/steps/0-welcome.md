# GitHub Copilot Workshop — PPC 2026

_Aprende a usar GitHub Copilot con ejercicios prácticos y guiados._

## Bienvenido

Tu entorno está listo. En este workshop de **2 horas** completarás **8 ejercicios** usando GitHub Copilot sobre una app real de notas con un bug de arranque y una evolución de feature pendiente.

## Configurar el entorno

Abre este repositorio en un **Codespace** (botón verde **Code → Codespaces → New codespace**) o clónalo localmente con VS Code.

Una vez dentro, ejecuta en terminal:

```bash
python -m venv .venv
source .venv/bin/activate          # Linux/macOS
# .venv\Scripts\Activate.ps1       # Windows PowerShell
pip install -r backend/requirements.txt
```

---

## Ejercicio 1: Onboard del codebase con Agent

### Objetivo

Entender la arquitectura de la app antes de tocar nada.

### Instrucciones

Abre Copilot Chat en modo **Agent** y pega:

```
/init onboard the code on the backend folder, which is where the application code lives. Ignore the folders deck, docs and resources. Also ignore any .md file you find in the repo as they are not related with the codebase
```

### Validación

Responde mentalmente (o por escrito) estas preguntas antes de continuar:

- ¿Cuál es la arquitectura general de la app?
- ¿Qué hace cada capa principal (`routes`, `services`, `schemas`)?
- ¿Qué archivos son más sensibles al arranque?

---

## Ejercicio 2: Diagnosticar el bug con Ask

### Objetivo

Reproducir el fallo de arranque y usar Copilot para identificar la causa raíz.

### Reproducir el problema

```bash
uvicorn app.main:app --app-dir backend --reload
```

La app debe **fallar al arrancar**. Copia el traceback completo.

### Instrucciones

Cambia a modo **Ask** y pega (sustituyendo el traceback real):

```
La aplicacion falla al arrancar. Este es el error que estoy viendo en terminal:

[pega aqui el traceback completo o al menos las ultimas lineas]

Lee el codigo relevante y dime:
1. cual es la causa raiz exacta,
2. en que archivo esta,
3. por que rompe el startup,
4. cual seria la correccion minima razonable.
```

### Validación

Antes de continuar, verifica que puedes responder:

- ¿Cuál es la causa raíz exacta?
- ¿En qué archivo está?
- ¿Cuál es la corrección mínima?

---

## Ejercicio 3: Acotar el alcance con Plan

### Objetivo

Generar un plan pequeño y verificable antes de implementar.

### Instrucciones

Cambia a modo **Plan** y pega:

```
Genera un plan minimo para corregir el bug de arranque de la app con estas restricciones:
- no reestructures toda la aplicacion,
- corrige solo la causa raiz,
- mantén la app monolitica y local,
- el cambio debe ser pequeno y facil de explicar en una sesion en vivo,
- incluye una unica validacion final con pytest backend/tests/test_notes_page.py.

No implementes todavia. Solo quiero pasos concretos.
```

### Validación

Revisa que el plan cumple estos criterios antes de continuar:

- [ ] Toca pocos archivos
- [ ] No introduce refactors grandes
- [ ] Corrige solo la causa raíz
- [ ] Termina con un test único y estrecho

Si el plan es demasiado grande, acótalo con:

```
Reduce el plan al slice mas pequeno posible. Prefiero corregir solo el bug de startup y validar con un unico test, sin refactorizar toda la arquitectura.
```

---

## Ejercicio 4: Implementar y validar con Agent

### Objetivo

Ejecutar el plan acordado y confirmar que la app arranca y los tests pasan.

### Instrucciones

Cambia a modo **Agent** y pega:

```
Implementa el plan acordado sobre el backend.

Objetivo concreto:
- corrige el bug que impide arrancar la aplicacion,
- no conviertas esto en un refactor amplio,
- conserva el comportamiento de app local de notas,
- si tocas el servicio de notas, manten el cambio corto y explicable,
- valida al final con pytest backend/tests/test_notes_page.py.
```

Si Agent se va de alcance, usa este prompt para redirigirlo:

```
Deten el refactor amplio. Limita el cambio a backend/app/services/note_service.py. Corrige solo el bug de arranque y valida con pytest backend/tests/test_notes_page.py.
```

### Validación

```bash
pytest backend/tests/
```

Todos los tests deben pasar. Opcionalmente, confirma que la app ya arranca:

```bash
uvicorn app.main:app --app-dir backend --reload
```

### Crear el PR de validación

Cuando los tests pasen:

1. Crea una rama desde `main`:
   ```bash
   git checkout -b ejercicio-4/fix-startup-bug
   git add backend/app/services/note_service.py
   git commit -m "fix: correct note loading in NoteService.load_initial_notes"
   git push origin ejercicio-4/fix-startup-bug
   ```

2. Abre un **Pull Request** de `ejercicio-4/fix-startup-bug` → `main`.

3. Espera a que GitHub Actions valide tu PR (~1 minuto). Si pasa, **fusiona el PR** para desbloquear los ejercicios 5–8.

---

¿Tienes dudas? Consulta [`docs/EJERCICIOS_1_4_MODOS_COPILOT.md`](docs/EJERCICIOS_1_4_MODOS_COPILOT.md) o [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md).
