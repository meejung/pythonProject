print('============= Welcome! To hockey equipment store! =============')

print("""
==========================================
1. equipments(player)
2. add equipments(player)
3. delete equipments(player)
4. equipments(goalie)
5. add equipments(goalie)
6. delete equipments(goalie)
7. stop and return to the home
==========================================
""")

player = ['Hockey stick','Hockey jersy','Hockey shoulder pads','Hockey elbow pads','Hockey pants','Hockey gloves','hockey shinguard','skates','helmet']
goalie = ['Hockey mask','Hockey shoulder pads','Hockey blocker','Hockey catcher','Hockey leg pads','Hockey skate','Hockey stick',]
while True:
    number = int(input("Click the button that you want to see!"))

    if number == 1:
        print("================================equipment(player)==============================================")
        for i in player:
            print(i)
        print("==============================================================================")
    elif number == 2:
        add_player = input("Write a equipment that your ganna add.")
        player.append(add_player)

    elif number == 3:
        remove_player = input("Write a menu that your ganna remove.")
        player.remove(remove_player)

    elif number == 4:
        print("================================equipment(goalie)==============================================")
        for u in goalie:
            print(u)
        print("==============================================================================")

    elif number == 5:
        add_goalie = input("Write a equipment that your ganna add.")
        player.append(add_goalie)


    elif number == 6:
        remove_goalie = input("Write a menu that your ganna remove.")
        player.remove(remove_goalie)

    elif number == 7:
        print('END')
        break

    else:
        print("The number doesn't exit....   'Please try a diffrent number.'")
