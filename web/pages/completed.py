import streamlit as st
from core import todo
from controller import toggle_task

st.title("Виконані завдання")

has_completed = False

if not todo:
    st.write("Список тудушок порожній.")
else:
    for i, task in enumerate(todo, start=1):
        task_id = task["id"]
        if task.get("is_completed") == True:
            has_completed = True
            label = task["task"]
            if task["type"] == "deadline":
                label += f": {task['deadline']}"
            elif task["type"] == "recurring":
                label += f": {task.get('times_done', 0)}/{task.get('times_total', 0)}"
            st.checkbox(label, value=task["is_completed"], key=f"task_{task_id}", on_change=toggle_task, args=(i, task_id))
    if not has_completed and todo:
        st.write("Немає виконаних завдань.")