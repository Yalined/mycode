#!/usr/bin/env python3
"""Author: Yalined Rohena - Ascii final project"""

import os

def print_ascii(fn):
    f= open(fn,'r')
    print(''.join([line for line in f]))

while True:
    print_ascii('menuascii.txt')

    choice = input("""
    Here are the top movies from the 2010's each year. Choose any movie you would like to read fun facts about. Choose by entering the number from the list and hit 'enter'. Press 'q' to quit.

    1. ๐ ๐พ ๐   ๐ ๐ ๐พ ๐ ๐  3 (2010)

    2. โ๐๐ฃ๐ฃ๐ช โ๐ ๐ฅ๐ฅ๐๐ฃ: ๐ป๐๐๐ฅ๐๐๐ช โ๐๐๐๐ ๐จ๐ค ๐ก๐ฅ. ๐ (2011)

    3. Mแดสแด แดส's Tสแด Aแด แดษดษขแดสs (2012)

    4. ๐โ๐ ๐ป๐ข๐๐๐๐ ๐บ๐๐๐๐ : ๐ถ๐๐ก๐โ๐๐๐ ๐น๐๐๐ (2013)

    5. ๐๐ถ๐ฎ๐ป๐ฒ๐ฌ๐ช๐ท ๐ข๐ท๐ฒ๐น๐ฎ๐ป (2014)

    6. ฯจโฒงโฒ๊ โฒฐโฒ๊๐: โฒโฒฃโฒ๐โฒโฒโฒ ๐ฅโฒโฒ - โฒฆโฒโฒ ๐โฒ๊โฒฅโฒ โฒโฒฑโฒโฒโฒโฒ๐ (2015)

    7. แ๐ฎษขฯโ ใ๏ฌกโ: แฉ โ๐แฏแ แกแฏแโ โ๐แแแธ (2016)

    8. ๐๐๐๐ ๐๐๐๐: ๐ด๐๐๐๐๐๐ ๐๐ธ๐ธ๐ธ - ๐๐๐ ๐ป๐๐๐ ๐น๐๐๐ (๐ธ๐ถ๐ท๐ฝ)

    9. ไนใ้ฉโผ้ฟโๅฐธ้ฉ๐ ใธๅ๐ๅฐบโ(ๅทฑ0ไธจใฅ)

    10.๐ ๐๐พ๐๐๐พ๐๐: ๐ค๐๐ฝ๐๐บ๐๐พ (๐ค๐ข๐ฃ๐ซ)
    """)

    if choice == "1": #toy story 3
        print_ascii('toystoryascii.txt')#print file with ascii art and open file with film info 
        f = open("toystory.txt", "r")
        for x in f:
          print(x, end="")
        input("Press ENTER to return to the main menu")
        os.system("clear")


    if choice == "2": #harry potter
        print_ascii('harrypotterascii.txt') 
        f = open ("harrypotter.txt", "r")
        for x in f:
          print(x, end="")  
        input("Press ENTER to return to the main menu")
        os.system("clear")

    if choice == "3": #Avengers
        print_ascii('avengersascii.txt')
        f = open ("avengers.txt", "r")
        for x in f:
          print(x, end="")
        input("Press ENTER to return to the main menu")
        os.system("clear")

    if choice == "4": #Hunger Games
        print_ascii('hungergamesacii.txt')
        f = open ("hungergames.txt", "r")
        for x in f:
          print(x, end="")
        input("Press ENTER to return to the main menu")
        os.system("clear")
 
    if choice == "5": #American Sniper
        print_ascii('americansniperascii.txt')
        f = open ("americansniper.txt", "r")
        for x in f:
          print(x, end="")
        input("Press ENTER to return to the main menu")
        os.system("clear")

    if choice == "6": #Force Awakens
        print_ascii('starwarsforceascii.txt')
        f = open ("starwarsforce.txt", "r")
        for x in f:
          print(x, end="")
        input("Press ENTER to return to the main menu")
        os.system("clear")

    if choice == "7": #Rogue one
        print_ascii('rogueoneascii.txt')
        f = open ("starwarsrogueone.txt", "r")
        for x in f:
          print(x, end="")
        input("Press ENTER to return to the main menu")
        os.system("clear")

    if choice == "8": #Last Jedi
        print_ascii('starwarsjediascii.txt')
        f = open ("starwarsjedi.txt", "r")
        for x in f:
          print(x, end="")
        input("Press ENTER to return to the main menu")
        os.system("clear")    

    if choice == "9": #Black Panther
        print_ascii('blackpantherascii.txt')
        f = open ("blackpanther.txt", "r")
        for x in f:
          print(x, end="")
        input("Press ENTER to return to the main menu")
        os.system("clear")

    if choice == "10": #Endgame
        print_ascii('endgameascii.txt')
        f = open ("endgame.txt", "r")
        for x in f:
          print(x, end="")
        input("Press ENTER to return to the main menu")
        os.system("clear")    

    elif choice == "q":
        print("Thanks for playing!")
        break
