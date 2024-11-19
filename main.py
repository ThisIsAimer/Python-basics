num = int(0)
items = []

string = "bro"
string.upper()


while 3 > num:
    text = input("Add, Show, Edit, Complete or End: ")
    text = text.strip().lower()
    match text:
        case "add":
            toDo = input("enter your toDo: ")
            items.append(toDo)
        case "show":
            # for index, item in items:
            for index,item in enumerate(items):
                print(f"{index+1}. {item}")

        case "edit":
            number = int(input("number of the toDo to edit: "))
            newTodo = input("enter what edited todo: ")
            items[number-1] = newTodo
            print()
        case "complete":
            number = int(input("enter the number of ToDo to complete: "))
            items.remove(items[number-1]) #can also use pop with index number

        case "end":
            break
        case somethingElse:
            print("invalid error")


