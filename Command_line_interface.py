from time import strftime

from functions import *
import time

now = strftime("%b %d %Y, %H:%M:%S")

print("it is:- " + now)

while True:
    # file = open("todo.txt", "r")
    # items = file.readlines()
    # file.close()

    items = get_todos()
    print("---------------------------------------------------------")
    userInput = input("Add, Show, Edit, Complete or End: ")
    userInput = userInput.lower()
    if userInput.startswith("add"):
            toDo = userInput[4:]


            items.append(toDo + "\n")

            write_todos(items)

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

            write_todos(items)

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

            write_todos(items)

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


