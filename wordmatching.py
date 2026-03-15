def match(words):
    c=0
    l=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            c+=1
            l.append(word)
    print(l)
    return c 
count=match(["aarna","abc","level","xyz"])
print(count)