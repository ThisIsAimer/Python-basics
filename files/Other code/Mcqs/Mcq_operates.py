import json

with open("Data.json","r") as file:
    content = file.read()
data = json.loads(content)


for index,items in enumerate(data):
    print( f"Question no {index+1}: {items["question"]}")
    choices = ord("a")
    for item in items["options"]:
        print(f"{chr(choices)}. {item}")
        choices += 1

    user_input = input("enter the option you think is correct: ").lower()
    items["user_input"] = user_input
print("-------------------------------------------------------------------------------")
score = 0
for index,items in enumerate(data):
    print(f"For Question number {index+1}:-")
    print(f"User answer: {items["user_input"]}| correct answer:{items["Correct answer"]}")
    if items["user_input"] == items["Correct answer"]:
        score+=1

print("---------------------------------------------------------------------------------")
print("Number of correct answers is: " , score , " out of: ", index+1)
#:)