# collect the necessary inputs: salary, apr, years
# calculate the montly payement 
# show to the user 

def main():
    print("This is a montly payement calculator app")
    print("")

    principal_loan = float(input("Enter the amonut of loan :"))
    arp = float(input("Enter the interest rate amount :"))
    years = int(input("Enter the Time duration :"))

    monthly_interest = arp / 1200
    amount_of_months = years * 12
    monthly_payement = principal_loan * monthly_interest / (1 - (1+ monthly_interest) ** (-amount_of_months))

    print("The montly payement for this loan is %.2f " % monthly_payement)

main()

def main():
    print("This is a montly payement calculator for your loant")

    amount = float(input("Enter the amount of loan :"))
    rate_of_interest = float(input("Enter the interest amount :"))
    time_duration = int("Enter time duration in years :")

    montly_interest = rate_of_interest / 1200
    amount_of_month = time_duration * 12
    montly_payment = amount *  montly_interest / (1 - (1+ montly_interest) ** (-amount_of_month))

    print("The monthly payement for this loan is %.2f " % montly_payment)