import streamlit as st
import functions

todos = functions.loadTodos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.saveTodos(todos)
    

st.title("My Todo App")
st.subheader("This is my app")



st.write("This app is to increase your productivity.")

for todo in todos:
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(todos.index(todo))
        functions.saveTodos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...",on_change=add_todo, key="new_todo")

st.session_state