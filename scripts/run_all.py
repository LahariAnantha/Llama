
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]

scripts = [
    "profile_data.py",
    "clean_data.py",
    "integrate_data.py",
    "initial_analysis.py",
    "initial_visualization.py"
]

for script in scripts:
    subprocess.run(
        [sys.executable, str(root / "scripts" / script)],
        cwd=root,
        check=True
    )

print("Workflow completed successfully!")
