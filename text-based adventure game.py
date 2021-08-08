# Text-based adventure game - Viet Hoang Cao 

def game_over():
    print("I'm sorry that you were defeated while this game has not been completed yet so fingers cross for you next time")
game_over()

def treasure_room_1(): # alone 
    print("After all, this game has almost came to an end. However, it is not over yet. After entering the treasure room, a dragon is waiting for you.")
    print("Similar to previous challenges, you have two options to defeat the dragon. 1). Kill it slowly with your bow and arrows or 2). Take full advantage of your special abilities")
    choice_3 = int(input("Which option will you choose to defeat the final boss").strip())
    if choice_3 == 1:
        print("That is a great decision. You have defeated the cold-blooded dragon")
    elif choice_3 == 2:
        print("You have been defeated by the dragon. It is so strong that it is immune to your special abilities")
        game_over()

def treasure_room_2(): # with polar hear 
    print("After all, this game has almost come to an end. However, it is not over yet. After entering the treasure room, a dragon is waiting for you.")
    print("Similar to previous challenges, you have two options to defeat the dragon. 1). Kill it slowly with your bow and arrows and ask the polar bear for help or 2). Take full advantage of your special abilities")
    choice_4 = int(input("Which option will you choose to defeat the final boss? ").strip())
    if choice_4 == 1:
        print("That is a great decision. You have defeated the final boss thanks to the polar bear and your special archery talent")
    elif choice_4 == 2:
        print("You have been defeated by the dragon. It is so strong that it is immune to your special abilities")
        game_over()

def lion_room():
    print("So you have entered the lion room. A lion is sleeping very well at the end of the room")
    print("You have two options. 1). Walk past the lion silently and 2). Kill the lion")
    choice_1 = int(input("Which option will you go for? 1 or 2").strip()) 
    if choice_1 == 1: 
        print("Great choice. The lion can't notice you at all")
        treasure_room_1()
    elif choice_1 == 2:
        print("That's bad luck. The lion has been very hungry over the last few days.")
        game_over()

def tiger_room():
    print("So you have entered the tiger room. A tiger is fighting with a polar bear right at the center of room")
    print("Would you rather: 1). Run quickly across the room? and 2). Help the polar bear by shooting your bow to the tiger?")
    choice_2 = int(input("Which option will you go for ? 1 or 2").strip()) 
    if choice_2 == 1: 
        print("Unfortunately you attract both of them and they kill you.")
        game_over()
    elif choice_2 == 2:
        print("That's an outstanding decision. The polar becomes your loyal companion until the end")
        treasure_room_2()

def main_game():
    print("You are standing in front of two rooms. One is the lion room and the other is the tiger room.")
    room = input("Which door do you want to get inside? ").lower().strip()
    if room == "lion room":
        lion_room()
    elif room == "tiger room":
        tiger_room()

def start_game():
    ready = input("Welcome to my text-based adventure game. Are you ready? ").title().strip()
    if ready == "Yes":
        print("I hope you will have an enjoyable time experiencing my text-based adventure game. Now, let's get the ball rolling. ")
        main_game() 
    elif ready == "No":
        print("Then just take your time to prepare. Don't worry ! ")
    else:
        print("Invalid input. You can only enter yes or no")

while True:
    start_game()
    replay = input("Would you want to try this game again?").lower().strip()
    if replay == "yes":
        continue
    elif replay == "no":
        print("Thank you very much for playing. See you next time ")
        break