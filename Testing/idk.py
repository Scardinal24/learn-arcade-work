# For loops - when you know how many times to loop
# While loops - loop until a condition

# Starting of the game
start = "start"
while start == "start":
    start = input("Do you want to start? Type 'start' to start! Type 'No' to not start!")
    if start == "start":
        start = True

    if start == "No":
        print("Okay. The game will not start.")
        start = False

if start == True:
    print("You just graduated from college and you needed to get a job")

    print("a: Barista")
    print("b: Teacher")
    print("c: Programmer")
    print("d: I don't get a job")

job = "job"

while job == "job":
    job = input("Which job do you choose?")
    if job == "a":
        print("You took the job at Crazy Caffine's Coffee Shop!")
        print("But oh no! Everyone but you called in sick!")
        print("a: Close up shop and say 'Nobody showed up'.")
        print("b: Try your best to handle orders and the shop.")
        print("c: Sit in the back corner and cry.")
    if job == "b":
        print("You took the job at a local school near where you lived.")
        print("One of the boys decided to be a class clown and crack jokes during class.")
        print("a: tell him politely to stop and pay attention.")
    if job == "c":
        print("You decided to take a job at SparkPoint, a company for programming and technology.")
        print("Your supervisor told you about a bug complaint from their new smartwatch.")
        print("a: ")
    if job =="d":
        print("After not accepting the jobs, you applied for more jobs,")
        print("but your rent was coming up! What do you do?")

teach = "teacher"

while teach == "teacher":
    teacher = input("What do you do?")
    if teacher == "a":

coffee = "coffee"

while coffee == "coffee":
    coffee = input("What do you do?")
    if coffee == "a":
        print("Your supervisor recieved a complaint and let you go.")
        print("Letting go is a nice way of saying your fired.")
    if coffee == "b":
        print("Your supervisor recieved many compliments!")
        print("You recieved a promotion!")
    if coffee == "c":
        print("Not only did you get fired from youre job,")
        print("but you were also recammended for counciling. Good job.")
