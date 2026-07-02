# ✅ Lab 1 completado — Lab 2: Customizaciones de Copilot

¡Buen trabajo! Has diagnosticado y corregido el bug de arranque usando Ask, Plan y Agent.

Ahora aprenderás a usar las **customizaciones de GitHub Copilot** para preparar la siguiente evolución de la app: sustituir el almacenamiento en memoria por persistencia en un archivo SQLite local.

## Lab 2: Prompts, Instructions, Skills y Agents

### Objetivo

Aprender cómo `instructions`, `prompt`, `skill` y `agent` ayudan a añadir una feature nueva manteniendo un estilo de desarrollo estándar.

### Archivos de partida

Los archivos de customización viven en `resources/`. Tu tarea es moverlos a su ubicación correcta dentro de `.github/`:

| Origen | Destino |
|--------|---------|
| `resources/copilot-instructions.md` | `.github/copilot-instructions.md` |
| `resources/instructions/fastapi.instructions.md` | `.github/instructions/fastapi.instructions.md` |
| `resources/prompts/add-sqlite-persistence.prompt.md` | `.github/prompts/add-sqlite-persistence.prompt.md` |
| `resources/skills/notes-sqlite-persistence/SKILL.md` | `.github/skills/notes-sqlite-persistence/SKILL.md` |
| `resources/agents/notes-feature-finisher.agent.md` | `.github/agents/notes-feature-finisher.agent.md` |

### Paso 0 — Colocar los archivos

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

### Cómo se usan dentro de Copilot

| Tipo | Cómo se activa |
|------|---------------|
| `instructions` | Automáticamente cuando trabajas sobre archivos que encajan con su alcance |
| `prompt` | Se invoca con `/nombre-del-prompt` desde el chat |
| `skill` | Se pide de forma explícita describiendo la tarea |
| `agent` | Se selecciona el agent especializado desde el chat |

### Ejercicio 1 — Instructions

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

### Ejercicio 2 — Prompt reutilizable

Una vez colocado en `.github/prompts/`, prueba en el chat:

```
/add-sqlite-persistence
```

### Ejercicio 3 — Skill

En modo **Ask**:

```
Lee .github/skills/notes-sqlite-persistence/SKILL.md y explicame por que esto es una skill y no solo un prompt.
Quiero una explicacion centrada en el procedimiento, el criterio de salida y la reutilizacion.
```

### Ejercicio 4 — Agent especializado

Selecciona el agent `notes-feature-finisher` y lanza:

```
Añade persistencia SQLite en archivo a la app de notas con el cambio minimo razonable.

Condiciones:
- manten las rutas y la UI actuales,
- no distribuyas SQL por los handlers,
- lee antes el servicio y el test principal,
- valida al final con un comando pequeno antes de ampliar pruebas.
```

### Criterio de éxito

1. Has colocado los cinco archivos en `.github/`.
2. Has usado cada customización con un ejemplo real.
3. Puedes explicar para qué sirve cada una al añadir una feature.

## Crear el PR del Lab 2

1. Crea una rama:
   ```bash
   git checkout -b lab2/customizations
   git add .github/
   git commit -m "feat: add Copilot customizations for SQLite persistence"
   git push origin lab2/customizations
   ```

2. Abre un **Pull Request** de `lab2/customizations` → `main`.

3. Espera a que GitHub Actions valide los archivos. Si pasa, **fusiona el PR** para completar el workshop.

---

¿Tienes dudas? Consulta [`docs/LAB2_CUSTOMIZATIONS.md`](docs/LAB2_CUSTOMIZATIONS.md).
