# FRDR Helper as MCP Server — High-Level Plan

## Goal

Package the FRDR dataset preparation workflow as an MCP server that works with both **Claude Code** (stdio) and **ChatGPT Desktop** (SSE/HTTP), enabling researchers without CLI access to use the workflow through a chat interface.

## Implementation status (2026-03-24)

This plan is largely not implemented yet.

### Implemented prerequisites

- The repo now has the workflow definition in `AGENTS.md` and `steps/*.md`.
- Dataset state is tracked in `metadata.yaml`.
- Local preparation tooling exists for the Rogers Pass dataset, including `scripts/prepare_rogers_pass_dataset.py`.
- Jupyter/MCP-adjacent local tooling exists via `scripts/jupyter_mcp.py` and the `jupyter-mcp-server` dependency.

### Not implemented

- There is no `frdr_mcp_server/` package or equivalent MCP server application in the repo.
- `fastmcp` is not configured as a project dependency.
- None of the proposed MCP tools (`scope_init`, `research`, `explore_data`, `quality_check`, `draft_readme`, `validate_preflight`, `export_archive`, `get_status`) exist as MCP-exposed server tools.
- No MCP resources or prompts from this plan are implemented.
- No SSE/HTTP transport or ChatGPT Desktop integration is present.
- No Custom GPT instruction bundle or connector setup from this plan is present.

### Practical read

The project has implemented the underlying dataset workflow, but not the MCP productization layer described here.

## Current state

- Workflow logic lives in `AGENTS.md` + `steps/*.md` (markdown instructions read by Claude Code)
- Python helpers in `utils/` (e.g., `frdr_metadata.py`)
- State tracked in `metadata.yaml` per dataset
- 8-step pipeline: Scope → Research → Explore → QC → Data Prep → README → Preflight → Deposit

## Target architecture

```
┌──────────────────────────────────────────┐
│          frdr-helper MCP Server           │
│        (Python, FastMCP framework)        │
│                                          │
│  TOOLS (callable by any MCP client):     │
│  ┌────────────────────────────────────┐  │
│  │ scope_init        — create dataset │  │
│  │                     dir, seed      │  │
│  │                     metadata.yaml  │  │
│  │ research          — fetch DOI,     │  │
│  │                     search lit,    │  │
│  │                     populate       │  │
│  │                     metadata       │  │
│  │ explore_data      — profile        │  │
│  │                     uploaded files │  │
│  │                     (stats, dtypes,│  │
│  │                     preview)       │  │
│  │ quality_check     — run QC rules,  │  │
│  │                     flag issues    │  │
│  │ draft_readme      — generate FRDR  │  │
│  │                     README from    │  │
│  │                     metadata +     │  │
│  │                     template       │  │
│  │ validate_preflight— final checks   │  │
│  │ export_archive    — zip dataset    │  │
│  │                     for download   │  │
│  │ get_status        — workflow state │  │
│  └────────────────────────────────────┘  │
│                                          │
│  RESOURCES (read-only context):          │
│  - frdr://template/readme                │
│  - frdr://vocabulary/keywords            │
│  - frdr://docs/project-context           │
│  - frdr://dataset/{id}/metadata          │
│                                          │
│  PROMPTS (conversation starters):        │
│  - start_new_dataset                     │
│  - resume_workflow                       │
│                                          │
└──────────────────────────────────────────┘
        ▲                    ▲
        │ stdio              │ SSE / streamable HTTP
   Claude Code          ChatGPT Desktop
   (local files)        (file uploads → server working dir)
```

## Simplified scope for chat interfaces

Not all 8 steps translate well to chat. The chat-facing workflow is:

| Step | Chat version | Notes |
|------|-------------|-------|
| 1. Scope | Interactive Q&A → `scope_init` tool | User describes dataset, agent asks clarifying questions |
| 2. Research | `research` tool (web search + DOI lookup) | Works well in chat |
| 3. Explore | `explore_data` tool on uploaded files | Limited to what fits in Code Interpreter / upload size |
| 4. QC | `quality_check` tool returns report | Simplified rules, no notebook |
| 5. Data Prep | Skipped or manual | Too complex for chat sandbox |
| 6. README | `draft_readme` tool | Core deliverable, works great |
| 7. Preflight | `validate_preflight` tool | Automated checks |
| 8. Deposit | Manual (instructions provided) | Human does the actual FRDR submission |

