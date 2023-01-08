# How to open in read write mode? => 
with open("words.txt", "r+") as f:
    words = f.read()
    words = words.split()
    for word in words:
        f.write("'%s', " % word)