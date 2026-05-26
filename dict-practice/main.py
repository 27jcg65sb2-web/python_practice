with open("memo.txt","r") as f:
    text = f.readline()
    print(text)
with open("output.txt", "w") as f:
    f.write("hello")
