# The AgenticSync Skill

Five agentic guardrail skills that keep AI coding agents from getting lost, breaking architecture, or leaking secrets. Free, MIT, no signup, no API key, nothing to connect.

One maps your entire codebase into a lightweight token-budget symbol tree. One enforces a 4-pillar living documentation standard. One catches secret leaks before they reach GitHub. One runs self-healing test loops when code breaks. And one synchronizes every turn into atomic, semantic Git commits.

Built for **Google Antigravity**, **Claude Code**, **Cursor**, **Windsurf**, and autonomous coding agents.

**It enforces how agents build, never how they hallucinate.** Structure and guardrails, clean-room style. Zero monolithic bloat, zero secret leaks, zero context drift.

---

## Install

Paste this into Antigravity or Claude:

```
https://github.com/seadib/agentic-sync

install skill
```

Or as a plugin, in Claude Code / Antigravity:

```
/plugin marketplace add seadib/agentic-sync
/plugin install agentic-sync@agentic-sync
```

Project-local instead of global: copy the folder directly into your repo:

```bash
# For Google Antigravity
git clone https://github.com/seadib/agentic-sync.git .agents/skills/agentic-sync

# For Claude Code
mkdir -p .claude/skills
git clone https://github.com/seadib/agentic-sync.git .claude/skills/agentic-sync
```

Global installation across all projects:

```bash
# macOS / Linux (Claude)
cp -r agentic-sync ~/.claude/skills/

# Windows / Linux (Antigravity)
cp -r agentic-sync ~/.gemini/antigravity/skills/
```

The tools need Python 3.8 or newer. Standard-library only. Nothing to pip install.

---

## The five skills

| Command / Skill | What it does |
| :--- | :--- |
| `/agentic-map` | Scans the repo with AST symbol extraction and generates a ~1,200 token outline of functions, classes, and routes. No 8,000-line prompt bloat. |
| `/agentic-plan` | Decomposes tasks into 4 living documentation pillars (`docs/01-04_*.md`): Security, Database, Design, and Logic. |
| `/agentic-verify` | Pre-commit linter that detects credentials (`.env`, `service_account.json`, `*.key`) and blocks broken commits before git touches origin. |
| `/agentic-heal` | Intercepts compiler, linter, or test failures from stdout/stderr, feeds them back to the LLM, and self-heals until tests pass. |
| `/agentic-sync` | Synchronizes turn changes into atomic Conventional Commits and appends versioned changelog entries after every task. |

---

## How to use it

Run them in order. Each phase reads what the last one wrote:

```
map -> plan -> execute -> verify -> sync
```

An example: refactoring a legacy 8,000-line web portal with an external CMS and sensitive credentials:

1. **`/agentic-map`** scans the project. Out comes the token-budget symbol map: 17 HTML routes, the CMS query client, and the monolith script. The agent knows exactly where functions live without reading 8,000 lines.
2. **`/agentic-plan`** creates the 4 persistent documentation pillars under `docs/`:
   - `01_SECURITY_AND_AUTH.md`: Audits exposed credentials and client-side password leaks.
   - `02_DATABASE_AND_CMS.md`: Documents Sanity/Postgres schemas and query projections.
   - `03_DESIGN_AND_ASSETS.md`: Plans CSS modularization and favicon/asset directory cleanup.
   - `04_LOGIC_AND_ARCHITECTURE.md`: Breaks the monolith into modular ES imports.
3. **Execution**: The agent makes targeted edits in small, isolated steps.
4. **`/agentic-verify`**: Scans git status. It flags that a private `service_account.json` was about to be staged, aborts the commit, and prompts the agent to isolate it into a private directory.
5. **`/agentic-sync`**: Updates the version tag (`v1.1`), records what changed in `docs/01_SECURITY_AND_AUTH.md`, and commits with a clean message: `feat(security): isolate service credentials and block public route`.

---

## The tools

Three standard-library Python scripts. None touch the network, none require pip packages:

```bash
python3 scripts/generate_repo_map.py .          # lightweight AST symbol tree
python3 scripts/verify_changes.py               # pre-commit secret leak guard
python3 scripts/install_hook.py                 # 1-click git hook installer
```

- **`generate_repo_map.py`**: Parses JavaScript, TypeScript, Python, and HTML files into class signatures, method names, and exported constants. Caps output so your prompt never runs out of context.
- **`verify_changes.py`**: Inspects `git status`. If any file matches sensitive patterns (`.env`, `credentials.json`, `service_account.json`, `*.key`), it exits with code 1 and blocks the commit.
- **`install_hook.py`**: Injects `verify_changes.py` into `.git/hooks/pre-commit` so that even human developers cannot accidentally push secrets to public GitHub.

---

## The 4 Pillars

Every project maintains four living markdown files under `docs/`:

```
your-project/
├── docs/
│   ├── 00_MASTER_ROADMAP.md         # Master roadmap, information architecture, version milestones
│   ├── 01_SECURITY_AND_AUTH.md      # Credentials, secret boundaries, IAM policies, audit logs
│   ├── 02_DATABASE_AND_CMS.md       # Schemas, migrations, query projections, data models
│   ├── 03_DESIGN_AND_ASSETS.md      # CSS design tokens, layout hierarchy, asset directories
│   └── 04_LOGIC_AND_ARCHITECTURE.md # Application routing, state machines, business algorithms
```

---

## Fine print

**It enforces architecture, clean-room style.** It prevents agents from piling 500 new lines into a bloated file when a modular helper should be created.

**It stops secret leaks at the local gate.** Pre-commit hooks run locally on your machine before files ever reach a remote repository.

**It tracks living history.** You never wonder what an AI changed three days ago; every modification is stamped in the corresponding pillar changelog with date and version.

---

## Files

```
skills/agentic-sync/
├── SKILL.md                         # Core agent instructions and workflow
├── README.md                        # Package documentation and install guide
├── CONTRIBUTING.md                  # Guidelines for open-source contributors
├── LICENSE                          # MIT License
├── scripts/
│   ├── generate_repo_map.py         # AST symbol mapper
│   ├── verify_changes.py            # Pre-commit secret verification
│   └── install_hook.py              # Git pre-commit hook installer
├── templates/
│   └── PILLAR_TEMPLATE.md           # Starter template for the 4 pillars
├── references/
│   └── AIDER_SWE_ARCHITECTURE.md    # Technical deep-dive on Aider & SWE-agent
└── examples/
    └── BEFORE_AFTER_COMPARISON.md   # Real-world benchmark matrix
```

## License

MIT. Copyright (c) 2026 Abdullah Al Adib ([seadib](https://github.com/seadib)). Take it, change it, ship it.
