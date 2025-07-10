count=0
with open("text.txt") as f:
    data=f.read()
    word=data.split()
    count+=len(word)
    print(count)