**Output:** `export_archive` produces a zip containing README.txt, metadata.yaml, and any generated artifacts. In ChatGPT, user downloads this. In Claude Code, it's written to disk.

## Key design decisions

### 1. State management
- Server maintains a working directory per dataset session
- `metadata.yaml` is the state file (same schema as current)
- Each tool reads/updates metadata.yaml and returns results to the LLM
- LLM doesn't need to understand internal state — tools enforce workflow order

### 2. File handling across platforms

| Platform | File input | File output |
|----------|-----------|-------------|
| Claude Code | Local paths (tools read directly) | Written to `datasets/{id}/` |
| ChatGPT | User uploads in chat → server receives via MCP | `export_archive` → zip download |

For ChatGPT, the MCP server needs to run somewhere the ChatGPT app can reach (localhost or hosted). Files uploaded in chat are passed to tools as content.

### 3. Framework choice: FastMCP (Python)
- Team knows Python
- Existing utils are Python
- FastMCP is the simplest MCP framework
- Supports both stdio (Claude Code) and SSE (ChatGPT) transports

### 4. What stays in markdown instructions
- The MCP server handles **tool logic** (what each step does)
- A companion **system prompt / GPT instructions** file handles **orchestration** (which tools to call when, how to interact with the user, human-in-the-loop gates)
- This prompt file is shared across platforms with minor adaptation

## Implementation phases

### Phase 0: Workflow prerequisites
- Status: Implemented
- The repo has enough workflow definition and local scripts to serve as the basis for an MCP server, but only as conventional project files today.

### Phase 1: Core MCP server (MVP)
- Status: Not started
- Set up FastMCP project (`uv init`, dependencies)
- Implement tools: `scope_init`, `draft_readme`, `export_archive`, `get_status`
- Implement resources: README template, controlled vocabulary
- Test with Claude Code via stdio
- **Delivers:** Basic scope-to-README flow

### Phase 2: Research and exploration tools
- Status: Not started
- `research` tool (DOI resolution, web search integration)
- `explore_data` tool (file profiling with pandas)
- `quality_check` tool (basic QC rules)
- Port logic from `utils/frdr_metadata.py`

### Phase 3: ChatGPT integration
- Status: Not started
- Add SSE transport to server
- Write Custom GPT instructions (system prompt) for orchestration
- Test with ChatGPT Desktop Developer Mode
- Document setup for users (install, configure connector)

### Phase 4: Polish
- Status: Not started
- `validate_preflight` tool
- Prompts (start_new_dataset, resume_workflow)
- Error handling and edge cases
- User documentation

## Risks and mitigations

| Risk | Mitigation |
|------|-----------|
| ChatGPT MCP is beta, may change | Keep server protocol-standard; ChatGPT is a bonus, not the only client |
| File size limits in ChatGPT uploads | Document limits; large datasets stay in Claude Code |
| Team maintenance burden | FastMCP is simple Python; tools are isolated functions, easy to understand |
| Over-engineering vs. current approach | Phase 1 MVP is small; validate before building more |
| ChatGPT MCP requires Plus/Pro | Acceptable — target audience is researchers with institutional accounts |

## File structure (proposed)

```
frdr_mcp_server/
├── pyproject.toml
├── server.py              # FastMCP app, transport config
├── tools/
│   ├── scope.py           # scope_init
│   ├── research.py        # research
│   ├── explore.py         # explore_data
│   ├── quality.py         # quality_check
│   ├── readme.py          # draft_readme
│   ├── preflight.py       # validate_preflight
│   └── archive.py         # export_archive
├── resources/
│   ├── templates/         # README template, metadata schema
│   └── vocabulary/        # controlled keywords
├── prompts/
│   ├── start_new_dataset.txt
│   └── resume_workflow.txt
├── chatgpt/
│   └── gpt_instructions.md  # Custom GPT system prompt
└── tests/
```

## Open questions

1. **Hosting for ChatGPT SSE** — run locally (user installs) or host centrally? Localhost is simpler but requires setup. Hosted means managing a server.
2. **Authentication** — ChatGPT MCP supports OAuth. Needed if hosted; not needed if localhost.
3. **Data Prep step** — include a simplified version or explicitly exclude from chat workflow?
4. **Notebook execution** — can the MCP server run notebooks, or should exploration be pure Python functions?
