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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice = input("You see two roads, which one do you choose?\nSelect \"R\" for the one on the right\nSelect \"L\" for the one on the left\n").upper()
if choice=='R':
    ch = input("You see a busy looking street and a dark alley where do you go? \nSelect \"R\" to enter the busy looking street\nSelect \"L\" to enter the dark alley\n").upper()
    if ch=='R':
        print("You've entered the busy looking street.")
        op = input("You are now hungry, do you buy candy from the shop or get it from a kind looking stranger?\nSelect \"R\" to buy it from the shop\nSelect \"L\" to get it from the kind stranger offering it to you\n").upper()
        if op=='R':
            print("Good job, you've now replenished your energy and you can now walk more.\n As you walk around you see a spot marked with an \"x\" symbol let's dig and see what it is.\nYAYY You did it! You've found the treasure")
        else: 
            print("You're eating the candy that you got from the stranger, you can't help but notice that it's tasting weird.\nOh no, you've died and your parts have been sold in the black market! Let this be a lesson not to accept anything from strangers. Try again on your next life.")
    else:
        print("You've entered the dark alley.")
        print("Oh no, Kaneki mistook your face for a ghoul and has killed you, you are now dead. Try again but next time, wear a mask or something.")
else:
    print("You can see an island in the distance\nDo you take a boat over there or can you swim there? ")
    ch = input("Please select \"S\" if you've decided to swim or select \"B\" if you're going to take the boat\n").upper()
    if ch=='B':
        print("You see an island marked by a flag which has a skull wearing a straw hat and another island which looks like a paradise, which do you choose?")
        choo = input("Select \"R\" to land on the straw hat island\nSelect \"L\" to land on the paradise island\n").upper()
        if choo=='R':
            print("Ah, you meet the straw hat pirates. They seem nice, they are adamant on taking you on their next adventure.\n Something along the lines of back up food or something.\nYou never found the treasure. Maybe if you stick around you'll find the one piece with them. If you stay alive that long that is.")
        else:
            print("Ah, you land on the paradise island. It looks really calm, eerily calm even. Oh, what's up with this weird looking insects? Oh wait, no--\nYou were eated by catterpillars which looked human. You are now dead.")
    else:
        print("It's sweet that you think you've got the upper body strength but you gotta be more realistic man. You died trying to reach the island. Your body was eaten by a Kraken.")
