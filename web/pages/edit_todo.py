import streamlit as st
from core import todo
from controller import edit_task

task_list = []
for task in todo:
    task_list.append(task["task"])
st.title("Відредагувати завдання")
old_task = st.selectbox("Завдання", task_list)
new_task = st.text_input("Нове завдання")
if st.button("Відредагувати", use_container_width=True):
    if not new_task.strip():
        st.error("Помилка: Нова назва завдання не може бути порожньою.")
    else:
        if old_task == new_task:
            st.error("Помилка: Неможна перевизначити назву завдання саме на себе.")
        else:
            edit_task(old_task, new_task)
            st.toast(f"Завдання {old_task} успішно відредаговано.")