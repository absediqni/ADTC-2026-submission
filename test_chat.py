# %%
import os
import sys
from pathlib import Path

# 1. Dynamically find the 'opsmind' root folder even if you are in a subfolder
current_dir = os.getcwd()
while current_dir and not os.path.isdir(os.path.join(current_dir, "src")):
    parent_dir = os.path.dirname(current_dir)
    if parent_dir == current_dir:  # Reached the system root folder
        break
    current_dir = parent_dir

# 2. Load environment variables from .env if present
project_root = Path(current_dir)
if project_root.exists():
    dotenv_path = project_root / ".env"
    if dotenv_path.exists():
        for line in dotenv_path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                os.environ.setdefault(key.strip(), value.strip())

# 3. Inject the correct root path into Python's search paths
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)
    print(f"Added project root to path: {current_dir}")

# 4. Now run your import safely
from src.rag.rag_service import ask_opsmind

question = input("Ask OpsMind a question: ")
answer = ask_opsmind(question)

print("\n")
print(answer)