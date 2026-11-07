# 🔄 AgenticSync

<p align="center">
  <img src="https://img.shields.io/badge/Antigravity-Native_Skill-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Antigravity">
  <img src="https://img.shields.io/badge/Claude_Code-Supported-7C3AED?style=for-the-badge&logo=anthropic&logoColor=white" alt="Claude">
  <img src="https://img.shields.io/badge/ChatGPT-Compatible-10A37F?style=for-the-badge&logo=openai&logoColor=white" alt="ChatGPT">
  <img src="https://img.shields.io/badge/Cursor_&_Windsurf-Ready-000000?style=for-the-badge&logo=visualstudiocode&logoColor=white" alt="Cursor">
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="MIT License">
  <img src="https://img.shields.io/badge/Version-v1.0.0-emerald?style=for-the-badge" alt="Version">
</p>

> **The Autonomous Synchronization & Guardrail Protocol for AI Coding Agents.**  
> Keep your code, architecture, and agent memory 100% in sync without hallucination or context drift. Built on proven engineering patterns from **Aider**, **SWE-agent**, and **MetaGPT**.

---

## ⚡ The Problem: Why Do AI Agents Get Confused?

When software projects grow beyond a few files, LLMs (Claude, GPT-4o, Gemini) suffer from:
- ❌ **Context Drift:** Overwriting un-targeted files or hallucinating missing imports.
- ❌ **Documentation Drift:** Changing business logic without recording what was changed or why.
- ❌ **Accidental Credential Exposure:** Staging `.env` or `service_account.json` into public git.
- ❌ **Monolithic Bloat:** Turning 200-line scripts into 8,000-line unmaintainable monsters.

**AgenticSync** continuously synchronizes your agent's execution loop across 4 distinct architectural pillars, generates token-efficient AST symbol maps, enforces pre-commit secret guards, and logs every update in real time.

---

## ⚖️ Real-World Impact: Before vs. After

| Feature / Scenario | ❌ Typical AI Agent (Without Sync) | 🟢 With AgenticSync |
| :--- | :--- | :--- |
| **Token Efficiency** | Dumps 8,000-line monoliths into prompts, exhausting tokens and forgetting context. | Generates an elided AST symbol map (~1,200 tokens) using `generate_repo_map.py`. |
| **Secret Protection** | Accidentally commits `.env`, private keys, or `service_account.json` to public git. | `verify_changes.py` automatically blocks commits containing credentials via pre-commit hooks. |
| **Code Architecture** | Piles code into giant monoliths (`app.js`, `style.css`), creating massive tech debt. | Enforces **4 Modular Pillars** (Security, Database, Design, Logic). |
| **Change Tracking** | Makes 20 changes without a trail; you have no idea what broke 3 days later. | Appends semantic versioned entries (`[v1.2]`) to the specific pillar log after every single turn. |
| **Self-Healing** | Hallucinates fixes, breaks syntax, and falsely claims "Task Complete!" | Catches runtime errors in stdout/stderr and self-heals before reporting success. |

---

## 📦 1-Minute Quick Installation & Platform Setup

### 1. 🔷 Google Antigravity (AGY) Setup

#### Option A: Workspace Skill (Recommended)
Clone or place this folder into your project's `.agents/skills/` directory:
```bash
git clone https://github.com/YOUR_USERNAME/agentic-sync.git .agents/skills/agentic-sync
```
Antigravity automatically detects `SKILL.md` and activates this workflow for all turns.

#### Option B: Global Antigravity Skill
```bash
# Windows (PowerShell)
git clone https://github.com/YOUR_USERNAME/agentic-sync.git "$HOME\.gemini\antigravity\skills\agentic-sync"

# Mac / Linux
git clone https://github.com/YOUR_USERNAME/agentic-sync.git ~/.gemini/antigravity/skills/agentic-sync
```

---

### 2. 🟣 Claude Code & Claude Desktop Setup

#### For Claude Code (CLI)
Add this repository to your project instructions in `.claude/config.json` or `.clauderc`:
```json
{
  "skills": [
    "./skills/agentic-sync/SKILL.md"
  ]
}
```

#### For Claude Desktop (Projects / Custom Instructions)
1. Open your Claude Project $\rightarrow$ **Project Knowledge**.
2. Upload `SKILL.md` and `templates/PILLAR_TEMPLATE.md`.
3. Paste this in **Custom Instructions**:
   > *"Follow the 5-Phase Workflow defined in `SKILL.md`. Before modifying any file, check the 4-Pillar documentation under `docs/` and log every change in the corresponding change-log."*

---

### 3. 🟢 ChatGPT Plus / OpenAI Custom GPTs

1. Create a New GPT in the **GPT Builder**.
2. Under **Knowledge**, upload `SKILL.md` and `references/AIDER_SWE_ARCHITECTURE.md`.
3. In **Instructions**, add:
   ```markdown
   You are an autonomous Senior Software Engineer operating under the AgenticSync protocol.
   1. Never edit code without inspecting the repo map first.
   2. Always organize code changes into 4 pillars: Security, CMS/DB, UI/CSS, and Logic.
   3. Append versioned change-logs to docs after every modification.
   ```

---

### 4. 💻 Cursor & Windsurf AI Rules

#### For Cursor (`.cursorrules`)
Copy the following into your `.cursorrules` file at the root of your project:
```markdown
# AgenticSync Rules
- Always read docs/00_MASTER_ROADMAP.md before suggesting architectural changes.
- Ensure all secrets (keys, .env, service_account.json) are excluded from git.
- After every edit, update the corresponding pillar file in docs/*.md with a versioned change log.
```

---

## 🏗️ The 4-Pillar Architecture Template

Every codebase is automatically organized into four isolated, self-documenting files:

```
your-project/
├── docs/
│   ├── 00_MASTER_ROADMAP.md        # Executive roadmap, IA diagram & version milestones
│   ├── 01_SECURITY_AND_AUTH.md     # Secrets, credential isolation & auth policies
│   ├── 02_DATABASE_AND_CMS.md      # Schemas, migrations & headless CMS pipelines
│   ├── 03_DESIGN_AND_ASSETS.md     # CSS tokens, favicons, branding & UI components
│   └── 04_LOGIC_AND_ARCHITECTURE.md# Page routing, business logic & core algorithms
```

---

## 🛠️ Built-in Automation CLI Tools

### 1. Generate Lightweight Repo Map
Extracts top-level symbols (functions, classes, exports) within a token budget without overloading context windows:
```bash
python scripts/generate_repo_map.py .
```

### 2. Verify Pre-Commit Safety & Secret Leakage
Scans staged files to ensure no credentials (`service_account.json`, `.env`, `.pem`) are ever exposed:
```bash
python scripts/verify_changes.py
```

### 3. 1-Click Pre-Commit Hook Installation
```bash
python scripts/install_hook.py
```

---

## 🤝 Contributing
Contributions, feature requests, and issue discussions are welcome!
1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'feat: add automated pillar verification'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📄 License
Distributed under the **MIT License**. Free and open for everyone — developers, students, and autonomous agents alike.
