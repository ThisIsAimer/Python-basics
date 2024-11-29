# streamlit run web.py to run this
import streamlit as web
import functions



def add_todo():
    new_todo = web.session_state["add_todo"]
    todos.append(new_todo+"\n")
    functions.write_todos(todos)

todos = functions.get_todos()


web.subheader("")
web.title("My ToDo App")
web.subheader("this is my todo list")
web.write("\n")


for todo in todos:
    web.checkbox(todo)

web.text_input(label="",placeholder="add a new todo...",on_change=add_todo,key="add_todo")
