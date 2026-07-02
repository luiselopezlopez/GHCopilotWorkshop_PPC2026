# Instructor Runbook

## Objetivo del instructor

Usar esta sesion para enseñar un flujo de trabajo completo con GitHub Copilot:

1. entender antes de tocar codigo,
2. acotar antes de implementar,
3. automatizar sin perder control,
4. convertir patrones en customizaciones reutilizables.

## Mensaje de apertura sugerido

Texto exacto sugerido para abrir la sesion:

```text
Hoy no vamos a usar Copilot como simple autocomplete. Vamos a usarlo como herramienta para explorar un codebase, proponer un plan pequeño, ejecutar un cambio controlado y encapsular buenas practicas en prompts, instructions, skills y agents.
```

## Agenda sugerida minuto a minuto

1. 0-10 min: contexto, objetivo, prerequisitos y apertura del repo.
2. 10-45 min: ejercicios 1–4 (Ask, Plan y Agent sobre la app rota).
3. 45-100 min: ejercicios 5–8 (customizaciones orientadas a una nueva feature).
4. 100-120 min: recap, preguntas y siguientes pasos.

## Preparacion del docente antes de entrar en sala

Ejecuta estos comandos en tu maquina antes de la sesion:

```powershell
Set-Location "e:\Sesiones-y-materiales\workshop-GHCopilot"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
python -m compileall backend
pytest backend\tests\test_notes_page.py
```

Para demostrar el bug inicial del ejercicio 2:

```powershell
uvicorn app.main:app --app-dir backend --reload
```

## Guion del bloque inicial

### Qué enseñar en pantalla

1. Estructura del repo.
2. Carpeta `backend/`.
3. Carpeta `resources/`.
4. Carpeta `docs/`.

### Qué decir

Texto exacto sugerido:

```text
El caso del dia es una aplicacion web de notas, sencilla y completamente local. La aplicacion tiene un bug que impide el arranque. El objetivo no es solo arreglarla, sino aprender a usar Copilot para entender primero el problema, acotar la solucion y ejecutarla con control.
```

## Bloque 1: Ejercicios 1–4 (Ask, Plan y Agent)

### Objetivo docente del bloque 1

Que el alumno vea claramente que:

- `Ask` sirve para entender,
- `Plan` sirve para recortar alcance,
- `Agent` sirve para ejecutar un slice pequeño,
- la validacion debe ser estrecha y rapida.

### Prompt exacto que debes mostrar en directo

Abre Copilot Chat en modo `Ask` y pega esto:

```text
Haz onboard de este repo leyendo estos archivos:
- backend/app/main.py
- backend/app/routes/notes.py
- backend/app/services/note_service.py
- backend/app/schemas.py
- backend/tests/test_notes_page.py

Quiero que me expliques, sin proponer cambios todavia:
1. cual es la arquitectura general de la aplicacion,
2. que hace cada capa principal,
3. que puntos de arranque o inicializacion parecen mas sensibles,
4. que archivos deberia revisar primero antes de tocar nada.
```

### Qué remarcar

1. Pide a los asistentes que comparen la respuesta de Copilot con el codigo real.
2. Recalca que aun no se ha pedido implementacion.
3. Señala que una buena pregunta da contexto, alcance y restricciones.

### Segundo prompt exacto a enseñar

Después de ejecutar `uvicorn app.main:app --app-dir backend --reload` y mostrar el traceback, pega esto en modo `Ask`:

```text
La aplicacion falla al arrancar. Este es el error que estoy viendo en terminal:

[pega aqui el traceback completo o al menos las ultimas lineas]

Lee el codigo relevante y dime:
1. cual es la causa raiz exacta,
2. en que archivo esta,
3. por que rompe el startup,
4. cual seria la correccion minima razonable.
```

### Tercer prompt exacto a enseñar

Cambia a modo `Plan` y pega esto:

```text
Genera un plan minimo para corregir el bug de arranque de la app con estas restricciones:
- no reestructures toda la aplicacion,
- corrige solo la causa raiz,
- mantén la app monolitica y local,
- el cambio debe ser pequeno y facil de explicar en una sesion en vivo,
- incluye una unica validacion final con pytest backend/tests/test_notes_page.py.

No implementes todavia. Solo quiero pasos concretos.
```

### Cuarto prompt exacto a enseñar

Cambia a modo `Agent` y pega esto:

```text
Implementa el plan acordado sobre el backend.

Objetivo concreto:
- corrige el bug que impide arrancar la aplicacion,
- no conviertas esto en un refactor amplio,
- conserva el comportamiento de app local de notas,
- si tocas el servicio de notas, manten el cambio corto y explicable,
- valida al final con pytest backend/tests/test_notes_page.py.
```

### Comando exacto de validacion a enseñar

```powershell
pytest backend\tests\test_notes_page.py
```

### Qué observar durante el bloque

- Si Copilot se va de alcance, para y vuelve a acotar.
- Si propone demasiados archivos, recuerda que el objetivo es un slice pequeño.
- Si el grupo se atasca, usa la solucion del instructor para mostrar el siguiente paso.

## Bloque 2: Ejercicios 5–8 (customizaciones para una nueva feature)

### Objetivo docente del bloque 2

Que el grupo entienda la diferencia entre:

- una instruction persistente,
- un prompt reutilizable,
- una skill,
- un agent especializado.

Y que vea como esos mecanismos se aplican a una evolucion concreta del producto: añadir persistencia SQLite en archivo local sin reescribir la app.

### Frase exacta recomendada

```text
En este segundo bloque seguimos en la misma app de notas, pero cambiamos de tipo de trabajo. Ya no estamos corrigiendo un bug. Estamos preparando una feature nueva: persistir las notas en un archivo SQLite local con un cambio pequeno, incremental y facil de explicar.
```

