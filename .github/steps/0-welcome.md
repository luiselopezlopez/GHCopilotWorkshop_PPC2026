# GitHub Copilot Workshop — PPC 2026

_Aprende a usar GitHub Copilot con ejercicios prácticos y guiados._

## Bienvenido

Tu entorno está listo. En este workshop de **2 horas** usarás GitHub Copilot para:

1. **Lab 1**: Diagnosticar y corregir un bug real usando Ask, Plan y Agent.
2. **Lab 2**: Preparar customizaciones de Copilot para añadir una nueva feature.

## Configurar el entorno

Abre este repositorio en un **Codespace** (botón verde **Code → Codespaces → New codespace**) o clónalo localmente con VS Code.

Una vez dentro, ejecuta en terminal:

```bash
python -m venv .venv
source .venv/bin/activate          # Linux/macOS
# .venv\Scripts\Activate.ps1       # Windows PowerShell
pip install -r backend/requirements.txt
```

## Lab 1: Ask, Plan y Agent

### Objetivo

Usar GitHub Copilot para hacer onboard de la app y corregir el bug que impide que arranque.

### Reproducir el problema

```bash
uvicorn app.main:app --app-dir backend --reload
```

La app debe **fallar al arrancar**. Copia el traceback completo: lo usarás en la conversación con Copilot.

### Flujo recomendado

Sigue esta secuencia en orden:

#### Paso 1 — Onboard con Agent

Abre Copilot Chat en modo **Agent** y pega:

```
/init onboard the code on the backend folder, which is where the application code lives. Ignore the folders deck, docs and resources. Also ignore any .md file you find in the repo as they are not related with the codebase
```

#### Paso 2 — Diagnosticar con Ask

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

#### Paso 3 — Acotar con Plan

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

#### Paso 4 — Implementar con Agent

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

#### Paso 5 — Validar

```bash
pytest backend/tests/
```

Todos los tests deben pasar.

### Criterio de éxito

1. Puedes explicar la arquitectura general de la app.
2. Tienes un plan pequeño y concreto.
3. La app arranca sin errores.
4. `pytest backend/tests/` termina correctamente.

## Crear el PR del Lab 1

Cuando los tests pasen:

1. Crea una rama desde `main`:
   ```bash
   git checkout -b lab1/fix-startup-bug
   git add backend/app/services/note_service.py
   git commit -m "fix: correct note loading in NoteService.load_initial_notes"
   git push origin lab1/fix-startup-bug
   ```

2. Abre un **Pull Request** de `lab1/fix-startup-bug` → `main`.

3. Espera a que GitHub Actions valide tu PR (~1 minuto). Si pasa, **fusiona el PR** para desbloquear el Lab 2.

---

¿Tienes dudas? Consulta [`docs/LAB1_ASK_PLAN_AGENT.md`](docs/LAB1_ASK_PLAN_AGENT.md) o [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md).
