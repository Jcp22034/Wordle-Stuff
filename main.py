import os

#total words = 14855
#listofwords = open("all5letterwords2.txt","r")
#listofwords = open("tmp.txt","r")

def wordlistchoice():
    choice = input("Would you like to sort words from:\n\n[1] 'all5letterwords2.txt'\n[2] 'tmp.txt' - to help with getting the best answer using the solver\n[3] Custom file - Format: word"+"""\n"""+"\n\nChoice:\n")
    if "1" in choice:
        listofwords = open("all5letterwords2.txt","r")
    elif "2" in choice:
        listofwords = open("tmp.txt","r")
    elif "3" in choice:
        os.system("cls")
        words = input("Drag/Drop file here:    ")
        listofwords = open(words,"r")
    else:
        listofwords = wordlistchoice()
    return listofwords
def start(listofwords,list2,list3):
    makefolders()
    foreachword(listofwords,list2,list3)
def makefolders():
    try:
        os.mkdir("data")
    except:
        pass
    try:
        os.mkdir("data\\sorted")
    except:
        pass

def foreachword(listofwords,list2,list3):
    global totals
    global totalsplace
    global totalsunused
    totals = {}
    totalsplace = {}
    totalsunused = {}
    totalwords = 0
    sortedtotals2 = {}
    sortedtotalsplace2 = {}
    print("Total words sorted:\n")
    for x in listofwords:
        totals[x] = 0
        totalsplace[x] = 0
        totalsunused[x] = 0
        totalwords+=1
    wordsdone = 0
    for x in list3:
        numsdone=0
        for p in list2:
            wordtouse = list2[numsdone]
            numdone = 0
            numdone2 = 0
            correct = 0
            wrongplace = 0
            unused = 0
            correctletters = ""
            while numdone < 5:
                if wordtouse[numdone] == x[numdone2]:
                    correct +=1
                    correctletters +=wordtouse[numdone]
                if wordtouse[numdone] in x:
                    wrongplace +=1
                numdone+=1
                numdone2 +=1
            wrongplace = wrongplace - correct
            unused = 5 - (correct + wrongplace)
            #print(f"Word used: {x}\nWord tried: {wordtouse}\nNumber OF Correct Letters: {correct}\nCorrect Letters: {correctletters}\nLetters in the wrong place: {wrongplace}\nUnused Letters: {unused}\n")
            totals[wordtouse] += correct
            totalsplace[wordtouse] += wrongplace
            totalsunused[wordtouse] += unused
            numsdone +=1
        sortedtotals = dict(sorted(totals.items(), key=lambda x:x[1],reverse = True))
        sortedtotals2[x] = sortedtotals[x]
        sortedtotalsplace = dict(sorted(totalsplace.items(), key=lambda x:x[1],reverse = True))
        sortedtotalsplace2[x] = sortedtotalsplace[x]
        sortedtotalsunused = dict(sorted(totalsunused.items(), key=lambda x:x[1],reverse = True))
        for x in list3:
            try:
                if sortedtotals[x].isdigit():
                    pass
            except:
                sortedtotals[x] = str(sortedtotals[x]) + f"'Avg: {sortedtotals[x]}/{totalwords*5}"
            try:
                if sortedtotalsplace[x].isdigit():
                    pass
            except:
                sortedtotalsplace[x] = str(sortedtotalsplace[x]) + f"'Avg: {sortedtotalsplace[x]}/{totalwords*5}"
            try:
                if sortedtotalsunused[x].isdigit:
                    pass
            except:
                sortedtotalsunused[x] = str(sortedtotalsunused[x]) + f"'Avg: {sortedtotalsunused[x]}/{totalwords*5}"
        wordsdone +=1
        if wordsdone%1000 == 0:
            percentdone = (wordsdone/totalwords)*100
            print(f"{wordsdone}/{totalwords} ({percentdone}%)")
        elif wordsdone == totalwords:
            percentdone = (wordsdone/totalwords)*100
            print(f"{wordsdone}/{totalwords} ({percentdone}%)")
    totalpos= {}
    for x in list3:
        x2 =int(sortedtotals2[x]) + int(sortedtotalsplace2[x])
        totalpos[x] = x2
    sortedtotalpos = dict(sorted(totalpos.items(), key=lambda x:x[1],reverse = True))
    for x in list3:
        try:
            if sortedtotalpos[x].isdigit():
                pass
        except:
            sortedtotalpos[x] = str(sortedtotalpos[x]) + f"'Avg: {sortedtotalpos[x]}/{totalwords*10}"
    print("\nWriting sorted data to files!")
    totalsfile = open("data\\sorted\\correct.json","w")
    totalsfile.write(str(sortedtotals).replace("""", ""","""",
""").replace("'Avg"," Avg"))
    totalsfile.close()
    totalsplacefile = open("data\\sorted\\wrongplace.json","w")
    totalsplacefile.write(str(sortedtotalsplace).replace("""", ""","""",
""").replace("'Avg"," Avg"))
    totalsplacefile.close()
    totalsunusedfile = open("data\\sorted\\unused.json","w")
    totalsunusedfile.write(str(sortedtotalsunused).replace("""", ""","""",
""").replace("'Avg"," Avg"))
    totalsunusedfile.close()
    totalposfile = open("data\\sorted\\positive.json","w")
    totalposfile.write(str(sortedtotalpos).replace("""", ""","""",
""").replace("'Avg"," Avg"))
    totalposfile.close()
    input("\n\nComplete! All words sorted to 'data\\sorted'!")

listofwords2 = wordlistchoice()
listofwords = listofwords2.read()
listofwords = listofwords.split("\n")
listofwords2.close()
list2 = listofwords
list3 = listofwords
start(listofwords,list2,list3)
