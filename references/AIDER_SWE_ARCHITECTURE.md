# 📚 Reference: Aider, SWE-agent & MetaGPT Architecture Deep-Dive

This document details the exact engineering mechanisms utilized by the world's leading open-source agent frameworks and how `agentic-repo-tracker` incorporates them.

---

## 1. Aider: The Git-First Autonomous Pair Programmer
- **Repository:** `paul-gauthier/aider`
- **Core Innovation:**
  - **Tree-sitter AST Symbol Graph:** Generates an Abstract Syntax Tree of the repository to identify class definitions, function signatures, and method references.
  - **Personalized PageRank:** Calculates symbol centrality based on the files currently active in conversation, giving the LLM global context within a strict ~1,000–2,000 token budget.
  - **Atomic Commits & Conventional Messages:** Automatically generates clear commit messages describing code diffs.
  - **Self-Healing Test Loops (`--auto-test` / `--auto-lint`):** Executes lint and test commands after changes; if errors occur, captures stdout/stderr and prompts the LLM to fix its own mistakes autonomously.

---

## 2. SWE-agent: Trajectory-Driven Issue Solving
- **Repository:** `princeton-nlp/SWE-agent`
- **Core Innovation:**
  - **Agent-Computer Interface (ACI):** Tailors command-line interaction specifically for LLMs with custom search, file inspection, and targeted replacement tools.
  - **Trajectory Logging (`.traj` files):** Records every step: `Observation` (environment output) $\rightarrow$ `Thought` (internal chain-of-thought) $\rightarrow$ `Action` (tool call).
  - **Error Isolation:** Intercepts command failures without polluting the core context, enabling iterative recovery.

---

## 3. MetaGPT: Multi-Agent SOP Workflows
- **Repository:** `geekan/MetaGPT`
- **Core Innovation:**
  - **Standard Operating Procedures (SOPs):** Mimics a full software development team by establishing clear intermediate artifacts: PRD (Requirements) $\rightarrow$ System Architecture $\rightarrow$ Task Decomposition $\rightarrow$ Code Implementation.
  - **Structured Documentation:** Enforces that every project maintains living documentation files that update as the codebase matures.

---

## 4. How `agentic-repo-tracker` Unifies These Systems
By combining Aider's repository mapping, SWE-agent's self-healing trajectory loop, and user-defined 4-pillar modularization (Security, CMS/DB, UI/CSS, Logic), any AI agent can handle complex legacy repositories cleanly and reliably.
