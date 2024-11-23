user_input = input("please enter your numbers with a ,: ")

string_list = user_input.split(",")

number_list = [float(item) for item in string_list]

addition = 0

for item in number_list:
    addition+=item

print(addition)

