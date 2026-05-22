from core import get_all_todo, complete_todo, create_task, add_todo, edit_todo, delete_todo, clear_todos, todo
import streamlit as st
import os

TASK_TYPE_KEYS = {
    "Звичайна": {
        "key": "1"
    },
    "З дедлайном": {
        "key": "2"
    },
    "Розклад": {
        "key": "3"
    },
    "Повторювана": {
        "key": "4"
    }
}

def toggle_task(index, task_id):
    complete_todo(index)
    task = get_all_todo()[index - 1]
    st.session_state[f"task_{task_id}"] = task["is_completed"]

def render_todo_list():
    if not todo:
        st.write("Список тудушок порожній.")
        return
    for i, task in enumerate(todo, start=1):
        task_id = task["id"]
        label = task["task"]
        if task["type"] == "deadline" and task.get("deadline"):
            label += f": {task['deadline']}"
        elif task["type"] == "schedule":
            label += f": {task.get('time_start', '')} - {task.get('time_end', '')}"
        elif task["type"] == "recurring":
            label += f": {task.get('times_done', 0)}/{task.get('times_total', 0)}"
        if "is_completed" in task and task["is_completed"] == False:
            st.checkbox(label, value=task["is_completed"], key=f"task_{task_id}", on_change=toggle_task, args=(i, task_id))
        elif task["type"] == "schedule":
            st.markdown(f"- {label}")

def add_task(task_title, task_type, **extra):
    task_key = TASK_TYPE_KEYS.get(task_type)
    if task_key is None:
        st.error(f"Невідомий тип завдання: {task_type}")
        return
    task = create_task(task_title, task_key["key"], **extra)
    add_todo(task)
    
def edit_task(old_text, new_text):
    for i in range (1, len(todo) + 1):
        if todo[i-1]["task"] == old_text:
            edit_todo(i, new_text)
            break

def delete_task(target):
    for i in range (1, len(todo) + 1):
        if todo[i-1]["task"] == target:
            delete_todo(i)
            break

def load_todo():
    with os.scandir("data") as entries:
        backups = [entry.name for entry in entries if entry.is_file() and entry.name.startswith("todo_backup_")]
    return backups
