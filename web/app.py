import sys
from pathlib import Path
import streamlit as st

sys.path.append(str(Path(__file__).parent.parent))

from view import render_app
from core import load_todo

def main():
    Path("data").mkdir(exist_ok=True)
    load_todo()
    render_app()

if __name__ == "__main__":
    main()