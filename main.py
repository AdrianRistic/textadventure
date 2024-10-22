from dialogue import welcome_statement
from UI import main_menu

running = True
posCounter = 0

while running == True:
    if posCounter == 0:
        print(main_menu)
        posCounter += 1
user_input = input('--->')