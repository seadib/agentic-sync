# ⚖️ Case Study: Before vs. After Agentic Repo Tracker

This real-world comparison demonstrates why developers and engineering teams star, fork, and adopt this workflow.

---

| Feature / Scenario | ❌ Typical AI Agent (Without Guardrails) | 🟢 With Agentic Repo Tracker |
| :--- | :--- | :--- |
| **Token Usage** | Dumps entire 8,000-line files into context window, running out of tokens or forgetting prior instructions. | Uses `generate_repo_map.py` to feed only class signatures and function outlines (~1,200 tokens). |
| **Security & Secrets** | Blindly commits `.env`, API keys, or `service_account.json` to public GitHub. | `verify_changes.py` automatically blocks commits containing credentials with a pre-commit hook. |
| **Code Architecture** | Adds 500 lines to a single monolithic `app.js` or `style.css` without modularizing. | Enforces **4 Pillars** (Security, Database, Design, Logic) and modular separation. |
| **Change Tracking** | Makes 15 edits without any record, making debugging impossible after 3 turns. | Appends versioned entries (e.g. `[v8.2]`) to the specific pillar change log after every single turn. |
| **Error Recovery** | Hallucinates a fix, introduces syntax errors, and claims "It's working!" | Runs automated syntax/lint commands, catches errors, and self-heals before reporting completion. |
