contents = ["how are you today", "where are you today", "what time is it"]
filenames = ["how.txt","where.txt", "what.txt"]

for content, filename in zip(contents,filenames):
    file = open(fr"files\{filename}","w")
    file.write(content)