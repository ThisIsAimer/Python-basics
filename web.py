# streamlit run web.py to run this
import streamlit as web
import functions



def add_todo():
    new_todo = web.session_state["add_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


todos = functions.get_todos()


web.subheader("")
web.title("The ToDo App")
web.subheader("this app will increase your productivity")


web.text_input(label="",placeholder="add a new todo...",on_change=add_todo,key="add_todo")


for index,todo in enumerate(todos):
    check_box = web.checkbox(todo,key=index)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del web.session_state[index]
        web.rerun()


# web.session_state