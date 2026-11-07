#!/usr/bin/env python3
"""
generate_repo_map.py - Lightweight Repository Map & Symbol Outline Generator
Inspired by Aider's repomap.py architecture.
Extracts file tree and top-level definitions (functions, classes, exports) within a token budget.
"""

import os
import re
import sys

# Ensure UTF-8 output encoding across Windows/Linux terminals
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

IGNORE_DIRS = {
    ".git", "node_modules", "dist", "build", ".sanity", "__pycache__", 
    ".vscode", ".idea", "coverage", ".next", ".cache"
}

IGNORE_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".webp", ".svg", ".woff", 
    ".woff2", ".ttf", ".eot", ".mp4", ".pdf", ".zip", ".tar", ".gz"
}

def extract_symbols(file_path):
    symbols = []
    ext = os.path.splitext(file_path)[1].lower()
    
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
    except Exception:
        return symbols

    if ext in [".js", ".jsx", ".ts", ".tsx", ".mjs"]:
        fn_pattern = re.compile(r"^\s*(?:export\s+)?(?:async\s+)?function\s+([A-Za-z0-9_$]+)\s*\(")
        const_fn_pattern = re.compile(r"^\s*(?:export\s+)?const\s+([A-Za-z0-9_$]+)\s*=\s*(?:async\s*)?\(")
        class_pattern = re.compile(r"^\s*(?:export\s+)?class\s+([A-Za-z0-9_$]+)")
        for line in lines:
            m = fn_pattern.match(line) or const_fn_pattern.match(line)
            if m:
                symbols.append(f"fn {m.group(1)}()")
            c = class_pattern.match(line)
            if c:
                symbols.append(f"class {c.group(1)}")

    elif ext == ".py":
        py_def = re.compile(r"^\s*(?:async\s+)?def\s+([A-Za-z0-9_]+)\s*\(")
        py_class = re.compile(r"^\s*class\s+([A-Za-z0-9_]+)")
        for line in lines:
            d = py_def.match(line)
            if d:
                symbols.append(f"def {d.group(1)}()")
            c = py_class.match(line)
            if c:
                symbols.append(f"class {c.group(1)}")

    return symbols[:8]  # Limit to top 8 symbols per file for token budget

def build_repo_map(root_dir="."):
    lines = ["# 🗺️ Repository Map & Symbol Outline", ""]
    
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith(".")]
        level = root.replace(root_dir, "").count(os.sep)
        indent = "  " * level
        folder_name = os.path.basename(root) or root_dir
        
        if root != root_dir:
            lines.append(f"{indent}📁 **{folder_name}/**")
            
        sub_indent = "  " * (level + 1)
        for file in sorted(files):
            ext = os.path.splitext(file)[1].lower()
            if ext in IGNORE_EXTENSIONS:
                continue
            file_path = os.path.join(root, file)
            symbols = extract_symbols(file_path)
            sym_str = f" `[{', '.join(symbols)}]`" if symbols else ""
            lines.append(f"{sub_indent}📄 {file}{sym_str}")
            
    return "\n".join(lines)

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    print(build_repo_map(target))
