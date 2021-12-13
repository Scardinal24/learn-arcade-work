# Final Lab: Education on Zombification

import random


class Character:

    def __init__(self, description, hp, dmg, special, name, room):
        self.description = description
        self.hp = hp
        self.name = name
        self.dmg = dmg
        self.special = special
        self.room = room

class Player:

    def __init__(self, hp, dmg, special):
        self.hp = hp
        self.dmg = dmg
        self.special = special

class Room:

    def __init__(self, description, north, east, south, west):
        """Directions"""
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

def main():

    print("Hello there!")
    print("Welcome to school! Only issue is, we are in the middle of a zombie apocalypse!")
    print("Until authorities come to pick you up, you might wanna explore the school, "
        "\njust to see where's the safest place to lay low.")
    print()
    print("Oh yeah my name is AI-chan! I am here for explanation and comedic relief!")
    print("When you fight, you can attack, check health and use a special move!"
          "\n Pretty cool right~?")
    print("Just type what you want to do! Don't die on me though!")
    # Variable

# Rooms for the game
    current_room = 0
    # Room 0
    room_list = []
    my_room = Room("You are currently in the first classroom."
                   "\nGo north to enter another classroom, or stay put. I wouldn't stay."
                   "\nA zombie could come at any minute.", 1, None, None, None)
    room_list.append(my_room)
    # Room 1
    my_room = Room("You are in another classroom. Something seems off."
                   "\nDon't go back. I'd go north.", 2, 0, None, None)
    room_list.append(my_room)
    # Room 2
    my_room = Room("This is the gym. There is nothing there but athletic gear."
                   "\nThere is a room north, east, and west of you.", 6, 1, 3, 4)
    room_list.append(my_room)
    # Room 3
    my_room = Room("This must be the janitor's closet. Something seems off."
                   "\nThere is a room north and west of you.", 7, None, None, 2)
    room_list.append(my_room)
    # Room 4
    my_room = Room("You are in the Co-ed bathroom. It smells."
                   "\nThere is a room north and east of you."
                   "\nI wouldn't stay here if I were you.", 5, None, 2, None)
    room_list.append(my_room)
    # Room 5
    my_room = Room("You are in the teacher's lounge. Something seems off."
                   "\nThere is a room north of you and east of you.", 10, 4, 6, None)
    room_list.append(my_room)
    # Room 6
    my_room = Room("You are in a classroom full of cobwebs and crap."
                   "\nIt probably hasn't been used in years. They should clean it."
                   "\nThere is a room north, south, east, and west of you.", 9, 2, 7, 5)
    room_list.append(my_room)
    # Room 7
    my_room = Room("This is the smallest cafeteria you have even seen."
                   "\nSomething seems off.", 8, 3, None, 6)
    room_list.append(my_room)
    # Room 8
    my_room = Room("This is just an empty room."
                   "\nThe school probably hasn't found use for this room yet."
                   "\nHey! Just like you!", 11, 7, None, 9)
    room_list.append(my_room)
    # Room 9
    my_room = Room("Hmmm. This looks like a supply closet. Nothing here is worth using though."
                   "\n There's gotta be only a few rooms left until the Principal's office!"
                   "\nThere is a room north, south, east, and west of you.", 11, 6, 8, 10)
    room_list.append(my_room)
    # Room 10
    my_room = Room("I smell something horrid in here. There's a bit of stained blood on the walls and floor."
                   "\nThere is a room north, south, and east of here.", 11, 5, 9, None)
    room_list.append(my_room)
    # Room 11
    my_room = Room("Alright! The Principal's office! We made it! Huh...just a big desk and some chairs?"
                   "\nThis room looks boring and lame. Very anti-climactic.", None, None, None, None)
    room_list.append(my_room)

    enemy_list = []

    # Room 1
    enemy = Character("Oh no! A zombie! Ew...it looks like your ex. "
                      "\nWe should probably fight it!", 50, 10, 15,
                        "zombie", 1)
    enemy_list.append(enemy)

    # Room 3
    enemy = Character("Oh no! Another zombie! Huh.... "
                      "\nHe's still wearing a janitor's uniform.", 60,
                      15, 20, "janitor zombie", 3)
    enemy_list.append(enemy)

    # Room 5
    enemy = Character("Seriously? Another zombie? How many are there? "
                      "\nQueue Harry Potter reference: 36 "
                      "\ncounted them myself. 36?! Sorry sorry! Let's"
                      "\n get em!", 50, 10, 15, "zombie", 5)
    enemy_list.append(enemy)

    # Room 7
    enemy = Character("Oh no! Another one for the zillionth time!"
                      "\n There must be a boss like zombie the other zombies"
                      "\nare protecting! It might be in the principal's office!",
                      50, 10, 15, "zombie", 7)
    enemy_list.append(enemy)

    # Room 9
    enemy = Character("Hey! Another zombie! We must be close cause this one is bigger"
                      "\n than the other's we've fought! Let's kick his but! Hehe sorry!"
                      "\n I'm not allowed to cuss!", 75, 10, 15, "zombie guard", 9)
    enemy_list.append(enemy)

    # Room 10
    enemy = Character("I sense something evil beyond this room. I think the room ahead of us "
                      "\nis the principal's office. THIS DARN ZOMBIE GUARD THING IS IN THE WAY!"
                      "\nLet's put hom somewhere not in the way! Like knocked out on the floor!",
                      75, 10, 15, "zombie guard", 10)
    enemy_list.append(enemy)

    # Room 11
    # Room 11
    enemy = Character("Alright! Here's the zombie boss! If we beat this guy and we win!"
                      "\n Not the apocalypse yah dummy! If we defeat the boss zombie the other"
                      "\n zombies will either go outside or completely clear the joint to find"
                      "\n another boss to guard. But at least the school will be a crap ton safer!"
                      "\n And it will make it easier for authorities to find us and take us to a"
                      "\n safe zone! Let's end this! ONCE AND FOR ALL! Sorry...got too excited", 100,
                      25, 50, "zombie boss", 11)
    enemy_list.append(enemy)
    player = Player(65, 15, 25)
