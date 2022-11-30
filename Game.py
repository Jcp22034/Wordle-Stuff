from random import choice
import os
redo = 1
def customword():
    os.system("cls")
    word = input("Enter a 5-letter word:    ")
    if len(word) != 5:
        input("Incorrect length!")
        a2 = customword()
    else:
        a2 = word
        return a2
while redo == 1:
    typeplay = input("Do you wish to use:\n\n[1] A specific word\n[2] A random word\n\nChoice:    ")
    if "1" in typeplay:
        word = customword()
    else:
        a = str(open("all5letterwords2.txt","r").read()).split("\n")
        word = choice(a)
    tries = 0
    words = {}
    wordsans = {}
    while tries < 6:
        words[tries] = 0
        tries+=1
    tries = 0
    won = 0
    while tries < 6:
        wordsans[tries] = ""
        words[tries]=input("Enter a guess (No words with repeating letters unless 100% certain!):    ")
        os.system("cls")
        numdone = 0
        while numdone < 5:
            if words[tries][numdone] == word[numdone]:
                wordsans[tries] += "1"
            elif words[tries][numdone] in word:
                wordsans[tries] += "2"
            elif not words[tries][numdone] in word:
                wordsans[tries] +="3"
            numdone +=1
        print(""" _    _                   _  _       
    | |  | |                 | |(_)      
    | |  | |  ___   _ __   __| | _   ___ 
    | |/\| | / _ \ | '__| / _` || | / _ \ 
    \  /\  /| (_) || |   | (_| || ||  __/
     \/  \/  \___/ |_|    \__,_||_| \___|""")
        print("\n           ==================")
        print(f"           | {words[0]} |  {wordsans[0]} |")
        if words[1] == 0:
            print("           | ????? |  ????? |")
        else:
            print(f"           | {words[1]} |  {wordsans[1]} |")
        if words[2] == 0:
            print("           | ????? |  ????? |")
        else:
            print(f"           | {words[2]} |  {wordsans[2]} |")
        if words[3] == 0:
            print("           | ????? |  ????? |")
        else:
            print(f"           | {words[3]} |  {wordsans[3]} |")
        if words[4] == 0:
            print("           | ????? |  ????? |")
        else:
            print(f"           | {words[4]} |  {wordsans[4]} |")
        if words[5] == 0:
            print("           | ????? |  ????? |")
        else:
            print(f"           | {words[5]} |  {wordsans[5]} |")
        print("           ==================\n")
        print("\n1 = Letter in the correct place\n2 = Letter in the wrong place\n3 = Letter not used\n\n")
        if wordsans[tries] == "11111":
            input(f"Correct! Word: {word}")
            won = 1
            tries = 6
        tries +=1
    if won != 1:
        input(f"Failed, word was: {word}")
    val = input("Play Again? y/n:    ")
    if not "y" in val:
        redo = 0
