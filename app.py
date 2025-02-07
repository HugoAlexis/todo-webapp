import streamlit as st
import functions

def add_todo():
    new_todo = st.session_state['new_todo']
    functions.add_todo(todos, new_todo)
    st.session_state['new_todo'] = ''

def todo_selected():
    for item in st.session_state:
        if not item.startswith('todos_'):
            continue
        if st.session_state[item]:
            index_todo = int(item.removeprefix('todos_'))
            functions.todo_complete(todos, index_todo)

st.title('My todo app')
st.subheader('This is my todo app')

todos = []
functions.load_todos_data(todos)

for i, todo in enumerate(todos):
    st.checkbox(todo, key=f'todos_{i}', on_change=todo_selected)

st.text_input(
    label='New todo: ',
    placeholder='Enter a todo: ',
    key='new_todo',
    on_change=add_todo
)