# User input stuff
    done = False
    room_change = True
    while not done:
        if room_change:

            # User choice
            # Talks about the room
            print(room_list[current_room].description)
            # Going into the room triggers the enemy
            for enemy in enemy_list:
                if enemy.room == current_room:
                    print(enemy.description)
            room_change = False
        user_choice = input("\nWant do you want to do? ")
        # User options
        # If user quits
        if user_choice.lower() == "quit":
            print("you have quit the game. Hope I don't see you next time!")
            done = True
        # If user wants to go north
        elif user_choice.lower() == "north":
            next_room = room_list[current_room].north
            room_change = True
            if next_room is None:
                print()
                print("\nYou can't go there. Sorry bud.")
            else:
                current_room = next_room
        # If user wants to go east
        elif user_choice.lower() == "east":
            next_room = room_list[current_room].east
            room_change = True
            if next_room is None:
                print()
                print("\nYou can't go there. Sorry bud.")
            else:
                current_room = next_room
                # If user wants to go south
        elif user_choice.lower() == "south":
            next_room = room_list[current_room].south
            room_change = True
            if next_room is None:
                print()
                print("\nYou can't go there. Sorry bud.")
            else:
                current_room = next_room
        # If user wants to go west
        elif user_choice.lower() == "west":
            next_room = room_list[current_room].west
            room_change = True
            if next_room is None:
                print()
                print("\nYou can't go there. Sorry bud.")
            else:
                current_room = next_room
        # The user can choose to attack
        elif user_choice.lower() == "fight":
            print()
            print("\nAlright! A fight! You got basic attack and a special move! You can also check health!"
              "\n Don't get too cocky though because that stupid af zombie has the same thing!"
              "\n That's a bit overpowered for an enemy to be as powerful is not more than the character!"
              "\n Who created this darn zombie virus?!")
            print()
            print("Anywho!!! What do you wanna do now?")
        # The user then has to pick what to do
        if user_choice.lower() == "attack":
            for enemy in enemy_list:
                if enemy.room == current_room:
                    player.dmg = random.randrange(1, 15)
                    enemy.hp -= player.dmg
                    print()
                    print("Oh yeah! Let's use slash! Pow!")
                    print("That did", player.dmg, "dmg!")
                    print("That darn zombie is at", enemy.hp, " left!")
                    if enemy.hp <= 0:
                        print()
                        print("Yahoo! Yah did it! He dead! Again!")
                        player.hp = 65
                    else:
                        print("Kaboom! Let's keep it up!")
                        print("Ayaya! The zombie is attacking! He's using bite!")
                        player.hp = player.hp - enemy.dmg
                        print("Boof! That did", enemy.dmg, "damage!")


        elif user_choice.lower() == "special":
            for enemy in enemy_list:
                if enemy.room == current_room:
                    enemy.hp = enemy.hp - player.special
                    print()
                    print("Improvised special move: The Comet Home Run!")
                    print("Nice! That did", player.special, "damage!")
                    print("That darn zombie is at", enemy.hp, " left!")
                    if enemy.hp <= 0:
                        print()
                        print("Yahoo! Yah did it! He dead! Again!")
                        player.hp = 65
                    else:
                        print("Kaboom! Let's keep it up!")
                        print("Ayaya! The zombie is attacking! He's using bite!")
                        player.hp = player.hp - enemy.special
                        print("Boof! That did", enemy.special, "damage!")

        elif user_choice.lower() == "check health":
            print()
            if player.hp <= 10:
                print("Oh no! You're low on health! Be super super careful! I can't resurrect you yah know!")
                print("Health:", player.hp)

            elif player.hp <= 50:
                print("Oof yah took a beating! You got this though! It's just a flesh wound!")
                print("Health:", player.hp)

            else:
                print("Pfffffft what are you checking your health for! You barely have a scratch on you!")
                print("Health:", player.hp)
# Main function
main()