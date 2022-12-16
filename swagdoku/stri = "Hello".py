stri = "Hello"
outlst = []
for i in enumerate(stri):
    if i[1] == "l":
        outlst.append(i[0])
print(outlst)
