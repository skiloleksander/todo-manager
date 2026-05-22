import streamlit as st
from controller import add_task
import datetime

st.title("Додати нове завдання")
task = st.text_input("Завдання")
task_type = st.selectbox("Тип завдання", ["Звичайна", "З дедлайном", "Розклад", "Повторювана"])
if task_type == "З дедлайном":
    deadline = st.date_input("Дедлайн")
elif task_type == "Розклад":
    time_start = st.time_input("Початок")
    time_end = st.time_input("Кінець")
elif task_type == "Повторювана":
    times_total = st.number_input("Кількість повторів", min_value=2, step=1)
if st.button("Додати", use_container_width=True):
    if not task.strip():
        st.error("Помилка: Назва завдання не може бути порожньою.")
    else:
        is_valid = True
        if task_type == "Розклад":
            if time_start >= time_end:
                st.error("Помилка: Час закінчення має бути пізніше за час початку.")
                is_valid = False
        elif task_type == "З дедлайном":
            if deadline < datetime.date.today():
                st.error("Помилка: Ви встановлюєте дедлайн, який вже минув.")
                is_valid = False
        if is_valid:
            if task_type == "Звичайна":
                add_task(task, task_type)
            elif task_type == "З дедлайном":
                add_task(task, task_type, deadline = deadline.strftime("%Y-%m-%d"))
            elif task_type == "Розклад":
                add_task(task, task_type, time_start = time_start.strftime("%H:%M"), time_end = time_end.strftime("%H:%M"))
            elif task_type == "Повторювана":
                add_task(task, task_type, times_total = times_total)
            st.toast(f"Завдання {task} успішно додано!")