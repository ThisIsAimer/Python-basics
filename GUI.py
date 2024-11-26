import  functions
import FreeSimpleGUI as Gui

label = Gui.Text("Type in a To-Do")
input_box = Gui.InputText(tooltip="Enter to do")
add_button = Gui.Button("Add")

window = Gui.Window("My To-Do App", layout=[[label], [input_box, add_button]])
window.read()# it displays the window
window.close()