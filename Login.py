print("Welcome to ISG")
acc = input("Do you have a account?")
if acc =="yes":
    

    print("Please Login:\n")
    User_name= input("Username: ")
    pass_=input("Password: ")
    print("Welcome to your childs profile,what would you like to see?")
    print("\n1.Behavious , \n2.Accademic ,\n")
    select = input("Select any : ")
    if select =="1":
        print("Sipho's Profile")
        print("\n -Sipho is noisy in class \n -He eats during lessons")
    elif select == "2":
        print("formal task april: 30/45")
   
    elif select == "3":
        
    count = 2
    pass_=input("Enter password")
    while count > 0:

        if pass_=="1234":
         print("Welcome")
        else:
            retry_=input("Retry password")
            count -= 1
            print("Login Failed")
            break
elif acc == "no":
    print("please register")
    first_name = input("Name: ")
    surname = input("Surname: ")
    email = input("Email: ")
    pass_word=input("password: ")
    print("Confirm password")
    pass_word2 = input("confirm password: ")
    if pass_word == pass_word2:
        print("account confirmed")
    else:
        print("Password does not match")
        quit()
    
    print("Welcome to your childs profile,what would you like to see?")
    print("\n1.Behavious , \n2.Accademic ,\n3.Homework")



else:
       quit()
