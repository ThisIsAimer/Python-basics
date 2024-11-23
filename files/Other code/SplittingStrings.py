user_input = input("please enter your numbers with a ,: ")

our_list = user_input.split(",")

number_list = [float(item) for item in our_list]

addition = 0

for item in number_list:
    addition+=item

print(addition)

