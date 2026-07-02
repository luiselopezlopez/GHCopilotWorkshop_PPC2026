# Lab 2: Prompts, Instructions, Skills y Agents para una feature nueva

## Objetivo

Usar las customizaciones de Copilot para preparar la siguiente evolucion natural de la aplicacion: sustituir el almacenamiento en memoria por persistencia en un archivo SQLite local.

El objetivo del laboratorio no es construir una arquitectura compleja. El objetivo es aprender como `instructions`, `prompt`, `skill` y `agent` ayudan a añadir una feature nueva manteniendo un estilo de desarrollo estandar:

1. entender primero el diseño actual,
2. proponer un cambio incremental,
3. mantener rutas y UI estables,
4. validar con pasos pequenos.

## Resultado esperado

Al terminar este lab deberias ser capaz de:

- explicar como se usa cada tipo de customizacion al añadir una feature,
- colocar cada archivo en su ubicacion correcta dentro de `.github/`,
- pedir a Copilot un diseño incremental para SQLite,
- distinguir entre una guia persistente, un prompt reusable, una skill de procedimiento y un agent de ejecucion,
- mantener la implementacion pequena y explicable.

## Archivos foco iniciales

- `resources/copilot-instructions.md`
- `resources/instructions/fastapi.instructions.md`
- `resources/prompts/add-sqlite-persistence.prompt.md`
- `resources/skills/notes-sqlite-persistence/SKILL.md`
- `resources/agents/notes-feature-finisher.agent.md`

## Preparacion del laboratorio

Al comenzar este laboratorio, la carpeta `.github/` no debe contener ninguna customizacion del repo. Los archivos de partida viven en `resources/` y el objetivo es moverlos a su ubicacion final correcta.

Antes de tocar nada, comprueba la situacion actual con estos comandos:

```powershell
Get-ChildItem .\resources -Recurse
Test-Path .\.github
```

## Paso 0: Colocar los archivos en el sitio correcto

Ejecuta exactamente estos comandos:

```powershell
New-Item -ItemType Directory -Force .github\instructions | Out-Null
New-Item -ItemType Directory -Force .github\prompts | Out-Null
New-Item -ItemType Directory -Force .github\skills\notes-sqlite-persistence | Out-Null
New-Item -ItemType Directory -Force .github\agents | Out-Null
Copy-Item .\resources\copilot-instructions.md .\.github\copilot-instructions.md
Copy-Item .\resources\instructions\fastapi.instructions.md .\.github\instructions\fastapi.instructions.md
Copy-Item .\resources\prompts\add-sqlite-persistence.prompt.md .\.github\prompts\add-sqlite-persistence.prompt.md
Copy-Item .\resources\skills\notes-sqlite-persistence\SKILL.md .\.github\skills\notes-sqlite-persistence\SKILL.md
Copy-Item .\resources\agents\notes-feature-finisher.agent.md .\.github\agents\notes-feature-finisher.agent.md
```

Despues confirma que han quedado colocados con:

```powershell
Get-ChildItem .\.github -Recurse
```

## Como se usan de verdad dentro de Copilot

Antes de entrar en cada ejercicio, conviene dejar claro que no todos estos mecanismos se usan igual:

1. `instructions`: no se lanzan manualmente; Copilot las aplica automaticamente cuando trabajas sobre archivos que encajan con su alcance.
2. `prompt`: se invoca como prompt reutilizable desde el chat una vez colocado en `.github/prompts/`.
3. `skill`: se puede pedir de forma explicita al describir un problema o una tarea repetible.
4. `agent`: se usa seleccionando ese agent especializado para ejecutar una tarea acotada.

Piensa en ello asi:

- las `instructions` influyen en como responde Copilot,
- el `prompt` acelera una peticion concreta,
- la `skill` empaqueta un procedimiento repetible,
- el `agent` encapsula un rol operativo.

## Orden recomendado

Sigue este orden, porque va de lo mas simple a lo mas estructurado:

1. instructions,
2. prompt,
3. skill,
4. agent.

## Escenario funcional del lab

La app actual guarda notas en memoria. Queremos preparar una evolucion pequena y razonable:

- persistir las notas en un archivo SQLite local,
- mantener las rutas actuales,
- no reescribir la UI,
- no convertir el ejercicio en una migracion grande.

## Ejercicio 1: Instructions

Abre estos dos archivos:

- `.github/copilot-instructions.md`
- `.github/instructions/fastapi.instructions.md`

En modo `Ask`, pega este prompt exacto:

```text
Lee estas instructions del repo:
- .github/copilot-instructions.md
- .github/instructions/fastapi.instructions.md

Explicame:
1. que reglas son globales,
2. que reglas aplican solo a backend/**/*.py,
3. como empujan a Copilot hacia una implementacion incremental de SQLite en vez de un refactor amplio.
```

Si quieres que Copilot proponga un cambio concreto en las instructions, usa este prompt exacto en modo `Plan`:

```text
Genera un plan pequeño para reforzar estas instructions con dos objetivos:
- que una nueva feature de persistencia use una capa de servicio o repositorio pequena,
- que el agente valide primero con un comando estrecho antes de ampliar el alcance.
```

### Ejemplo de uso real de las instructions

Las `instructions` no se ejecutan con un comando especial. Su efecto se ve cuando pides trabajo sobre un archivo que cae dentro de `backend/**/*.py`.

Prueba este ejemplo en modo `plan`:

```text
Revisa backend/app/services/note_service.py y propon una evolucion pequena para soportar persistencia SQLite en archivo.

Restricciones:
- manten las rutas actuales,
- no metas SQL en las plantillas ni en las rutas,
- valida con un unico comando pequeno.
```

Que deberias observar:

