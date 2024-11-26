import FreeSimpleGUI as Gui


text1 = Gui.Text("Select files to compress: ")
label1 = Gui.Input()
button1 = Gui.FilesBrowse("choose")

text2 = Gui.Text("Select destination folder: ")
label2 = Gui.Input()
button2 = Gui.FolderBrowse("choose")

convert = Gui.Button("convert")

window = Gui.Window("File compressor", layout= [[text1,label1,button1],[text2,label2,button2],[convert]])

window.read()
window.close()