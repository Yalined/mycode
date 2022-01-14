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

    1. 🅃 🄾 🅈   🅂 🅃 🄾 🅁 🅈  3 (2010)

    2. ℍ𝕒𝕣𝕣𝕪 ℙ𝕠𝕥𝕥𝕖𝕣: 𝔻𝕖𝕒𝕥𝕙𝕝𝕪 ℍ𝕒𝕝𝕝𝕠𝕨𝕤 𝕡𝕥. 𝟚 (2011)

    3. Mᴀʀᴠᴇʟ's Tʜᴇ Aᴠᴇɴɢᴇʀs (2012)

    4. 𝑇ℎ𝑒 𝐻𝑢𝑛𝑔𝑒𝑟 𝐺𝑎𝑚𝑒𝑠: 𝐶𝑎𝑡𝑐ℎ𝑖𝑛𝑔 𝐹𝑖𝑟𝑒 (2013)

    5. 𝓐𝓶𝓮𝓻𝓲𝓬𝓪𝓷 𝓢𝓷𝓲𝓹𝓮𝓻 (2014)

    6. Ϩⲧⲁꞅ Ⲱⲁꞅ𝛓: Ⲉⲣⲓ𝛓ⲟⲇⲉ 𝓥ⲒⲒ - Ⲧⲏⲉ 𝓕ⲟꞅⲥⲉ Ⲁⲱⲁⲕⲉⲛ𝛓 (2015)

    7. ᖇ𝖮ɢυ∈ 〇ﬡ∈: ᗩ ⟆𝜏Ꭿᖇ ᙡᎯᖇ⟆ ⟆𝜏ᗝᖇႸ (2016)

    8. 𝚂𝚝𝚊𝚛 𝚆𝚊𝚛𝚜: 𝙴𝚙𝚒𝚜𝚘𝚍𝚎 𝚅𝙸𝙸𝙸 - 𝚃𝚑𝚎 𝙻𝚊𝚜𝚝 𝙹𝚎𝚍𝚒 (𝟸𝟶𝟷𝟽)

    9. 乃㇄闩⼕长 尸闩𝓝 〸卄🝗尺 (己0丨〥)

    10.𝖠𝗏𝖾𝗇𝗀𝖾𝗋𝗌: 𝖤𝗇𝖽𝗀𝖺𝗆𝖾 (𝟤𝟢𝟣𝟫)
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