1. Copilot tiende a mantener el cambio pequeno.
2. Propone una separacion razonable entre rutas y persistencia.
3. Suele incluir una validacion acotada porque las instructions ya se lo piden.

## Ejercicio 2: Prompt reutilizable

Abre `.github/prompts/add-sqlite-persistence.prompt.md`.

Usa este prompt exacto en modo `Ask`:

```text
Lee .github/prompts/add-sqlite-persistence.prompt.md y dime:
1. que tarea puntual resuelve,
2. por que esto es un prompt y no una instruction,
3. que parte reforzarias para que la propuesta sea aun mas incremental.
```

Despues, en modo `Agent`, usa este prompt exacto:

```text
Mejora solo .github/prompts/add-sqlite-persistence.prompt.md.

Quiero que el prompt:
- obligue a leer primero rutas, servicio y test principal,
- pida una propuesta de diseño pequena,
- sugiera una validacion estrecha,
- mantenga el foco en persistencia SQLite local.
```

### Ejemplo de uso real del prompt

Una vez que el archivo existe en `.github/prompts/`, puedes reutilizarlo para arrancar siempre la conversacion de diseño sobre esta feature sin reescribir el contexto.

Ejemplo de uso esperado en el chat:

```text
/add-sqlite-persistence
```

Si quieres acotarlo un poco mas, añade despues:

```text
Quiero una propuesta incremental para persistir notas en un archivo sqlite local sin rehacer la app.
```

Que deberias observar:

1. Copilot parte de una estructura de analisis ya preparada.
2. Lee los archivos relevantes antes de proponer cambios.
3. La respuesta queda mas consistente entre alumnos porque el punto de partida es comun.

## Ejercicio 3: Skill

Abre `.github/skills/notes-sqlite-persistence/SKILL.md`.

Primero usa modo `Ask` con este prompt exacto:

```text
Lee .github/skills/notes-sqlite-persistence/SKILL.md y explicame por que esto es una skill y no solo un prompt.
Quiero una explicacion centrada en el procedimiento, el criterio de salida y la reutilizacion.
```

Despues usa modo `Plan` con este prompt exacto:

```text
Genera un plan pequeño para ampliar la skill notes-sqlite-persistence con un caso adicional:
arranque de la base de datos vacia o inicializacion del esquema.

Quiero mantener la skill corta, operativa y especifica de este workshop.
```

Y si vas a aplicarlo, usa modo `Agent` con esto:

```text
Implementa el cambio acordado solo en .github/skills/notes-sqlite-persistence/SKILL.md.
Añade el caso nuevo sin convertir la skill en un documento largo o generico.
```

### Ejemplo de uso real de la skill

La `skill` tiene sentido cuando la tarea coincide con un patron repetible del workshop: añadir persistencia SQLite sin romper la sencillez de la app.

Prueba este ejemplo en modo `Ask` o `Agent`:

```text
Quiero que uses la skill notes-sqlite-persistence para guiar una propuesta de implementacion.
Lee primero el flujo actual de notas, propon la capa minima de persistencia SQLite y termina con una sola validacion inicial.
```

Que deberias observar:

1. Copilot sigue un procedimiento mas estable.
2. Empieza por entender el flujo actual antes de sugerir SQL.
3. La respuesta se parece menos a una improvisacion y mas a una receta reutilizable.

## Ejercicio 4: Agent especializado

Abre `.github/agents/notes-feature-finisher.agent.md`.

En modo `Ask`, pega esto:

```text
Lee .github/agents/notes-feature-finisher.agent.md y explicame:
1. que rol especializado define,
2. que limites de alcance tiene,
3. por que encaja mejor con una feature incremental que con un refactor grande.
```

Si vas a ajustarlo, usa este prompt exacto en modo `Agent`:

```text
Mejora solo .github/agents/notes-feature-finisher.agent.md.

Objetivos:
- dejar aun mas claro que debe implementar features pequenas y no refactors grandes,
- exigir leer tests y servicio antes de editar,
- mantener SQLite encapsulado fuera de las rutas,
- mantener el texto corto y operativo.
- utilizar los prompts, skills e instructions disponibles en el repositorio para optimizar la ejecucion de la tarea
```

### Ejemplo de uso real del agent

Aqui la idea no es solo pedir consejo, sino delegar ejecucion en un rol especializado.

Selecciona el agent `notes-feature-finisher` y lanza una peticion como esta:

```text
Añade persistencia SQLite en archivo a la app de notas con el cambio minimo razonable.

Condiciones:
- manten las rutas y la UI actuales,
- no distribuyas SQL por los handlers,
- lee antes el servicio y el test principal,
- valida al final con un comando pequeno antes de ampliar pruebas.
```

Que deberias observar:

1. El agent trabaja con mas autonomia que un prompt normal.
2. Aun asi mantiene limites operativos claros.
3. El resultado deberia ser mas estable para una implementacion incremental que para brainstorming abierto.

## Validacion conceptual

Cuando termines, responde por escrito a estas cuatro preguntas:

1. Cuando usarías un prompt en vez de una instruction.
2. Cuando una skill aporta mas que un prompt.
3. Cuando compensa crear un agent.
4. Como se combinan los cuatro elementos para añadir una feature nueva sin perder simplicidad.

## Frases guia para recordar

- Prompt: una tarea puntual.
- Instructions: reglas persistentes.
- Skill: procedimiento reutilizable.
- Agent: rol especializado con autonomia acotada.

## Criterio de exito

El lab se considera completado si:

1. has colocado correctamente los cinco archivos de `resources/` dentro de `.github/`,
2. has usado cada customizacion con un ejemplo relacionado con persistencia SQLite,
3. puedes explicar por que cada una existe,
4. puedes decir que parte del trabajo resuelve cada una al añadir una feature nueva.
