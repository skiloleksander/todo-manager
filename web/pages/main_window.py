import streamlit as st
from controller import render_todo_list, load_todo
from core import clear_todos, backup, load_from_backup, count_todos

st.title("TODO Manager")
col1, col2, col3, col4 = st.columns(4)   
with col1:
    if st.button("Додати", use_container_width=True):
        st.switch_page("pages/add_todo.py")
with col2:
    if st.button("Редагувати", use_container_width=True):
        st.switch_page("pages/edit_todo.py")
with col3:
    if st.button("Видалити", use_container_width=True):
        st.switch_page("pages/delete_todo.py")
with col4:
    with st.popover("Очистити", use_container_width=True):
        st.markdown("Ви точно впевнені, що хочете очистити тудушку?")
        if st.button("Так"):
            clear_todos()
col5, col6, col7 = st.columns([1, 2, 2])
with col5:
    if st.button("Підрахувати", use_container_width=True):
        count = count_todos()
        st.info(f"Всього тудушок {count}.")
with col6:
    if st.button("Резервне копіювання", use_container_width=True):
        backup()
        st.toast("Резервна копія успішно створена.")
with col7:
    with st.popover("Завантажити резервну копію", use_container_width=True):
        backups = load_todo()
        target = st.selectbox("Резервні копії", backups)
        if st.button("Загрузити бекап"):
            load_from_backup(f"data/{target}")
st.divider()
render_todo_list()