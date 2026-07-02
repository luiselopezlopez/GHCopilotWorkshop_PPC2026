## 🚀 Paso 0: Abrir el Codespace y crear tu rama de trabajo

**Antes de hacer cualquier otra cosa**, sigue estos pasos en orden.

1. Abre este repositorio en un Codespace:

   [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

2. Espera a que VS Code cargue en el navegador y las extensiones terminen de instalarse.

3. En el terminal integrado, crea y publica tu rama de trabajo:

   ```bash
   git checkout -b ejercicio-8/customizations
   git push -u origin ejercicio-8/customizations
   ```

4. Confirma que estás en la rama correcta:

   ```bash
   git branch --show-current
   # Resultado esperado: ejercicio-8/customizations
   ```

---

## ✅ Ejercicio 4 completado — Ejercicios 5–8: Customizaciones de Copilot

¡Buen trabajo! Has diagnosticado y corregido el bug de arranque usando Ask, Plan y Agent.

Ahora aprenderás a usar las **customizaciones de GitHub Copilot** para preparar la siguiente evolución de la app: sustituir el almacenamiento en memoria por persistencia en un archivo SQLite local.

---

## Preparación: colocar los archivos

Los archivos de customización viven en `resources/`. Tu tarea es moverlos a su ubicación correcta dentro de `.github/`:

| Origen | Destino |
|--------|---------|
| `resources/copilot-instructions.md` | `.github/copilot-instructions.md` |
| `resources/instructions/fastapi.instructions.md` | `.github/instructions/fastapi.instructions.md` |
| `resources/prompts/add-sqlite-persistence.prompt.md` | `.github/prompts/add-sqlite-persistence.prompt.md` |
| `resources/skills/notes-sqlite-persistence/SKILL.md` | `.github/skills/notes-sqlite-persistence/SKILL.md` |
| `resources/agents/notes-feature-finisher.agent.md` | `.github/agents/notes-feature-finisher.agent.md` |

```bash
mkdir -p .github/instructions .github/prompts .github/skills/notes-sqlite-persistence .github/agents
cp resources/copilot-instructions.md .github/copilot-instructions.md
cp resources/instructions/fastapi.instructions.md .github/instructions/fastapi.instructions.md
cp resources/prompts/add-sqlite-persistence.prompt.md .github/prompts/add-sqlite-persistence.prompt.md
cp resources/skills/notes-sqlite-persistence/SKILL.md .github/skills/notes-sqlite-persistence/SKILL.md
cp resources/agents/notes-feature-finisher.agent.md .github/agents/notes-feature-finisher.agent.md
```

Confirma que quedaron colocados:

```bash
find .github -name "*.md" | sort
```

---

## Cómo se activa cada tipo de customización

| Tipo | Cómo se activa |
|------|---------------|
| `instructions` | Automáticamente cuando trabajas sobre archivos que encajan con su alcance |
| `prompt` | Se invoca con `/nombre-del-prompt` desde el chat |
| `skill` | Se pide de forma explícita describiendo la tarea |
| `agent` | Se selecciona el agent especializado desde el chat |

---

## Ejercicio 5: Instructions

### Objetivo

Entender qué reglas se aplican automáticamente cuando Copilot trabaja sobre archivos del backend.

### Instrucciones

Abre `.github/copilot-instructions.md` y `.github/instructions/fastapi.instructions.md`.

En modo **Ask**, pega:

```
Lee estas instructions del repo:
- .github/copilot-instructions.md
- .github/instructions/fastapi.instructions.md

Explicame:
1. que reglas son globales,
2. que reglas aplican solo a backend/**/*.py,
3. como empujan a Copilot hacia una implementacion incremental de SQLite en vez de un refactor amplio.
```

### Validación

Prueba el efecto real en modo **Plan** sobre un archivo del backend:

```
Revisa backend/app/services/note_service.py y propon una evolucion pequena para soportar persistencia SQLite en archivo.

Restricciones:
- manten las rutas actuales,
- no metas SQL en las plantillas ni en las rutas,
- valida con un unico comando pequeno.
```

Verifica que Copilot mantiene el cambio pequeño y propone una validación acotada — efecto directo de las instructions.

---

## Ejercicio 6: Prompt reutilizable

### Objetivo

Usar un prompt predefinido para arrancar siempre la conversación de diseño sobre esta feature con el mismo contexto.

### Instrucciones

Abre `.github/prompts/add-sqlite-persistence.prompt.md`.

En modo **Ask**, pega:

```
Lee .github/prompts/add-sqlite-persistence.prompt.md y dime:
1. que tarea puntual resuelve,
2. por que esto es un prompt y no una instruction,
3. que parte reforzarias para que la propuesta sea aun mas incremental.
```

### Validación

Invoca el prompt reutilizable desde el chat:

```
/add-sqlite-persistence
```

Verifica que Copilot parte de una estructura de análisis ya preparada y que la respuesta es consistente con el contexto del prompt.

---

## Ejercicio 7: Skill

### Objetivo

Entender cómo una skill empaqueta un procedimiento repetible con criterio de salida propio.

### Instrucciones

Abre `.github/skills/notes-sqlite-persistence/SKILL.md`.

En modo **Ask**, pega:

```
Lee .github/skills/notes-sqlite-persistence/SKILL.md y explicame por que esto es una skill y no solo un prompt.
Quiero una explicacion centrada en el procedimiento, el criterio de salida y la reutilizacion.
```

### Validación

Usa la skill en modo **Ask** o **Agent**:

```
Quiero que uses la skill notes-sqlite-persistence para guiar una propuesta de implementacion.
Lee primero el flujo actual de notas, propon la capa minima de persistencia SQLite y termina con una sola validacion inicial.
```

Verifica que Copilot sigue un procedimiento más estable que con un prompt libre y que empieza entendiendo el flujo antes de proponer SQL.

---

## Ejercicio 8: Agent especializado

### Objetivo

Delegar la ejecución de una feature incremental a un agent con un rol y límites de alcance definidos.

### Instrucciones

Abre `.github/agents/notes-feature-finisher.agent.md`.

En modo **Ask**, pega:

```
Lee .github/agents/notes-feature-finisher.agent.md y explicame:
1. que rol especializado define,
2. que limites de alcance tiene,
3. por que encaja mejor con una feature incremental que con un refactor grande.
```

Después, selecciona el agent `notes-feature-finisher` y lanza:

```
Añade persistencia SQLite en archivo a la app de notas con el cambio minimo razonable.

Condiciones:
- manten las rutas y la UI actuales,
- no distribuyas SQL por los handlers,
- lee antes el servicio y el test principal,
- valida al final con un comando pequeno antes de ampliar pruebas.
```

### Validación

Verifica que:

- [ ] El agent trabaja con autonomía pero mantiene límites operativos claros
- [ ] La implementación no distribuye SQL fuera del servicio
- [ ] Termina con una validación estrecha y explicable

### ✅ Cerrar este lab: abrir el PR

Cuando los cinco archivos estén en `.github/`:

1. Haz commit y push de los archivos de customización:

   ```bash
   git add .github/
   git commit -m "feat: add Copilot customizations for SQLite persistence"
   git push
   ```

2. Abre un **Pull Request** de `ejercicio-8/customizations` → `main`.

3. Espera a que GitHub Actions valide los archivos. **Fusiona el PR** cuando pasen.

> Al fusionar, este issue se cerrará automáticamente y el workshop quedará completado 🎉

---

¿Tienes dudas? Consulta [`docs/EJERCICIOS_5_8_CUSTOMIZACIONES.md`](docs/EJERCICIOS_5_8_CUSTOMIZACIONES.md).
