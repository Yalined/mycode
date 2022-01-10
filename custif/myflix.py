#!/usr/bin/env python3
"""Author Yalined Rohena: Using while loop and if logic for Python Basics class"""

round = 0
while True:
    round = round + 1
    print('Do you want to know where you were born in your past life? Reply yes to proceed.')
    answer = input(" Ready!? ")
    if answer == 'yes':
        print('Hell yeah!')
        break
    if answer == 'no':
        print('Oh no... We are still doing it.')


message = 'The country you were born in your past life is '

choice = input("""
What combination of color do you like the most?:

1. red,green,white
2. orange,green,white
3. blue,white
4. red,white
5. blue,white,red
6. yellow,red
7. purple,black,green,pink
""")
if choice == "1": #red/green/white
    message = message + 'Madagascar.'

elif choice == "2": #orange/green/white
    message = message + 'India.'

elif choice == "3": #blue/white
    message = message + 'Greece.'

elif choice == "4": #red/white
    message = message + 'Turkey.'

elif choice == "5": #blue/white/red
    message = message + 'France.'

elif choice == "6": #yellow/red
    message = message + 'Spain.'

else:
    message = 'This is your first life. No past lives found.'
print(message)




