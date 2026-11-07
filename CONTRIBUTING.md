# Contributing to AgenticSync

Thank you for your interest in contributing to AgenticSync.

## Code of Conduct

Maintain an objective, collaborative, and professional environment. Focus on code quality, security rigor, and architectural clarity.

## Development Workflow

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Implement changes ensuring:
   - Scripts are compatible with Python 3.8+ across Windows, macOS, and Linux.
   - Zero external heavy dependencies (use Python standard library wherever possible).
   - All documentation follows the 4-pillar structure.
4. Run validation before committing:
   ```bash
   python scripts/verify_changes.py
   ```
5. Commit your changes using Conventional Commits:
   ```bash
   git commit -m "feat(mapper): add support for rust and go symbol extraction"
   ```
6. Open a Pull Request with a clear description of the problem solved.
