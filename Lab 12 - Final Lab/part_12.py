import random
import math

class Student:
    def __init__(self, name, hp, dmg, special, chance):
        self.hp = hp
        self.dmg = dmg
        self.special = special
        self.chance = chance
        self.name = name

    def gethp(self):
        return self.hp
    def getdmg(self):
        return self.hp
    def getspecial(self):
        return self.special
    def getchance(self):
        return self.chance
    def getname(self):
        return self.name

    def sethp(self, newhp):
        self.hp = newhp
    def setdmg(self, newdmg):
        self.dmg = newdmg
    def setspecial(self, newspecial):
        self.special = newspecial
    def getchance(self, newchance):
        self.chance = newchance

class Bully:
    def __init__(self, name, hp, dmg, special, chance, north, east, south, west):
        super().__init__()
        self.hp = hp
        self.dmg = dmg
        self.special = special
        self.chance = chance
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west

    def gethp(self):
        return self.hp
    def getdmg(self):
        return self.hp
    def getspecial(self):
        return self.special
    def getchance(self):
        return self.chance
    def getname(self):
        return self.name

    def sethp(self, newhp):
        self.hp = newhp
    def setdmg(self, newdmg):
        self.dmg = newdmg
    def setspecial(self, newspecial):
        self.special = newspecial
    def getchance(self, newchance):
        self.chance = newchance

class Teacher:
    def __init__(self, name, hp, dmg, special, chance, north, east, south, west):
        super().__init__()
        self.hp = hp
        self.dmg = dmg
        self.special = special
        self.chance = chance
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west

    def gethp(self):
        return self.hp
    def getdmg(self):
        return self.hp
    def getspecial(self):
        return self.special
    def getchance(self):
        return self.chance
    def getname(self):
        return self.name

    def sethp(self, newhp):
        self.hp = newhp
    def setdmg(self, newdmg):
        self.dmg = newdmg
    def setspecial(self, newspecial):
        self.special = newspecial
    def getchance(self, newchance):
        self.chance = newchance

class Janitor:
    def __init__(self, name, hp, dmg, special, chance, north, east, south, west):
        super().__init__()
        self.hp = hp
        self.dmg = dmg
        self.special = special
        self.chance = chance
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west

    def gethp(self):
        return self.hp
    def getdmg(self):
        return self.hp
    def getspecial(self):
        return self.special
    def getchance(self):
        return self.chance
    def getname(self):
        return self.name

    def sethp(self, newhp):
        self.hp = newhp
    def setdmg(self, newdmg):
        self.dmg = newdmg
    def setspecial(self, newspecial):
        self.special = newspecial
    def getchance(self, newchance):
        self.chance = newchance

class Principal:
    def __init__(self, name, hp, dmg, special, chance, north, east, south, west):
        super().__init__()
        self.hp = hp
        self.dmg = dmg
        self.special = special
        self.chance = chance
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west

    def gethp(self):
        return self.hp
    def getdmg(self):
        return self.hp
    def getspecial(self):
        return self.special
    def getchance(self):
        return self.chance
    def getname(self):
        return self.name

    def sethp(self, newhp):
        self.hp = newhp
    def setdmg(self, newdmg):
        self.dmg = newdmg
    def setspecial(self, newspecial):
        self.special = newspecial
    def getchance(self, newchance):
        self.chance = newchance

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
    print("Welcome to school! Class just finished and your parents aren't here.")
    print("Until they come to pick you up, you might wanna explore the school.\n")
    # Variable

