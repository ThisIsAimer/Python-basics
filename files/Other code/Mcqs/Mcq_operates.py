import json

with open("Data.json","r") as file:
    content = file.read()
data = json.loads(content)

for items in data:
    print( items["question"])
    for index, item in enumerate(items["options"]):
        print(index+1, f" {item}")

    user_input = int(input("enter the option number you find correct: "))
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