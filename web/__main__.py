import subprocess
import sys
from pathlib import Path

def main():
    Path("data").mkdir(exist_ok=True)
    app_path = Path(__file__).parent / "app.py"
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", str(app_path)])
    except KeyboardInterrupt:
        print("Завершення роботи...")

if __name__ == "__main__":
    main()