# Rooms for the game
    current_room = 0
    # Room 0
    room_list = []
    my_room = Room("You are currently in your classroom."
                   "\nGo north to enter another classroom, or stay put. I wouldn't stay."
                   "\nYour bully is still in the classroom.", 1, None, None, None)
    room_list.append(my_room)
    # Room 1
    my_room = Room("You are in another classroom. Something seems off."
                   "\nDon't go back. Id go north.", 2, 0, None, None)
    room_list.append(my_room)
    # Room 2
    my_room = Room("This is the gym. There is nothing there but athletic gear."
                   "\nThere is a room north, east, and west of you.", 6, 1, 3, 4)
    room_list.append(my_room)
    # Room 3
    my_room = Room("This must be the janitor's closet.Something seems off."
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
    my_room = Room("You are in the Sword Art Online Room. This is the worst room ever."
                   "\nAsuna and Kirito are cuddling. Ew! Leave now!"
                   "\nThere is a room north, south, east, and west of you.", 11, 6, 8, 10)
    room_list.append(my_room)
    # Room 10
    my_room = Room("You are in the Legend of Zelda room. Dark Ganon is there. I'd leave him alone."
                   "\nThere is a room north, south, and east of here.", 11, 5, 9, None)
    room_list.append(my_room)
    # Room 11
    my_room = Room("You are in the Terraria room. CALAMITUS IS HERE! Quit the game now before you die!"
                   "\nNo actually. Quit the game. There is nowhere else to go", None, None, None, None)
    room_list.append(my_room)

# Where the enemies are going to be
    bully_list = []

    # Room 1
    my_bully = Bully("Oh no! There is a bully that wants his lumch money early!"
                     "\n We probably have to fight him!", 50, 10, 15, 5, 2, 0, None, None)
    bully_list.append(my_bully)
    # Room 7
    my_bully = Bully("Seriously? Another bully? How many bullys do you have?"
                   "\nYou are going to have to fight this one.", 50, 10, 15, 5, 8, 3, None, 6)
    bully_list.append(my_bully)

    teacher_list = []

    # Room 5
    my_teacher = Teacher("Hey! It's that teacher you have a crush on!"
                   "\nDidn't she give you a free A in Biology last year?"
                    "\nToo bad you need to fight her to leave.", 75, 20, 25, 15, 10, 4, 6, None)
    teacher_list.append(my_teacher)

    # Room 8
    my_teacher = Teacher("Uh oh! Looks like the room isn't so empty!"
                   "\nAnother teacher! Not as good looking as the last one though."
                   "\nShe should be easy to take out!", 60, 15, 20, 10, 11, 7, None, 9)
    teacher_list.append(my_teacher)

    principal_list = []

    # Room 11
    my_principal = Principal("Ew, it's the principal King Moron."
                   "\nI wonder if you become principal if you take him out.", None, None, None, None)
    principal_list.append(my_principal)

# User input stuff
    done = False
    while not done:
        # User choice
        print(room_list[current_room].description)
        user_choice = input("\nWhat direction. ")
        # User options
        # If user quits
        if user_choice.upper() == "QUIT" or user_choice.upper() == "Q" or user_choice.upper() == "q":
            print("you have quit the game. Hope I don't see you next time!")
            done = True
            # If user wants to go north
        elif user_choice.upper() == "NORTH" or user_choice.upper() == "N" or user_choice.upper() == "n":
            next_room = room_list[current_room].north
            if next_room is None:
                print()
                print("\nYou can't go there. Sorry bud.")
            else:
                current_room = next_room
        # If user wants to go east
        elif user_choice.upper() == "EAST" or user_choice.upper() == "E" or user_choice.upper() == "e":
            next_room = room_list[current_room].east
            if next_room is None:
                print()
                # ERROR HERE: INDENT DOES NOT MATCH
                # ANY OUTER INDENTATION LEVEL
                print("\nYou can't go there. Sorry bud.")
             else:
                current_room = next_room
                    # If user wants to go south
        elif user_choice.upper() == "SOUTH" or user_choice.upper() == "S" or user_choice.upper() == "s":
            next_room = room_list[current_room].south
            if next_room is None:
                print()
                print("\nYou can't go there. Sorry bud.")
            else:
                current_room = next_room
            # If user wants to go west
        elif user_choice.upper() == "WEST" or user_choice.upper() == "W" or user_choice.upper() == "w":
            next_room = room_list[current_room].west
            if next_room is None:
                print()
                print("\nYou can't go there. Sorry bud.")
            else:
                current_room = next_room


# Main function
main()