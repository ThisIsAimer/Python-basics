import csv

with open("temperatures.csv","r") as file:
    data = list(csv.reader(file))

place = input("enter the name of the city: ")

for row in data[1:]:
    if row[0] == place:
        print("temperature: ", row[1])