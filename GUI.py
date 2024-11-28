import  functions
import FreeSimpleGUI as Gui

todos = functions.get_todos()
label = Gui.Text("Type in a To-Do")
input_box = Gui.InputText(tooltip="Enter to do",key="todo")
add_button = Gui.Button("Add")
list_box = Gui.Listbox(values=todos,key="todos",enable_events=True,size=(45,7))
edit_button = Gui.Button("Edit")
complete_button = Gui.Button("Complete")
exit_button = Gui.Button("Exit")

window = Gui.Window("My To-Do App", layout=[[label], [input_box, add_button],[list_box,edit_button,complete_button],[exit_button]],font=("Helvetica",10))
while True:
    todos = functions.get_todos()
    event,value = window.read()# it displays the window
    #window can be used to access everything in the programme and update it

    print(event)
    print(value)
    match event:
        case "Add":
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(todos)

        case "Edit":
            edited_todo = value["todos"][0]
            index = todos.index(edited_todo)
            new_todo = value["todo"]
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(todos)

        case "todos":
            window["todo"].update(value= value["todos"][0])

        case "Complete":
            complete_todo = value["todos"][0]
            index = todos.index(complete_todo)
            todos.remove(complete_todo)
            functions.write_todos(todos)
            window["todos"].update(todos)
            window["todo"].update(value="")

        case "Exit":
            break

        case Gui.WIN_CLOSED:
            break

window.close()