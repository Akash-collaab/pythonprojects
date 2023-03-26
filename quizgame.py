print("Welcome to my computer")

playing = input("Do you wanna play? ")
score = 0

if playing.lower() != "yes":
    quit()
print("Let's paly!")

answer = input("What does a CPU stands for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')   

answer = input("What does a GPU stands for? ")
if answer.lower() == ("graphical processing unit " or "graphics processing unit"):
    print('Correct!')
    score += 1
else:
    print('Incorrect!')   

answer = input("What does a RAM stands for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')      

answer = input("What does a ROM stands for? ")
if answer.lower() == "read only memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')   

print("You got " + str(score) + " question correct!")
print("You got " + str((score / 4) * 100) + "%.")