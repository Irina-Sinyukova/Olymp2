c = 0
for x1 in "КГЗБ"*3:
    for x2 in "КГЗБ"*3:
        for x3 in "КГЗБ"*3:
            for x4 in "КГЗБ"*3:
                for x5 in "КГЗБ"*3:
                    for x6 in "КГЗБ"*3:
                        word = list(x1+x2+x3+x4+x5+x6)
                        if len(set(word)) == 1 and "Б" in word:
                            c+=3
                        if "Б" not in word:
                            c+=1
print(c)