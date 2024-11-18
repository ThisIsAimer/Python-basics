num = int(0)
items = []

string = "bro"
string.upper()


while 3 > num:
    text = input("Add, Show, Edit or End: ")
    text = text.strip().lower()
    match text:
        case "add":
            toDo = input("enter your toDo: ")
            items.append(toDo)
        case "show":
            number = 1
            for item in items:
                print(str(num)+".",item)
                num+=1
        case "edit":
            editNumber = int(input("number of the toDo to edit: "))
            newTodo = input("enter what edited todo: ")
            items[editNumber-1] = newTodo
            print()
        case "end":
            break
        case somethingElse:
            print("invalid error")


