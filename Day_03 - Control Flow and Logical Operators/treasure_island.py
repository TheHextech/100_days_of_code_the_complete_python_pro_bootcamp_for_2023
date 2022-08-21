print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# Flowchart of this project here below:
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

# The lower() function will transform the string in lower case
first_move = input('Would you move left or right? ').lower() 

if first_move == 'right':
    print('\nYou met Dracula. Game Over.')

elif first_move == 'left':
    second_move = input('\nWould you swim or wait? ').lower()
    
    if second_move == 'swim':
        print('\nThe river if full of alligators. Game Over.')
    
    elif second_move == 'wait':
        third_move = input('\nWould you open red, blue or yellow door? ').lower()
        if third_move == 'red' or third_move == 'blue':
            print('\nThere was a deadly poison trap! Game Over.')
        
        elif third_move == 'yellow':
            print('\nYou found the legendary jewell! You win!')
    
        else:
            print("\nYou can't digit. You died.")

    else:
        print("\nYou can't digit. You died.")

else:
    print("\nYou can't digit. You died.")
