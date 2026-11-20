username = '@Admin'      #Hardcoded username 
password = '@Admin0001'  #Hardcoded password 
# system 
a = 0
while a == 0 :
    u = input("Enter the username : ")
    if(u == username):                 # Username verification
        i = 0
        while i == 0 :
            p = input("Enter the password : ")
            if(p == password):        # Password verification 
                print("Welcome !")
                i = 1                 # For terminating the while loop 
                a = 1                 # For terminating the while loop 
            else :
                print("Try Again !")
    else:
        print("The username doesn't exist ! Please enter a valid username.")