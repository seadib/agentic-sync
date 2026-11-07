# AgenticSync

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform: Antigravity](https://img.shields.io/badge/Antigravity-Skill-4285F4)](https://github.com/seadib/agentic-sync)
[![Platform: Claude](https://img.shields.io/badge/Claude-Code%20&%20Desktop-7C3AED)](https://github.com/seadib/agentic-sync)
[![Platform: Cursor](https://img.shields.io/badge/Cursor-Rules-black)](https://github.com/seadib/agentic-sync)
[![Standard: 4--Pillars](https://img.shields.io/badge/Architecture-4--Pillars-10b981)](https://github.com/seadib/agentic-sync)

The Autonomous Synchronization and Guardrail Protocol for AI Coding Agents.

AgenticSync prevents autonomous AI agents from hallucinating architecture, introducing technical debt, causing monolithic file bloat, or leaking credentials during multi-step development sprints.

---

## Technical Overview

Autonomous coding agents (powered by Claude 3.5 Sonnet, GPT-4o, Gemini Pro) frequently encounter four critical failure modes on repositories exceeding 1,000 lines:

1. **Context Drift:** The agent modifies unintended files or loses awareness of prior architecture decisions.
2. **Credential Exposure:** Secret keys, environment files (`.env`), or service account tokens are staged and committed to public remotes.
3. **Monolithic Accumulation:** Code is continuously injected into single files (`app.js`, `style.css`) instead of adhering to modular system design.
4. **Documentation Disconnect:** Code logic changes while project specifications remain stale.

AgenticSync addresses these issues through five synchronized execution phases, a 4-pillar architectural standard, token-optimized Abstract Syntax Tree (AST) mapping, and automated pre-commit verification.

---

## Installation Guide

### 1. Google Antigravity

#### Workspace Installation (Per Project)
Clone the skill directly into your project's `.agents/skills` directory:

```bash
git clone https://github.com/seadib/agentic-sync.git .agents/skills/agentic-sync
```

Antigravity detects `SKILL.md` automatically and enforces the 4-pillar workflow.

#### Global Installation (System-Wide)

```bash
# macOS / Linux
git clone https://github.com/seadib/agentic-sync.git ~/.gemini/antigravity/skills/agentic-sync

# Windows (PowerShell)
git clone https://github.com/seadib/agentic-sync.git "$HOME\.gemini\antigravity\skills\agentic-sync"
```

---

### 2. Claude Code (Anthropic CLI)

Add the skill directory to your Claude Code workspace configuration:

```bash
# Inside your project root
mkdir -p .claude/skills
git clone https://github.com/seadib/agentic-sync.git .claude/skills/agentic-sync
```

Add the following directive to your project's `CLAUDE.md`:

```markdown
## Development Protocol
This project enforces the AgenticSync standard.
Before writing or modifying code:
1. Inspect the repository map via `python .claude/skills/agentic-sync/scripts/generate_repo_map.py .`
2. Consult the 4-pillar documentation under `docs/` (Security, Database, Design, Logic).
3. Execute `python .claude/skills/agentic-sync/scripts/verify_changes.py` prior to committing.
```

---

### 3. Cursor & Windsurf IDEs

Initialize the guardrail directly in your root `.cursorrules` file:

```markdown
# AgenticSync Guardrail Policy
- Always reference docs/00_MASTER_ROADMAP.md for task sequencing.
- Sensitive files (*.key, *.pem, .env, service_account*.json) are strictly prohibited from staging.
- Modularize code: do not exceed 400 lines per source file.
- Update the corresponding docs/[01-04]_*.md changelog entry upon completing any code modification.
```

To enable pre-commit automated checks in your repository:

```bash
python .agents/skills/agentic-sync/scripts/install_hook.py
```

---

### 4. ChatGPT / OpenAI Custom GPTs

1. Navigate to **GPT Builder** -> **Configure** -> **Knowledge**.
2. Upload `SKILL.md` and `templates/PILLAR_TEMPLATE.md`.
3. In **Instructions**, declare:
   > "Operate as a Principal Software Engineer following the AgenticSync standard. Refuse to perform undocumented edits. Break all architectural tasks into the 4 defined pillars (Security, Database, Design, Logic), and append versioned changelogs to docs/ after each turn."

---

## 4-Pillar Architectural Standard

AgenticSync enforces clear separation of concerns across four persistent markdown files located in `docs/`:

```
project-root/
└── docs/
    ├── 00_MASTER_ROADMAP.md         # Master roadmap, information architecture, version milestones
    ├── 01_SECURITY_AND_AUTH.md      # Credentials, secret boundaries, IAM policies, audit logs
    ├── 02_DATABASE_AND_CMS.md       # Schemas, migrations, query projections, data models
    ├── 03_DESIGN_AND_ASSETS.md      # CSS design tokens, layout hierarchy, asset directories
    └── 04_LOGIC_AND_ARCHITECTURE.md # Application routing, state machines, business algorithms
```

---

## Performance Comparison: Before vs. After

| Metric | Without AgenticSync | With AgenticSync Standard |
| :--- | :--- | :--- |
| **Context Window Overhead** | Full source files parsed (8,000+ tokens) | AST symbol maps generated (~1,200 tokens) |
| **Credential Safety** | Secrets frequently committed inadvertently | Pre-commit hook terminates commit on secret pattern detection |
| **Code Structure** | Monolithic accumulation | Enforced domain separation across 4 distinct pillars |
| **Debugging & Traceability** | Untracked file alterations | Semantic versioning and changelogs appended per turn |
| **Verification Loop** | Assumed execution success | Self-healing stdout/stderr error interception prior to completion |

---

## Built-In CLI Utilities

### 1. Repository Symbol Mapper (`generate_repo_map.py`)
Generates an AST symbol outline of functions, classes, and exported constants within a token budget:

```bash
python scripts/generate_repo_map.py .
```

### 2. Pre-Commit Safety Scanner (`verify_changes.py`)
Verifies git status and prevents credentials (`service_account.json`, `.env`, `.key`) from being staged:

```bash
python scripts/verify_changes.py
```

### 3. Automated Git Hook Installer (`install_hook.py`)
Configures `.git/hooks/pre-commit` to execute safety checks automatically before every commit:

```bash
python scripts/install_hook.py
```

---

## Contributing

Contributions adhering to standard Conventional Commits are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and review the [MIT License](LICENSE) before submitting pull requests.

## License

Distributed under the **MIT License**. Copyright (c) 2026 Abdullah Al Adib (seadib).
