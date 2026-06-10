import os
import sys

# Ensure the repo root (where logic_utils.py lives) is importable regardless of
# how pytest is invoked (bare `pytest` vs `python -m pytest`).
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
