filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]

for name in filenames:
    newName = name.replace(".txt","")
    print(newName)