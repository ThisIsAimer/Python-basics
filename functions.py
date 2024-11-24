
def get_todos(filepath="files/Other code/todo.txt"):
    with open(filepath, "r") as _file:
        _items = _file.readlines()
        return _items

def write_todos(items_, filepath = "files/Other code/todo.txt"):
    with open(filepath, "w", ) as _file:  # stores in text file
        _file.writelines(items_)
