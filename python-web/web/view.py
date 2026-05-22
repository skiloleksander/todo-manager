import streamlit as st
from controller import render_todo_list

def render_app():
    pg = st.navigation([st.Page("pages/main_window.py", title="Головне вікно")
                        , st.Page("pages/add_todo.py", title="Додати нове завдання")
                        , st.Page("pages/edit_todo.py", title="Редагувати завдання")
                        , st.Page("pages/delete_todo.py", title="Видалити завдання")
                        , st.Page("pages/completed.py", title="Виконані завдання")], position="top")
    pg.run()