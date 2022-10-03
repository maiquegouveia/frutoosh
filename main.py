
users = 0
username = []
email = []
password = []
feedback = []
phone_number = []

username_adm = "MAIQUE"
email_adm = "maique@123"
password_adm = "love123"

product = ["Nintendo Switch", "PlayStation 5 Console", "Xbox Series X"]
products_price = [299.99, 499.99, 499.00] 

def menu (): 
    while True:
        print("Hello " + username[position] + "!")
        print(" 1 - Online Shopping")
        print(" 2 - Send Feedback")
        print(" 3 - Settings")
        print(" 4 - Log Out")
        menu_option = input("Choose an option --> ")
        
        if menu_option == "1":
            n = 0
            print("List of our products: ")
            for product_name in product:
                print(str(n) + " - " + product_name + " | Price: $" + str(products_price[n]))
                n += 1
                
            product_option = int(input("Choose an option --> "))
            products_quantity = int(input("How many " + product[product_option] + " do you want to buy? "))
            total_price = float(products_price[product_option]) * products_quantity
            print("Total Price: $" + str(total_price) + " dollars.")
            
        elif menu_option == "2":
            review = input("Feedback: ")
            feedback[position] = review
            print("Thank you for your feedback!")
            
        elif menu_option == "3":
            while True:
                print("1 - Change Username")
                print("2 - Change E-mail")
                print("3 - Change Password")
                print("4 - Go Back")
                menu_option = input("Choose an option --> ")
                
                if menu_option == "1":
                    new_username = input("Enter the new username: ").upper()
                    if new_username in username:
                        print("This username is being used.")
                    else:
                        username[position] = new_username
                        print("The username was changed successfully.")
                        
                elif menu_option == "2":
                    new_email = input("Enter the new email: ")
                    if new_email in email:
                        print("This email is being used.")
                    else:
                        email[position] = new_email
                        print("The email was changed successfully.")
                        
                elif menu_option == "3":
                    new_password = input("Enter the new password: ")
                    test_new_password = input("Enter the new password again: ")
                    if new_password == test_new_password:
                        password[position] = new_password
                        print("The password was changed successfully.")
                    else:
                        print("The passwords don't match.")
                        
                elif menu_option == "4":
                    break
                else:
                    print("Invalid option.")
                    
        elif menu_option == "4":
            print("See you later!")
            break
        else:
            print("Invalid option.")

def menu_adm():
    global username_adm
    global email_adm
    global password_adm
    
    while True:
        print("Hello " + username_adm + ", welcome back!")
        print("1 - Products")
        print("2 - Database")
        print("3 - Settings")
        print("4 - Log Out")
        menu_option = input("Choose an option --> ")
        
        if menu_option == "1":
            while True:
                print("1 - Remove Product")
                print("2 - Add Product")
                print("3 - Go Back")
                menu_option = input("Choose an option --> ")
                if menu_option == "1":
                    remove_products()
                elif menu_option == "2":
                    add_products()
                elif menu_option == "3":
                    break
                else:
                    print("Invalid option.")
                    
        elif menu_option == "2":
            print("Search in database")
            while True:
                consult_name = input("Enter a valid username or 0 to return: ").upper()
                if consult_name == '0':
                    break
                elif consult_name in username:
                    search_pos = username.index(consult_name)
                    print("Username: " + username[search_pos])
                    print("Phone Number: " + phone_number[search_pos])
                    print("Email: " + email[search_pos])
                    if len(feedback):    
                        print("Feedback: " + feedback[search_pos])
                    else:
                        print("User hasn't written a feedback yet.")
                    break
                else:
                    print("Invalid username.")
            
        elif menu_option == "3":
            while True:
                print("1 - Change Username")
                print("2 - Change E-mail")
                print("3 - Change Password")
                print("4 - Go Back")
                menu_option = input("Choose an option --> ")
                
                if menu_option == "1":
                    new_username = input("Enter the new username: ").upper()
                    if new_username in username:
                        print("This username is being used.")
                    else:
                        username_adm = new_username
                        print("The username was changed successfully.")
                        
                elif menu_option == "2":
                    new_email = input("Enter the new email: ")
                    if new_email in email:
                        print("This email is being used.")
                    else:
                        email_adm = new_email
                        print("The email was changed successfully.")
                        
                elif menu_option == "3":
                    new_password = input("Enter the new password: ")
                    test_new_password = input("Enter the new password again: ")
                    if new_password == test_new_password:
                        password_adm = new_password
                        print("The password was changed successfully.")
                    else:
                        print("The passwords don't match.")
                        
                elif menu_option == "4":
                    break
                else:
                    print("Invalid option.")
        elif menu_option == "4":
            break
        else:
            print("Invalid option.")
            
def remove_products():
    n = 0
    print("All the registered products: ")
    for name in product:
        print(str(n) + " - " + name)
        n += 1
    remove_option = int(input("Choose the product you want to remove --> "))
    product.remove(product[remove_option])
    products_price.remove(products_price[remove_option])
    print("Product successfully removed.")
    
def add_products():
    n = 0
    print("All the registered products: ")
    for name in product:
        print(str(n) + " - " + name)
        n += 1
    product.append(input("Enter the new product: "))
    products_price.append(input("Enter the price: "))
    print(product[-1] + " added to the list.")
    
while True:
    i = 0
    access_website = input("Enter YES to access the website or NO to close the program: ").lower()
    if access_website =="yes":
        print("*** Welcome to Frutoosh ***")
        print("You need an account to access this website.")
        
        while True:
            access_answer = input("Do you have an account? YES or NO? ").lower()
            if access_answer == "yes":
                check_email = input("Enter the email: ")
                if check_email == email_adm:
                    check_password = input("Enter the password: ")
                    if check_password == password_adm:
                        menu_adm()
                        break
                    else:
                        print("Invalid password.")
                else:
                    verification = False
                    position = 0
                    
                    while True:
                        if users > 0:
                            if position < users:
                                if email[position] == check_email:
                                    verification = True
                                    break
                                else:
                                    position += 1
                            else:
                                break
                        else:
                            print("No accounts created.")
                            break
                        
                    if verification == True and users > 0:
                        check_password = input("Enter the password: ")
                        if password[position] == check_password:
                            menu()
                            break
                        else:
                            print("Invalid password.")
                    elif verification == False and users > 0:
                        print("Email address not found.")
                    else:
                        pass
                    
            elif access_answer == "no":
                while True:
                    create_account_answer = input("Do you want to create an account? YES or NO? ").lower()
                    if create_account_answer == "yes":
                        while True:
                            create_username = input("Enter a username: ").upper()
                            if create_username in username:
                                print("This username is being used.")
                            else:
                                break
                        while True:    
                            create_email = input("Enter the email: ")
                            if create_email in email:
                                print("This email is being used.")
                            else:
                                break
                        while True:    
                            create_number = input("Enter your phone number: ")
                            if create_number in phone_number:
                                print("This phone number is being used.")
                            else:
                                break
                        create_password = input("Enter the password: ")
                        confirm_password = input("Enter the password again: ")
                        if create_password == confirm_password:
                            username.append(create_username)
                            email.append(create_email)
                            password.append(create_password)
                            phone_number.append(create_number)
                            print("Account created successfully.")
                            users += 1
                            break
                        else:
                            print("The passwords don't match.")
                    elif create_account_answer == "no":
                        print("Come back later.")
                        quit()
                    else:
                        print("Invalid option.")
            else:
                print("Invalid option.")
            
    elif access_website == "no":
        print("See you later!")
        break
    else:
        print("Invalid option.")