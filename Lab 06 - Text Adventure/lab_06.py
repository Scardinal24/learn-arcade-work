# This Lab 6 was coded by Sammy Cardinal

# classes
class Room:
    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west

class Character:
    def __init__(self, name, hp, current_hp, dmg):
        self.name = name
        self.hp = hp
        self.current_hp = current_hp
        self.dmg = dmg

class Enemy:
    def __init__(self, name, hp, current_hp, dmg):
        self.name = name
        self.hp = hp
        self.current_hp = current_hp
        self.dmg = dmg

def main():
    room_list = []
    # Outside
    outside = Room("Outside", 1, None, None, None)
    room_list.append(outside)
    # Entrance
    entrence = Room("Entrance", 2, 0, None, None)
    room_list.append(entrence)
    # Room 1
    room_two = Room("Room 1", 6, 1, 3, 4)
    room_list.append(room_two)
    # Room 2
    room_three = Room("Room 2", 6, 1, 4, 3)
    room_list.append(room_three)
    # Room 3
    room_four = Room("Room 3", 7, None, 2, None)
    room_list.append(room_four)
    # Room 4
    room_five = Room("Room 4", 5, None, None, 2)
    room_list.append(room_five)
    # Room 5
    room_six = Room("Room 5", 10, 4, None, 6)
    room_list.append(room_six)
    # Room 6
    room_seven = Room("Room 6", 9, 2, 5, 7)
    room_list.append(room_seven)
    # Room 7
    room_eight = Room("Room 7", 8, 3, 6, None)
    room_list.append(room_eight)
    # Room 8
    room_nine = Room("Room 8", None, 7, 9, None)
    room_list.append(room_nine)
    # Room 9
    room_ten = Room("Room 9", 11, 6, 10, 8)
    room_list.append(room_ten)
    # Room 10
    room_eleven = Room("Room 10", None, 5, None, 9)
    room_list.append(room_eleven)
    # Room 11
    room_twelve = Room("Room 11", None, 9, None, None)
    room_list.append(room_twelve)

    character_list = []
    # Self
    self = Character("Self", 50, 0, 5)
    character_list.append(self)
    # Scout
    scout = Character("Scout", 150, 0, 15)
    character_list.append(scout)
    # Heavy
    heavy = Character("Heavy", 200, 0, 25)
    character_list.append(heavy)
    # Soldier
    soldier = Character("Soldier", 175, 0, 20)
    character_list.append(soldier)

    enemy_list = []
    # Heartless
    heartless = Enemy("Heartless", 100, 0, 5)
    enemy_list.append(heartless)
    # Shadow Knight
    shadow_knight = Enemy("Shadow Knight", 150, 0, 20)
    enemy_list.append(shadow_knight)
    # Calamitus
    calamitus = Enemy("Calamitus", 300, 0, 50)
    enemy_list.append = Enemy(calamitus)

current_room  = 0
entrance = current_room

def start():
    outside()
    print("\nYou got sucked into a world where enemies from multiple games come together.")
    print("The only way out is to survive the dungeon. The entrance is in front of you.")
    print("Do you stay outside and see what happens or do you enter?")

    answer = input(">").lower()

    if "stay outside" or "Stay outside" or "outside" in answer:
        print("Good job. In the middle of the night, you got mauled by a bear. Game Over.")
        game_over()

    elif "go inside" or "Go inside" or "enter" or "Enter" in answer:
        entrence()

def entrence():
    print("\nYou are now in the entrance, there is a room north of you. What direction do you go?")

    answer = input(">").lower()

    if "north" or "North" or "n" or "N" in answer:
        room_two()
    else:
        print("Do you even know how to type?")

def room_two():
    print("\nWelcome to the first room. There is a room north, east, and west of you.")
    print("The entrance is south of you. There is really nothing going on here. Which direction next?")

    if "North" or "north" or "N" or "n" in answer:
        room_six()
    elif "West" or "west" or "W" or "w" in answer:
        room_three()
    elif "East" or "east" or "E" or "e" in answer:
        room_four()
    elif "South" or "south" or "S" or "s" in answer:
        print("You wanna go back? Alright...")
        entrance()
    else:
        print("Do you even know how to type?")


def room_three():
    print("\nWelcome to the first room. There is a room north and east of you.")
    print("The entrance is south of you. There is really nothing going on here. Which direction next?")

    if "North" or "north" or "N" or "n" in answer:
        room_seven()
    elif "West" or "west" or "W" or "w" in answer:
        print("There isn't a room here. Try again")
    elif "East" or "east" or "E" or "e" in answer:
        room_four()

    else:
        print("Do you even know how to type?")
main()