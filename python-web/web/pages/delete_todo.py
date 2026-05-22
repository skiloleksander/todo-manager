import streamlit as st
from core import todo
from controller import delete_task

task_list = []
for task in todo:
    task_list.append(task["task"])
st.title("Видалити завдання")
target_task = st.selectbox("Завдання", task_list)
with st.popover("Видалити", use_container_width=True):
    st.markdown(f"Ви точно впевнені, що хочете видалити завдання {target_task}?")
    if st.button("Так"):
        delete_task(target_task)
        st.rerun()