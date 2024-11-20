num = int(0)
file = open("todo.txt", "r")
items = file.readlines()
file.close()

string = "bro"
string.upper()


while 3 > num:
    file = open("todo.txt", "r")
    items = file.readlines()
    file.close()
    text = input("Add, Show, Edit, Complete or End: ")+"\n"
    text = text.strip().lower()
    match text:
        case "add":
            toDo = input("enter your toDo: ")+"\n"


            items.append(toDo)
            file = open("todo.txt", "w",)  # stores in text file
            file.writelines(items)
            file.close()

            # file = open("todo.txt","a") # also works
            # items = file.readlines()
            # items.append(toDo)
            # file.writelines(toDo)
            # file.close()
        case "show":
            newItems = [item.strip("\n") for item in items]
            #enumerate makes the items in a list and assigns them number
            for index,item in enumerate(newItems):
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


