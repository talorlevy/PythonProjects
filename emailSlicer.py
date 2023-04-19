# collect the email from user
# split the email using the @, the first part as the username, the second part as the domain
# split domain using .

def main():
    print("Welcome to the email slicer! \n \n")
    print("")
    
    email_input = input("Input your email address: ")
    
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    
    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)

while True:
    main()
