word = "dhiraj"
l = len(word)
i = 0
while(i<l):
    sam = word[i]
    word[i] = word[l-1]
    word[l] = sam
    i+=1
    l=l-1
print(word)
