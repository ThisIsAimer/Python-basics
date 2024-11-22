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

    print("---------------------------------------------------------")
    userInput = input("Add, Show, Edit, Complete or End: ")
    userInput = userInput.strip().lower()
    if userInput.startswith("add"):
            toDo = userInput[4:]


            items.append(toDo + "\n")
            with open("todo.txt", "w",) as file:  # stores in text file
                file.writelines(items)

            # file = open("todo.txt","a") # also works
            # items = file.readlines()
            # items.append(toDo)
            # file.writelines(toDo)
            # file.close()
    elif userInput.startswith("show"):
            newItems = [item.strip("\n") for item in items]
            #enumerate makes the items in a list and assigns them number
            for index,item in enumerate(newItems):
                print(f"{index+1}. {item}")

    elif userInput.startswith("edit"):
        try:
            number = int(userInput[5:])
            newTodo = input("enter what edited todo: ")+"\n"
            items[number-1] = newTodo

            with open("todo.txt", "w", ) as file:
                file.writelines(items)
        except ValueError:
            print("____________________invalid______________________")
            print("please put the task number after 'edit'")
            continue
        except IndexError:
            print("____________________invalid______________________")
            print("The index you provided is invalid!")
            continue

    elif userInput.startswith("complete"):
        try:
            number = int(int(userInput[9:]))

            itemToRemove  = items[number-1].strip("\n")
            items.remove(items[number-1]) #can also use pop with index number

            with open("todo.txt", "w", ) as file:
                file.writelines(items)

            print(f"the task, '{itemToRemove}' has beem removed from the todo list")
        except ValueError:
            print("____________________invalid______________________")
            print("please put the task number after 'complete'")
            continue
        except IndexError:
            print("____________________invalid______________________")
            print("The index you provided is invalid!")
            continue

    elif userInput.startswith("end"):
            break
    else :
            print("invalid error")


