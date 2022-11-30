import os
def start(listofwords):
    solve(listofwords)

def solve(listofwords):
    os.system("cls")
    firsttry = input("Enter your first attempt (do NOT use words with the same letter in multiple times!):    ")
    dontuselist = []
    word2 = 0
    word3 = 0
    word4 = 0
    word5 = 0
    word6 = 0
    perfword = []
    specific = {}
    screen(firsttry,word2,word3,word4,word5,word6,perfword)
    val1 = int(input())
    numdone = 0
    arein = []
    while numdone < 5:
        specific[numdone] = 0
        numdone +=1
    numdone = 0
    while numdone < 5:
        if str(val1)[numdone] == "1":
            perfword.append(firsttry[numdone])
        elif str(val1)[numdone] =="3":
            dontuselist+=firsttry[numdone]
            perfword.append("?")
        elif str(val1)[numdone] == "2":
            perfword.append("?")
            arein.append(firsttry[numdone])
            specific[numdone] = firsttry[numdone]
        numdone +=1
    tmpnumdone = 0
    tmpposcheck = []
    figuredletters = 0
    for x in perfword:
        if x == "?":
            pass
        else:
            figuredletters+=1
    for x in perfword:
        if x == "?":
            pass
        else:
            for x2 in listofwords:
                tmpfig = 0
                numdone = 0
                while numdone < 5:
                    if x2[numdone] == perfword[numdone]:
                        if x2 in tmpposcheck:
                            pass
                        else:
                            tmpfig +=1
                    numdone +=1
                if tmpfig == figuredletters:
                    tmpposcheck.append(x2)
        tmpnumdone +=1
    if tmpposcheck != []:
        listofwords = tmpposcheck
    tmpprobable = []
    no = {}
    for x in listofwords:
        no[str(x).replace("'","")] = 0
        for y in dontuselist:
            if y in x:
                no[str(x).replace("'","")] +=1
        if no[str(x).replace("'","")] == 0:
            if not x in tmpprobable:
                tmpprobable.append(x)
    if tmpprobable != []:
        listofwords = tmpprobable
    tmpprobable = []
    no = {}
    numtodo = 0
    for y in arein:
        numtodo+=1
    for x in listofwords:
        no[str(x).replace("'","")] = 0
        for y in arein:
            if y in x:
                no[str(x).replace("'","")] +=1
        if no[str(x).replace("'","")] >= numtodo:
            if not x in tmpprobable:
                tmpprobable.append(x)
    if tmpprobable != []:
        listofwords = tmpprobable
    tmpprobable = []
    no = {}
    for x in listofwords:
        no[x]=0
        numdone = 0
        while numdone<5:
            if x[numdone] != specific[numdone]:
                no[x]+=1
            numdone+=1
        if no[x] == 5:
            tmpprobable.append(x)
    if tmpprobable != []:
        listofwords = tmpprobable
    print("All possible answers written to tmp.txt, pick one!")
    open("tmp.txt","w").write(str(listofwords).replace(",","\n").replace("['","").replace("']","").replace("'\n '","\n"))
    word2 = input("Enter a possible word:    ")
    screen(firsttry,word2,word3,word4,word5,word6,perfword)
    val2 = int(input())
    numdone = 0
    specific = {}
    while numdone < 5:
        specific[numdone] = 0
        numdone +=1
    numdone = 0
    while numdone < 5:
        if str(val2)[numdone] == "1":
            perfword[numdone] = word2[numdone]
        elif str(val2)[numdone] =="3":
            dontuselist+=word2[numdone]
            perfword[numdone]="?"
        elif str(val2)[numdone] == "2":
            perfword[numdone]="?"
            if not word2[numdone] in arein:
                arein.append(word2[numdone])
            specific[numdone] = word2[numdone]
        numdone +=1
    tmpnumdone = 0
    tmpposcheck = []
    figuredletters = 0
    for x in perfword:
        if x == "?":
            pass
        else:
            figuredletters+=1
    for x in perfword:
        if x == "?":
            pass
        else:
            for x2 in listofwords:
                tmpfig = 0
                numdone = 0
                while numdone < 5:
                    if x2[numdone] == perfword[numdone]:
                        if x2 in tmpposcheck:
                            pass
                        else:
                            tmpfig +=1
                    numdone +=1
                if tmpfig == figuredletters:
                    tmpposcheck.append(x2)
        tmpnumdone +=1
    if tmpposcheck != []:
        listofwords = tmpposcheck
    tmpprobable = []
    no = {}
    for x in listofwords:
        no[str(x).replace("'","")] = 0
        for y in dontuselist:
            if y in x:
                no[str(x).replace("'","")] +=1
        if no[str(x).replace("'","")] == 0:
            if not x in tmpprobable:
                tmpprobable.append(x)
    if tmpprobable != []:
        listofwords = tmpprobable
    tmpprobable = []
    no = {}
    numtodo = 0
    for y in arein:
        numtodo+=1
    for x in listofwords:
        no[str(x).replace("'","")] = 0
        for y in arein:
            if y in x:
                no[str(x).replace("'","")] +=1
        if no[str(x).replace("'","")] >= numtodo:
            if not x in tmpprobable:
                tmpprobable.append(x)
    if tmpprobable != []:
        listofwords = tmpprobable
    tmpprobable = []
    no = {}
    for x in listofwords:
        no[x]=0
        numdone = 0
        while numdone<5:
            if x[numdone] != specific[numdone]:
                no[x]+=1
            numdone+=1
        if no[x] == 5:
            tmpprobable.append(x)
    if tmpprobable != []:
        listofwords = tmpprobable
    print(f"All possible answers written to tmp.txt, pick one!")
    open("tmp.txt","w").write(str(listofwords).replace(",","\n").replace("['","").replace("']","").replace("'\n '","\n"))
    word3 = input("Enter a possible word:    ")
    screen(firsttry,word2,word3,word4,word5,word6,perfword)
    val2 = int(input())
    numdone = 0
    specific = {}
    while numdone < 5:
        specific[numdone] = 0
        numdone +=1
    numdone = 0
    while numdone < 5:
        if str(val2)[numdone] == "1":
            perfword[numdone] = word3[numdone]
        elif str(val2)[numdone] =="3":
            dontuselist+=word3[numdone]
            perfword[numdone]="?"
        elif str(val2)[numdone] == "2":
            perfword[numdone]="?"
            if not word3[numdone] in arein:
                arein.append(word3[numdone])
            specific[numdone] = word3[numdone]
        numdone +=1
    tmpnumdone = 0
    tmpposcheck = []
    figuredletters = 0
    for x in perfword:
        if x == "?":
            pass
        else:
            figuredletters+=1
    for x in perfword:
        if x == "?":
            pass
        else:
            for x2 in listofwords:
                tmpfig = 0
                numdone = 0
                while numdone < 5:
                    if x2[numdone] == perfword[numdone]:
                        if x2 in tmpposcheck:
                            pass
                        else:
                            tmpfig +=1
                    numdone +=1
                if tmpfig == figuredletters:
                    tmpposcheck.append(x2)
        tmpnumdone +=1
    if tmpposcheck != []:
        listofwords = tmpposcheck
    tmpprobable = []
    no = {}
    for x in listofwords:
        no[str(x).replace("'","")] = 0
        for y in dontuselist:
            if y in x:
                no[str(x).replace("'","")] +=1
        if no[str(x).replace("'","")] == 0:
            if not x in tmpprobable:
                tmpprobable.append(x)
    if tmpprobable != []:
        listofwords = tmpprobable
    tmpprobable = []
    no = {}
    numtodo = 0
    for y in arein:
        numtodo+=1
    for x in listofwords:
        no[str(x).replace("'","")] = 0
        for y in arein:
            if y in x:
                no[str(x).replace("'","")] +=1
        if no[str(x).replace("'","")] >= numtodo:
            if not x in tmpprobable:
                tmpprobable.append(x)
    if tmpprobable != []:
        listofwords = tmpprobable
    tmpprobable = []
    no = {}
    for x in listofwords:
        no[x]=0
        numdone = 0
        while numdone<5:
            if x[numdone] != specific[numdone]:
                no[x]+=1
            numdone+=1
        if no[x] == 5:
            tmpprobable.append(x)
    if tmpprobable != []:
        listofwords = tmpprobable
    print(f"All possible answers written to tmp.txt, pick one!")
    open("tmp.txt","w").write(str(listofwords).replace(",","\n").replace("['","").replace("']","").replace("'\n '","\n"))
    word4 = input("Enter a possible word:    ")
    screen(firsttry,word2,word3,word4,word5,word6,perfword)
    val2 = int(input())
    numdone = 0
    specific = {}
    while numdone < 5:
        specific[numdone] = 0
        numdone +=1
    numdone = 0
    while numdone < 5:
        if str(val2)[numdone] == "1":
            perfword[numdone] = word4[numdone]
        elif str(val2)[numdone] =="3":
            dontuselist+=word4[numdone]
            perfword[numdone]="?"
        elif str(val2)[numdone] == "2":
            perfword[numdone]="?"
            if not word4[numdone] in arein:
                arein.append(word4[numdone])
            specific[numdone] = word4[numdone]
        numdone +=1
    tmpnumdone = 0
    tmpposcheck = []
    figuredletters = 0
    for x in perfword:
        if x == "?":
            pass
        else:
            figuredletters+=1
    for x in perfword:
        if x == "?":
            pass
        else:
            for x2 in listofwords:
                tmpfig = 0
                numdone = 0
                while numdone < 5:
                    if x2[numdone] == perfword[numdone]:
                        if x2 in tmpposcheck:
                            pass
                        else:
                            tmpfig +=1
                    numdone +=1
                if tmpfig == figuredletters:
                    tmpposcheck.append(x2)
        tmpnumdone +=1
    if tmpposcheck != []:
        listofwords = tmpposcheck
    tmpprobable = []
    no = {}
    for x in listofwords:
        no[str(x).replace("'","")] = 0
        for y in dontuselist:
            if y in x:
                no[str(x).replace("'","")] +=1
        if no[str(x).replace("'","")] == 0:
            if not x in tmpprobable:
                tmpprobable.append(x)
    if tmpprobable != []:
        listofwords = tmpprobable
    tmpprobable = []
    no = {}
    numtodo = 0
    for y in arein:
        numtodo+=1
    for x in listofwords:
        no[str(x).replace("'","")] = 0
        for y in arein:
            if y in x:
                no[str(x).replace("'","")] +=1
        if no[str(x).replace("'","")] >= numtodo:
            if not x in tmpprobable:
                tmpprobable.append(x)
    if tmpprobable != []:
        listofwords = tmpprobable
    tmpprobable = []
    no = {}
    for x in listofwords:
        no[x]=0
        numdone = 0
        while numdone<5:
            if x[numdone] != specific[numdone]:
                no[x]+=1
            numdone+=1
        if no[x] == 5:
            tmpprobable.append(x)
    if tmpprobable != []:
        listofwords = tmpprobable
    print(f"All possible answers written to tmp.txt, pick one!")
    open("tmp.txt","w").write(str(listofwords).replace(",","\n").replace("['","").replace("']","").replace("'\n '","\n"))
    word5 = input("Enter a possible word:    ")
    screen(firsttry,word2,word3,word4,word5,word6,perfword)
    val2 = int(input())
    numdone = 0
    while numdone < 5:
        specific[numdone] = 0
        numdone +=1
    numdone = 0
    while numdone < 5:
        if str(val2)[numdone] == "1":
            perfword[numdone] = word5[numdone]
        elif str(val2)[numdone] =="3":
            dontuselist+=word5[numdone]
            perfword[numdone]="?"
        elif str(val2)[numdone] == "2":
            perfword[numdone]="?"
            if not word5[numdone] in arein:
                arein.append(word5[numdone])
            specific[numdone]=word5[numdone]
        numdone +=1
    tmpnumdone = 0
    tmpposcheck = []
    figuredletters = 0
    for x in perfword:
        if x == "?":
            pass
        else:
            figuredletters+=1
    for x in perfword:
        if x == "?":
            pass
        else:
            for x2 in listofwords:
                tmpfig = 0
                numdone = 0
                while numdone < 5:
                    if x2[numdone] == perfword[numdone]:
                        if x2 in tmpposcheck:
                            pass
                        else:
                            tmpfig +=1
                    numdone +=1
                if tmpfig == figuredletters:
                    tmpposcheck.append(x2)
        tmpnumdone +=1
    if tmpposcheck != []:
        listofwords = tmpposcheck
    tmpprobable = []
    no = {}
    for x in listofwords:
        no[str(x).replace("'","")] = 0
        for y in dontuselist:
            if y in x:
                no[str(x).replace("'","")] +=1
        if no[str(x).replace("'","")] == 0:
            if not x in tmpprobable:
                tmpprobable.append(x)
    if tmpprobable != []:
        listofwords = tmpprobable
    tmpprobable = []
    no = {}
    numtodo = 0
    for y in arein:
        numtodo+=1
    for x in listofwords:
        no[str(x).replace("'","")] = 0
        for y in arein:
            if y in x:
                no[str(x).replace("'","")] +=1
        if no[str(x).replace("'","")] >= numtodo:
            if not x in tmpprobable:
                tmpprobable.append(x)
    if tmpprobable != []:
        listofwords = tmpprobable
    tmpprobable = []
    no = {}
    for x in listofwords:
        no[x]=0
        numdone = 0
        while numdone<5:
            if x[numdone] != specific[numdone]:
                no[x]+=1
            numdone+=1
        if no[x] == 5:
            tmpprobable.append(x)
    if tmpprobable != []:
        listofwords = tmpprobable
    print(f"All possible answers written to tmp.txt, pick one!")
    open("tmp.txt","w").write(str(listofwords).replace(",","\n").replace("['","").replace("']","").replace("'\n '","\n"))
    num = 0
    for x in listofwords:
        num+=1
    input(f"No more can be discovered, you have a {(1/num)*100}% chance to guess!")
                                
        
