# Lab 04 Camel Game: Star Wars edition
import random

# Introduction
def main():
    print("You are in the middle of space.")
    print("You are trying to get back to Dantooine, a Rebel Alliance base.")
    print("Dantooine is 59 light years away, or 18 parsecs.")
    print("You are running from imperials because you stole a Tie Fighter!")
    print("You will be asked what to do in certain situations. Can you survive the chase?")
    print()
    # variables
    done = False
    light_years_traveled = 0
    imperials_traveled = -20
    tie_fighter_gas = 50
    thirst = 0
    canteen = 5
    cantina = -1

    # Game itself (main function)
    while not done:
        print("A. Drink Thala-Siren Milk from your canteen.")
        print("B. Ahead at moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status Check.")
        print("Q. Quit.")
        print()

        # Take input code
        choice = input("What is your decision?")

        # If the user wants to quit
        if choice.upper() == "Q":
            print("Goodbye. May the Force be with you.")
            done = True

        # If the user makes a status check
        elif choice.upper() == "E":
            print("Light Years Traveled:", light_years_traveled)
            print("Drinks in canteen:", canteen)
            print("The Imperials are", light_years_traveled - imperials_traveled, "light years behind you.")
            print()

        # If the user wants to stop for the night
        elif choice.upper() == "D":
            print("You stop at a nearby planet or asteroid and sleep for the night.")
            print("You filled up on gas and checked your hyperdrive.")
            print("The Imperials don't stop.")
            print()
            tie_fighter_gas = 50
            imperials_traveled -= random.randrange(1, 4)

        # If the user chooses 'full speed ahead'
        elif choice.upper()  == "C":
            light_years = random.randrange(5, 13)
            light_years_traveled += light_years
            thirst += 1
            tie_fighter_gas -= random.randrange(7, 15)
            if random.randrange(20) == 0:
                thirst = 0
                tie_fighter_gas = 0
                canteen = 3
                print("As you travel to the nearest cantina on the nearest planet,")
                print("You fill your cantina dn stomach with imported Thala-Siren Milk, and")
                print("The Tie Fighter you stole is all fueled up!")
                print("There are no problems with the Tie Fighter's hyperdrive.")
                print("The imperials continue to chase you.")
                print()
            else :
                print("You speed up your tie fighter, moving a total of", light_years, "light years.")
                print("The imperials continue chasing.")
                print()

        # If the user chooses 'moderate speed'
        elif choice.upper() == "B":
            light_years = random.randrange(5, 13)
            light_years_traveled += light_years
            thirst += 1
            tie_fighter_gas -= 1
            imperials_traveled += random.randrange(7, 15)
            cantina = random.randrange(20)
            if cantina == 10:
                thirst = 0
                tie_fighter_gas = 0
                canteen = 3
                print("As you travel to the nearest cantina on the nearest planet,")
                print("You fill your canteena dn stomach with imported Thala-Siren Milk, and")
                print("The Tie Fighter you stole is all fueled up!")
                print("There are no problems with the Tie Fighter's hyperdrive.")
                print("The imperials continue to chase you.")
                print()
            else:
                print("You move forward at a decent speed, moving a total of", light_years, "light years.")
                print("The imperials continue chasing.")
                print()

        # Drink from the canteen
        elif choice.upper() == "A":
            if canteen > 0:
                canteen -= 1
                thirst = 0
                print("You take a drink of your Thala-Siren Milk. The milk satisfies your thirst.")
            else:
                print("Your canteen is empty. You are sad that you are out of Thala-Siren milk.")
                print(" You imagine yourself as a old, wrinkly Thala-Siren from Ahch-To.")

        # Status updates

        # Thirst
        if thirst > 5:
            print("You died of thirst! The tie fighter crashes and the Rebels fail.")
            print("GAME OVER!")
            print()
            done = True
        elif thirst > 4:
            print("You are really thirsty!")

        # Distance Traveled/ win check
        if light_years_traveled >= 59:
            print("Congratulations! You survived the imperial chase!")
            print("The Rebels now have the upper hand against the Galactic Empire!")
            print("Leia gave you a medal and Han Solo challenged you to a race.")
            print()
            done = True

        # Tie Fighter Troubles
        if tie_fighter_gas < 10:
            print("Your tie fighter ran out of gas!")
            print("You crash landed and died a horrible and fiery death!")
            print("I guess the good news is the imperials didn't find the rebel base.")
            print("The rebels lost and the Galactic Empire conquers the entire galaxy.")
            print("You still wonder to this day if anyone held a funeral for you.")
            print("GAME OVER!")
            print()
            done = True
        elif tie_fighter_gas < 5:
            print("You're getting low on gas. There might be something wrong with the hyperdrive.")
            print()

        # Imperials distance from you
        if light_years_traveled - imperials_traveled <= 0:
            print("The imperials caught up to you!")
            print("You appeared in their firing range and they shot you down!")
            print("On the bright side they had to buy a new tie fighter.")
            print("GAME OVER!")
            print()
        elif light_years_traveled - imperials_traveled < 15:
            print("You can see familiar planets as you are getting close to Dantooine.")
            print("The natives are getting close!")
            print()

    # Exit message
    print("Exiting Game.")
    input("")
main()
