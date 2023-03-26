def emailspliter():
    print("Welcome to email spilter...")
    
    user_input = input("Enter your email :")

    (username, domain) = user_input.split("@")
    (domain, extension) = domain.split(".")


    print("Username :", username)
    print("Domain :", domain)
    print("Extension :", extension)

while True:
    emailspliter()
    if input == "quit":
        print("Thankyou for using Emailspliter...")
        quit()

    
           

    



