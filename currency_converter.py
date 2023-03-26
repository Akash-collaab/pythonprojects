def main():
    print("This is a program to convert us doller into indian currency...")

    dollar = eval(input("Enter the amount :"))

    Rupees = convert_to_rupees(dollar)
    print("This is ",Rupees ,"Rupees.")

convert_to_rupees = lambda dollar: dollar * 83

main()
