# streamlit run web.py to run this
import streamlit as web
import functions

todos = functions.get_todos()

web.title("My ToDo App")
web.subheader("this is my todo list")
web.write("\n")


for todo in todos:
    web.checkbox(todo)

web.text_input(label="",placeholder="add a new todo...")
