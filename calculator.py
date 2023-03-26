def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a, b):
    answer = a - b
    print(str(a) + " - "  + str(b) + " = " + str(answer) + "\n")

def mul(a, b):
    answer = a * b
    print(str(a) + " * "  + str(b) + " = " + str(answer) + "\n")

def div(a, b):
    answer = a / b
    print(str(a) + " / "  + str(b) + " = " + str(answer) + "\n")

while True:
    print("A : Addition") 
    print("S : Subtraction")
    print("M : Multiplication")
    print("D : Division")
    print("E : Exit")

    choice = input("Input your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("Enter first Number: "))
        b = int(input("Enter second number: "))
        add(a,b)

    elif choice == "s" or choice == "S":
        print("Subtraction")
        a = int(input("Enter first Number: "))
        b = int(input("Enter second number: "))
        sub(a,b)

    elif choice == "m" or choice == "M":
        print("Multiplication")
        a = int(input("Enter first Number: "))
        b = int(input("Enter second number: "))
        mul(a,b)

    elif choice == "d" or choice == "D":
        print("Multiplication")
        a = int(input("Enter first Number: "))
        b = int(input("Enter second number: "))
        div(a,b)

    elif choice == "e" or choice == "E":
        print("Program ended")
        quit()

    