def screen(firsttry,word2,word3,word4,word5,word6,perfword):
    os.system("cls")
    print(""" _____         _                    
/  ___|       | |                   
\ `--.   ___  | |__   __  ___  _ __ 
 `--. \ / _ \ | |\ \ / / / _ \| '__|
/\__/ /| (_) || | \ V / |  __/| |   
\____/  \___/ |_|  \_/   \___||_|  """)
    print("\n            =========")
    print(f"            | {firsttry} |")
    if word2 == 0:
        print("            | ????? |")
    else:
        print(f"            | {word2} |")
    if word3 == 0:
        print("            | ????? |")
    else:
        print(f"            | {word3} |")
    if word4 == 0:
        print("            | ????? |")
    else:
        print(f"            | {word4} |")
    if word5 == 0:
        print("            | ????? |")
    else:
        print(f"            | {word5} |")
    if word6 == 0:
        print("            | ????? |")
    else:
        print(f"            | {word6} |")
    print("            =========\n")
    a = """word = '_perfword_'""".replace("_perfword_",str(perfword)).replace("', '","").replace("['","").replace("']","").replace("[]","?????")
    print(a)
    print("\nTry using main.py on tmp.txt to find the best word to use!(do NOT use words with the same letter in multiple times!)")
    print("\n1 = Letter in the correct place\n2 = Letter in the wrong place\n3 = Letter not used\n\nPlease enter the respective numbers (e.g. 12323):")
    
    



'''a = int(input("Would you rather be shown words:\n[1] More likely to be correct\n[2] More likely to give letters\nChoice(1/2):    "))
if a == 1:
    listofwords = open(".\\data\\sorted\\correct.json","r")
elif a == 2:
    listofwords = open(".\\data\\sorted\\positive.json","r")
else:
    quit()'''
listofwords = open("all5letterwords2.txt","r")
listofwords = listofwords.read()
listofwords = listofwords.split("\n")
start(listofwords)
