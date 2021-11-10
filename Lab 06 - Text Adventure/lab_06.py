class Room:
    def __init__(self, description, north, east, south, west):
        """Directions"""
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
# Main function
# Main Function
def main():
    print("Hello there!")
    print("You got stuck into a Dungeon. There may be evil creatures or treasure. Cool?")
    print("You should probably explore it, just in case there is something cool.\n")
    # Variable
    current_room = 0
    # Room 0
    room_list = []
    my_room = Room("You are outside the dungeon."
                   "\nGo north to enter the dungeon, or stay put. I wouldn't stay put"
                   "\nYou'll probably get mauled by a bear.", 1, None, None, None)
    room_list.append(my_room)
    # Room 1
    my_room = Room("You are in the entrance of the dungeon. Nothing special."
                   "\nDon't go back outside. Id go north.", 2, 0, None, None)
    room_list.append(my_room)
    # Room 2
    my_room = Room("Welcome to the room of doom. There is nothing there."
                   "\nThere is a room north, east, and west of you.", 6, 1, 3, 4)
    room_list.append(my_room)
    # Room 3
    my_room = Room("Welcome to the room of the heartless. There is a heartless here. I'd leave it alone."
                   "\nThere is a room north and west of you.", 7, None, None, 2)
    room_list.append(my_room)
    # Room 4
    my_room = Room("You are in the Persona room. Yu Narukami is fighting a shadow. You cheer him on!"
                   "\nThere is a room north and east of you."
                   "\nDon't worry. Yu defeats the shadow and gives you a high five.", 5, None, 2, None)
    room_list.append(my_room)
    # Room 5
    my_room = Room("You are in a treasure room. You pick up a cool gold necklace and you put it on."
                   "\nThere is a room north of you and east of you.", 10, 4, 6, None)
    room_list.append(my_room)
    # Room 6
    my_room = Room("You are in the Castlevania room. There is the Shadow Knight."
                   "\nYou don't want to bug him as he sold his soul to the devil."
                   "\nThere is a room north, south, east, and west of you.", 9, 2, 7, 5)
    room_list.append(my_room)
    # Room 7
    my_room = Room("You are in the Dragon Ball Z room of Doom."
                   "\nOh no! Frieza is here! You better run into a different room quick!"
                   "\nThere is a room north, south and west of you.", 8, 3, None, 6)
    room_list.append(my_room)
    # Room 8
    my_room = Room("Welcome to the Naruto Room. Naruto is sitting in the corner eating ramen."
                   "\nHe has another bowl next to him, so you sit down and eat ramen with him."
                   "\nThere is a room north, south, and west of you.", 11, 7, None, 9)
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
    done = False
    while not done:
        # User choice
        print(room_list[current_room].description)
        user_choice = input("\nWhat direction. ")
        # User options
        # If user quits
        if user_choice.upper() == "QUIT" or user_choice.upper() == "Q":
            print("you have quit the game.")
            done = True
        # If user wants to go north
        elif user_choice.upper() == "NORTH" or user_choice.upper() == "N":
            next_room = room_list[current_room].north
            if next_room is None:
                print()
                print("\nYou shant go there.")
            else:
                current_room = next_room
        # If user wants to go east
        elif user_choice.upper() == "EAST" or user_choice.upper() == "E":
            next_room = room_list[current_room].east
            if next_room is None:
                print()
                print("\nYou shant go there.")
            else:
                current_room = next_room
        # If user wants to go south
        elif user_choice.upper() == "SOUTH" or user_choice.upper() == "S":
            next_room = room_list[current_room].south
            if next_room is None:
                print()
                print("\nYou shant go there.")
            else:
                current_room = next_room
        # If user wants to go west
        elif user_choice.upper() == "WEST" or user_choice.upper() == "W":
            next_room = room_list[current_room].west
            if next_room is None:
                print()
                print("\nYou shant go there.")
            else:
                current_room = next_room
# Main function
main()

