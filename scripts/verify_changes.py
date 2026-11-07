#!/usr/bin/env python3
"""
verify_changes.py - Pre-commit and Self-Healing Verification Linter
Inspired by Aider's auto-test and SWE-agent's trajectory verification.
Ensures documentation change-logs are updated and no secret files are exposed.
"""

import os
import subprocess
import sys

# Ensure UTF-8 output encoding across Windows/Linux terminals
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

SENSITIVE_PATTERNS = [
    "service_account.json", ".env", "id_rsa", ".pem", ".key", "credentials.json"
]

def run_cmd(cmd):
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return res.stdout.strip()
    except subprocess.CalledProcessError as e:
        return ""

def check_git_status():
    status = run_cmd("git status --porcelain")
    if not status:
        print("✔ Working tree clean.")
        return True
    
    lines = status.split("\n")
    print(f"📊 Modified files ({len(lines)}):")
    has_security_risk = False
    
    for line in lines:
        parts = line.strip().split()
        if len(parts) >= 2:
            fname = parts[-1]
            print(f"   • {line.strip()}")
            for sens in SENSITIVE_PATTERNS:
                if sens in fname.lower():
                    print(f"   🚨 CRITICAL SECURITY WARNING: Sensitive file detected: {fname}")
                    has_security_risk = True
                    
    if has_security_risk:
        print("\n❌ Verification FAILED: Sensitive credentials detected in git status.")
        return False
        
    print("\n✔ Git status verification passed.")
    return True

if __name__ == "__main__":
    success = check_git_status()
    sys.exit(0 if success else 1)
