from dialogue import welcome_statement
from UI import main_menu
from data import new_game
from level1 import level1

running = True
posCounter = 0

while running == True:
    if posCounter == 0:
        print(main_menu)
        posCounter += 1
    user_input = input('--->')
    if 'l'in user_input:
        print('loading')
        posCounter += 1
    elif 'n' in user_input:
         with open("savegame.json", "w") as file:
            file.write(new_game)
            posCounter += 1
    if posCounter == 2:
        level1()