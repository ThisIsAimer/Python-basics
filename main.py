num = int(0)
file = open("todo.txt", "r")
items = file.readlines()
file.close()

string = "bro"
string.upper()


while 3 > num:
    # file = open("todo.txt", "r")
    # items = file.readlines()
    # file.close()

    with open("todo.txt", "r") as file:
        items = file.readlines()


    userInput = input("Add, Show, Edit, Complete or End: ") + "\n"
    userInput = userInput.strip().lower()
    if "add" in userInput:
            toDo = userInput[4:]


            items.append(toDo)
            with open("todo.txt", "w",) as file:  # stores in text file
                file.writelines(items)

            # file = open("todo.txt","a") # also works
            # items = file.readlines()
            # items.append(toDo)
            # file.writelines(toDo)
            # file.close()
    elif "show" in userInput:
            newItems = [item.strip("\n") for item in items]
            #enumerate makes the items in a list and assigns them number
            for index,item in enumerate(newItems):
                print(f"{index+1}. {item}")

    elif "edit" in userInput:
            number = int(input("number of the toDo to edit: "))
            newTodo = input("enter what edited todo: ")+"\n"
            items[number-1] = newTodo

            with open("todo.txt", "w", ) as file:
                file.writelines(items)

    elif "complete" in userInput:
            number = int(input("enter the number of ToDo to complete: "))

            itemToRemove  = items[number-1].strip("\n")
            items.remove(items[number-1]) #can also use pop with index number

            with open("todo.txt", "w", ) as file:
                file.writelines(items)

            print(f"the task, '{itemToRemove}' has beem removed from the todo list")

    elif "end" in userInput:
            break
    else :
            print("invalid error")