### Paso previo obligatorio del bloque 2

Muestra que inicialmente la carpeta `.github/` no contiene customizaciones del repo y que el material de partida vive en `resources/`.

Comandos exactos sugeridos:

```powershell
Get-ChildItem .\resources -Recurse
Test-Path .\.github
New-Item -ItemType Directory -Force .github\instructions | Out-Null
New-Item -ItemType Directory -Force .github\prompts | Out-Null
New-Item -ItemType Directory -Force .github\skills\notes-sqlite-persistence | Out-Null
New-Item -ItemType Directory -Force .github\agents | Out-Null
Copy-Item .\resources\copilot-instructions.md .\.github\copilot-instructions.md
Copy-Item .\resources\instructions\fastapi.instructions.md .\.github\instructions\fastapi.instructions.md
Copy-Item .\resources\prompts\add-sqlite-persistence.prompt.md .\.github\prompts\add-sqlite-persistence.prompt.md
Copy-Item .\resources\skills\notes-sqlite-persistence\SKILL.md .\.github\skills\notes-sqlite-persistence\SKILL.md
Copy-Item .\resources\agents\notes-feature-finisher.agent.md .\.github\agents\notes-feature-finisher.agent.md
Get-ChildItem .\.github -Recurse
```

### Secuencia exacta recomendada

1. Abre `.github/copilot-instructions.md`.
2. Abre `.github/instructions/fastapi.instructions.md`.
3. Abre `.github/prompts/add-sqlite-persistence.prompt.md`.
4. Abre `.github/skills/notes-sqlite-persistence/SKILL.md`.
5. Abre `.github/agents/notes-feature-finisher.agent.md`.

### Mensaje clave que conviene verbalizar aqui

Texto exacto sugerido:

```text
No todo se usa igual. Las instructions actuan en segundo plano cuando trabajamos sobre archivos que encajan con su alcance. El prompt se invoca para arrancar una tarea concreta. La skill se pide cuando queremos que Copilot siga un procedimiento repetible. El agent se selecciona cuando queremos delegar ejecucion dentro de un rol acotado.
```

### Prompt exacto para explicar instructions

```text
Lee estas instructions del repo:
- .github/copilot-instructions.md
- .github/instructions/fastapi.instructions.md

Explicame:
1. que reglas son globales,
2. que reglas aplican solo a backend/**/*.py,
3. como empujan a Copilot hacia una implementacion incremental de SQLite en vez de un refactor amplio.
```

### Ejemplo de uso real que debes demostrar para instructions

Pega esto en modo `Agent` mientras tienes abierto `backend/app/services/note_service.py`:

```text
Revisa backend/app/services/note_service.py y propon una evolucion pequena para soportar persistencia SQLite en archivo.

Restricciones:
- manten las rutas actuales,
- no metas SQL en las plantillas ni en las rutas,
- valida con un unico comando pequeno.
```

Explica al grupo que aqui no se esta invocando una instruction manualmente: simplemente se ve su efecto sobre la respuesta.

### Prompt exacto para explicar el prompt reusable

```text
Lee .github/prompts/add-sqlite-persistence.prompt.md y explicame:
1. que tarea concreta resuelve,
2. por que esto es un prompt y no una instruction,
3. que mejora pequeña añadirias para hacerlo aun mas incremental.
```

### Ejemplo de uso real que debes demostrar para el prompt

En el chat, invoca el prompt reutilizable con:

```text
/add-sqlite-persistence
```

Si hace falta, añade despues:

```text
Quiero una propuesta incremental para persistir notas en un archivo sqlite local sin rehacer la app.
```

### Prompt exacto para explicar la skill

```text
Lee .github/skills/notes-sqlite-persistence/SKILL.md y explicame por que esto es una skill y no solo un prompt.
Quiero una explicacion centrada en el procedimiento, el criterio de salida y la reutilizacion.
```

### Ejemplo de uso real que debes demostrar para la skill

```text
Quiero que uses la skill notes-sqlite-persistence para guiar una propuesta de implementacion.
Lee primero el flujo actual de notas, propon la capa minima de persistencia SQLite y termina con una sola validacion inicial.
```

### Prompt exacto para explicar el agent

```text
Lee .github/agents/notes-feature-finisher.agent.md y explicame:
1. que rol especializado define,
2. que limites de alcance tiene,
3. por que encaja mejor con una feature incremental que con un refactor grande.
```

### Ejemplo de uso real que debes demostrar para el agent

Selecciona el agent `notes-feature-finisher` y lanza esto:

```text
Añade persistencia SQLite en archivo a la app de notas con el cambio minimo razonable.

Condiciones:
- manten las rutas y la UI actuales,
- no distribuyas SQL por los handlers,
- lee antes el servicio y el test principal,
- valida al final con un comando pequeno antes de ampliar pruebas.
```

## Cierre de la sesion

### Mensaje exacto sugerido

```text
La idea principal de hoy es que Copilot funciona mucho mejor cuando le pedimos primero comprension, luego plan y solo despues implementacion. Y cuando un patron se repite, lo sacamos del chat y lo convertimos en customizacion reusable.
```

## Plan B

### Si el grupo va lento

1. Prioriza los ejercicios 1–4 completos.
2. Convierte los ejercicios 5–8 en una demo guiada donde solo muevan los archivos y usen el prompt reusable y las instructions.
3. Deja skill y agent como explicacion dirigida por el docente.

### Si el grupo va rapido

1. Pide un test adicional para verificar que una nota creada reaparece tras reiniciar la app.
2. Refuerza la skill para cubrir inicializacion de esquema o base vacia.
3. Crea un segundo prompt reutilizable centrado en tests de persistencia.
