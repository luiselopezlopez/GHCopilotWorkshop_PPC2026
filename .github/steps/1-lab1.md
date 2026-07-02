## 🚀 Paso 0: Abrir el Codespace y crear tu rama de trabajo

**Antes de hacer cualquier otra cosa**, sigue estos pasos en orden.

1. Abre este repositorio en un Codespace:

   [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

2. Espera a que VS Code cargue en el navegador y las extensiones terminen de instalarse.

3. En el terminal integrado, crea y publica tu rama de trabajo:

   ```bash
   git checkout -b ejercicio-4/fix-startup-bug
   git push -u origin ejercicio-4/fix-startup-bug
   ```

4. Confirma que estás en la rama correcta:

   ```bash
   git branch --show-current
   # Resultado esperado: ejercicio-4/fix-startup-bug
   ```

5. Instala las dependencias del backend:

   ```bash
   python -m venv .venv
   # Linux/macOS:
   source .venv/bin/activate
   # Windows PowerShell:
   # .venv\Scripts\Activate.ps1
   pip install -r backend/requirements.txt
   ```

---

## Ejercicios 1–4: Ask, Plan y Agent

### Objetivo

Usar GitHub Copilot de forma guiada para:

1. hacer onboard de un codebase ya existente,
2. entender por qué la app no arranca,
3. generar un plan pequeño y verificable,
4. implementar la corrección con Agent,
5. validarla con un test estrecho.

El objetivo funcional es corregir el bug que impide el arranque de la aplicación web de notas.

---

## Ejercicio 1: Onboard del codebase con Agent

Abre Copilot Chat en modo **Agent** y pega:

```
/init onboard the code on the backend folder, which is where the application code lives. Ignore the folders deck, docs and resources. Also ignore any .md file you find in the repo as they are not related with the codebase
```

### Validación del ejercicio 1

Antes de continuar, responde mentalmente:

- ¿Cuál es la arquitectura general de la app?
- ¿Qué hace cada capa principal (`routes`, `services`, `schemas`)?
- ¿Qué archivos son más sensibles al arranque?

---

## Ejercicio 2: Diagnosticar el bug con Ask

Reproduce el fallo de arranque:

```bash
uvicorn app.main:app --app-dir backend --reload
```

La app debe **fallar al arrancar**. Copia el traceback completo.

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

### Validación del ejercicio 2

Antes de continuar, verifica que puedes identificar:

- La causa raíz exacta del bug
- El archivo y la línea donde se produce
- La corrección mínima necesaria

---

## Ejercicio 3: Acotar el alcance con Plan

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

Si el plan es demasiado grande, acótalo con:

```
Reduce el plan al slice mas pequeno posible. Prefiero corregir solo el bug de startup y validar con un unico test, sin refactorizar toda la arquitectura.
```

### Validación del ejercicio 3

- [ ] Tienes un plan de 3 pasos o menos
- [ ] Toca un solo archivo de producción
- [ ] Termina con un test único y estrecho

---

## Ejercicio 4: Implementar y validar con Agent

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

Si Agent se va de alcance:

```
Deten el refactor amplio. Limita el cambio a backend/app/services/note_service.py. Corrige solo el bug de arranque y valida con pytest backend/tests/test_notes_page.py.
```

### Validación del ejercicio 4

```bash
pytest backend/tests/
```

Todos los tests deben pasar.

---

## ✅ Cerrar este lab: abrir el PR

Cuando `pytest backend/tests/` pase limpio:

1. Haz commit y push de tu corrección:

   ```bash
   git add backend/app/services/note_service.py
   git commit -m "fix: correct note loading in NoteService.load_initial_notes"
   git push
   ```

2. Crea el Pull Request en GitHub:

   ```bash
   gh pr create --base main --title "fix: ejercicio 4 — corrección bug de arranque" --body "Corrección del bug de arranque identificado en los ejercicios 1–4."
   ```

   O abre la URL que Git imprime en el terminal tras el `push` para crearlo desde la interfaz web.

3. Espera a que GitHub Actions valide los tests (~1 minuto). **Fusiona el PR** cuando pasen.

> Al fusionar, este issue se cerrará automáticamente y se abrirá el issue del siguiente lab.
