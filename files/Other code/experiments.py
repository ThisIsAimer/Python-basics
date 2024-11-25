import glob

myfiles = glob.glob("*.txt")
print(myfiles)

for files in myfiles:
    with open(files,"r") as file:
        print(file.read()+"\n")