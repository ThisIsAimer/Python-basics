import FreeSimpleGUI as Gui
import  zip_function

text1 = Gui.Text("Select files to compress: ")
label1 = Gui.Input()
button1 = Gui.FilesBrowse("choose",key="file")

text2 = Gui.Text("Select destination folder: ")
label2 = Gui.Input()
button2 = Gui.FolderBrowse("choose", key="directory")

convert = Gui.Button("convert",key="convert")

window = Gui.Window("File compressor", layout= [[text1,label1,button1],[text2,label2,button2],[convert]])

while True:
    event,value = window.read()
    print(event)
    file_path = value["file"].split(";")
    folder = value["directory"]
    match event:
        case "convert":
            zip_function.zip_converter(file_path,folder)
        case Gui.WIN_CLOSED:
            break



window.close()