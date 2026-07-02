# Lab 1: Ask, Plan y Agent

## Objetivo

Usar GitHub Copilot de forma guiada para:

1. hacer onboard de un codebase ya existente,
2. entender por que la app no arranca,
3. generar un plan pequeño y verificable,
4. implementar la correccion con Agent,
5. validarla con un test estrecho.

El objetivo funcional del lab es corregir el bug que impide el arranque de la aplicacion web de notas.

## Resultado esperado

Al terminar este lab deberias ser capaz de:

- explicar la arquitectura actual de la app,
- describir donde se produce el fallo de arranque,
- pedir a Copilot un plan util y no demasiado grande,
- ejecutar un cambio concreto con Agent,
- validar el resultado con un comando de test.

## Archivos foco

- `backend/app/main.py`
- `backend/app/routes/notes.py`
- `backend/app/services/note_service.py`
- `backend/app/schemas.py`
- `backend/tests/test_notes_page.py`

## Preparacion

Abre una terminal en la raiz del repo y ejecuta exactamente estos comandos:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
python -m compileall backend
```

Ahora ejecuta exactamente este comando para reproducir el problema del laboratorio:

```powershell
uvicorn app.main:app --app-dir backend --reload
```

La aplicacion debe fallar al arrancar. Copia o conserva el traceback porque lo usaras en la conversacion con Copilot.

## Flujo de trabajo recomendado

En este lab no empieces editando. Sigue esta secuencia exacta:

1. `Ask` para hacer onboard.
2. `Ask` para diagnosticar el bug.
3. `Plan` para acotar.
4. `Agent` para implementar.
5. terminal para validar.

## Paso 1: Onboard del codebase con Ask

Abre Copilot Chat en modo `Agent`.

Pega este prompt exacto:

```text
/init onboard the code on the backend folder, which is where the application code lives. Ignore the folders deck, docs and resources. Also ignore any .md file you find in the repo as they are not related with the codebase
```.ne



## Paso 2: Diagnosticar el bug con Ask

Con el traceback del terminal a mano, pega este segundo prompt exacto en modo `Ask`:

```text
La aplicacion falla al arrancar. Este es el error que estoy viendo en terminal:

[pega aqui el traceback completo o al menos las ultimas lineas]

Lee el codigo relevante y dime:
1. cual es la causa raiz exacta,
2. en que archivo esta,
3. por que rompe el startup,
4. cual seria la correccion minima razonable.
```

## Paso 3: Acotar con Plan

Cambia Copilot Chat al modo `Plan`.

Pega este prompt exacto:

```text
Genera un plan minimo para corregir el bug de arranque de la app con estas restricciones:
- no reestructures toda la aplicacion,
- corrige solo la causa raiz,
- mantén la app monolitica y local,
- el cambio debe ser pequeno y facil de explicar en una sesion en vivo,
- incluye una unica validacion final con pytest backend/tests/test_notes_page.py.

No implementes todavia. Solo quiero pasos concretos.
```

## Paso 4: Revisar el plan antes de ejecutar

Antes de aceptar el plan, comprueba que cumple esto:

- toca pocos archivos,
- no introduce refactors grandes,
- corrige la causa raiz,
- termina con un test unico y estrecho.

Si el plan es demasiado grande, usa este prompt exacto:

```text
Reduce el plan al slice mas pequeno posible. Prefiero corregir solo el bug de startup y validar con un unico test, sin refactorizar toda la arquitectura.
```

## Paso 5: Implementar con Agent

Pasa Copilot Chat a modo `Agent`.

Pega este prompt exacto:

```text
Implementa el plan acordado sobre el backend.

Objetivo concreto:
- corrige el bug que impide arrancar la aplicacion,
- no conviertas esto en un refactor amplio,
- conserva el comportamiento de app local de notas,
- si tocas el servicio de notas, manten el cambio corto y explicable,
- valida al final con pytest backend/tests/test_notes_page.py.
```

## Paso 6: Validar por terminal

Cuando Agent termine, ejecuta exactamente esto:

```powershell
pytest backend\tests\test_notes_page.py
```

Si quieres validar tambien que la app ya arranca, ejecuta:

```powershell
uvicorn app.main:app --app-dir backend --reload
```

Y en otra terminal:

```powershell
Invoke-WebRequest -Uri http://127.0.0.1:8000/ | Select-Object -ExpandProperty StatusCode
```

## Paso 7: Si Agent se va de alcance

Si Agent intenta tocar demasiados archivos o reescribir demasiado, córtalo y vuelve a acotar con este prompt exacto:

```text
Deten el refactor amplio. Limita el cambio a backend/app/main.py, backend/app/services/note_service.py y backend/tests/test_notes_page.py. Corrige solo el bug de arranque y valida solo con pytest backend/tests/test_notes_page.py.
```

## Qué debe observar el alumno

Durante el ejercicio, fijate en estas señales:

- `Ask` sirve para entender y no para ejecutar cambios.
- `Plan` es util cuando se le dan restricciones claras.
- `Agent` funciona mejor si el slice ya esta acotado.
- el mejor resultado no es el mas grande, sino el mas verificable.

## Criterio de exito

El lab se considera completado si se cumplen los cuatro puntos siguientes:

1. Puedes explicar la arquitectura general de la app sin mirar la solucion del docente.
2. Has obtenido un plan pequeño y concreto.
3. La app ya arranca.
4. `pytest backend\tests\test_notes_page.py` termina correctamente.
