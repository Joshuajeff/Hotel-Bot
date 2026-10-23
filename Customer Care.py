#database
import os
verified_user_and_password = {"josh": "7203Josh_"}

verified_username_and_full_name = {"josh": "Joshua Kelechi"}

verified_username_and_password_data = """Username,Password,Full name,Age,Phone number,Email Address
josh,7203Josh_,Joshua Kelechi,38,08067513975,Joshuajeff2064@gmail.com
"""
loc = "C:\\Users\\joshu\\PycharmProjects\\Roughsheet\\customer.csv"
if os.path.exists(loc):
    pass
else:
    with open('customer_details.csv', 'w') as file:
        file.write(verified_username_and_password_data)


#introduction
def front_page():
    front_page_loop = "start"
    while front_page_loop == "start":
        print(f"                \033[41m Welcome to Elite Customer care\033[0m")
        print("\033[34m -login\n -Sign up\n \033[0m")
        login_or_signup = input("\033[34m Enter: \033[0m")
        login_or_signup = login_or_signup.lower()
        if login_or_signup == "login":
            print("                   \033[7mWELCOME TO LOGIN PORTAL\033[0m")
            print("                           \033[4m LOGIN\033[0m\n")
            login()
            language()

        elif login_or_signup == "sign up":
            print("                   \033[7mWELCOME TO SIGN UP PORTAL\033[0m")
            print("                             \033[4mSIGN UP\033[0m\n")
            print("                    \033[4mThank You for choosing us,\033[0m")
            print("              \033[4mWe look forward to serving you better\n\033[0m")
            signup()
            language()
            front_page_loop = "end"
        else:
            print("\033[91m\n You have entered a wrong input\033[0m\n")


def login():
    # this make it possible for you to be able to use the username a user entered outside the function
    global username
    # start the loop as soon as the function is invoked
    username_loop = "start"
    while username_loop == "start":
        username = input("\033[34mEnter Username:  \033[0m")
        username = username.lower()
        with (open('customer.csv', 'r') as file):
            names = file.read()
            new_details = names.split("\n")
            if f"{username}," in names:
                for users in new_details:
                    if username in users:
                        real_name = users
                        main_name = real_name.split(",")
                        if username == main_name[0]:
                            username_loop = "end"
                            pass_loop = "start"
                            while pass_loop == "start":
                                password = input("\033[34mEnter Password: \033[0m")
                                details = users.split(", ")
                                if password == main_name[1]:
                                    pass_loop = "end"

                                else:
                                    print("\033[31mYou have entered a wrong password \033[0m")
                        else:
                            print("\033[31mYou have entered a wrong username \033[0m")



            else:
                print("\033[31mYou have entered a wrong detail \033[0m")
                print("\033[7mDO YOU WISH TO:\n 1. CONTINUE\n 2. RETURN TO SIGN UP\n 3. FORGOTTEN "
                      "USERNAME\033[0m")
                wish_loop = "start"
                while wish_loop == "start":
                    response = input("\033[34mEnter:  \033[0m")
                    response = response.lower()
                    if response == "1" or response == "continue":
                        login()
                    elif response == "2" or response == "return to sign up":
                        signup()
                    elif response == "3" or response == "forgotten username":
                        wish_loop = "end"
                        print("\033[94mEnter the last know username \033[0m")
                        last_username = input("\033[34mEnter:  \033[0m")
                        last_username = last_username.lower()
                        with (open('customer.csv', 'r') as file):
                            last_names = file.read()
                            last_user_name = last_names.split("\n")
                            if f"{last_username}," in last_names:
                                for user_name in new_details:
                                    if last_username in user_name:
                                        real_last_user = user_name
                                        main_name = real_last_user.split(",")
                                        if last_username == main_name[0]:
                                            wish_loop = "end"
                                            forgotten_username_loop = "end"
                                            forgotten_email = "start"
                                            print("\033[94mPlease provide the email address associated with this account "
                                                  "\033[0m")
                                            emailed_address = input("\033[34mEnter Email Address:  \033[0m")
                                            emailed_address = emailed_address.lower()
                                            with (open('customer.csv', 'r') as file):
                                                names = file.read()
                                                new_details = names.split("\n")
                                                if f"{email_address}," in names:
                                                    for people in new_details:
                                                        if email_address in people:
                                                            real_email = people
                                                            main_name = real_email.split(",")
                                                            if email_address == main_name[5]:
                                                                forgotten_email = "end"
                                                            else:
                                                                print("\033[31mYou have entered a wrong password \033[0m")
                                        else:
                                            print("\033[31mYou have entered a wrong username \033[0m")



                    else:
                        print("\033[31mYou have entered a wrong input\nPlease try again \033[0m")





def signup():
    global username2
    global name
    global phone_num
    global email_address
    global pass2
    global age
    signup_loop = "start"
    while signup_loop == "start":
        introduction_loop = "start"
        while introduction_loop == "start":
            print("                   \033[7mWELCOME TO SIGN UP PORTAL\033[0m")
            print("                             \033[4mSIGN UP\033[0m\n")
            print("                    \033[4mThank You for choosing us,\033[0m")
            print("              \033[4mWe look forward to serving you better\n\033[0m")
            name = input(f"\033[94m Enter Full name: \033[0m")
            name = name.capitalize()
            name_value = name.isdigit()
            if name_value:
                print(
                    "\033[91m\nPlease your name has to be an alphabet\ndo you wish to give us another name? \033[0m\n")
                print("\033[94mReply with Yes or no \033[0m")
                name_answer = input("")
                name_answer = name_answer.lower()
                if name_answer == "no":
                    print("\033[91m\n Sorry we cannot attend to you \033[0m\n")
                    front_page()
                elif name_answer == "yes":
                    signup()
            else:
                introduction_loop = "end"
                print(f"\033[93m Welcome {name}\033[0m")
                age = input("\033[94m How old are you: \033[0m")
                if int(age) < 18:
                    print("\n\033[91m Sorry we cannot attend to you\033[0m\n")
                    front_page()
                else:
                    pass

            phone_num_loop = "start"
            while phone_num_loop == "start":
                phone_num = input("\033[34m Phone Number: \033[0m")
                if phone_num.isdigit():
                    if len(phone_num) > 11:
                        print("\033[31mNumber should be 11 digits \033[0m")
                    elif len(phone_num) < 11:
                        print("\033[31mNumber should be 11 digits \033[0m")

                    else:
                        pass
                        phone_num_loop = "end"
                else:
                    print("\033[31mPhone number must be digit \033[0m")
            email_loop = "start"
            while email_loop == "start":
                email_address = input(f"\033[94m Enter Email: \033[0m")
                if "@" in email_address:
                    pass
                    email_loop = "end"
                else:
                    print(f"\033[94m Invalid Email address\033[0m")

            username2_loop = "start"
            while username2_loop == "start":
                username2 = input("\033[34m Choose username: \033[0m")
                username2 = username2.lower()
                if username2 in verified_user_and_password:
                    print("\033[91m Sorry that username has been chosen already\n"
                          "Please Choose another username\033[0m\n")
                else:
                    pass
                    username2_loop = "end"

            password_loop = "start"
            while password_loop == "start":
                pass2 = input("\033[34m Choose password: \033[0m")
                if len(pass2) >= 8:
                    if not pass2.isnumeric():
                        if not pass2.isupper():
                            if not pass2 == pass2.lower():
                                if (not pass2.find("0") == -1 or not pass2.find("1") == -1 or not pass2.find("2") == -1
                                        or not pass2.find("3") == -1 or not pass2.find("4") == -1 or not pass2.find(
                                            "5") == -1
                                        or not pass2.find("6") == -1 or not pass2.find("7") == -1 or not pass2.find(
                                            "8") == -1
                                        or not pass2.find("9") == -1):
                                    # verified_password.append(pass2)
                                    verified_user_and_password.update({username2: pass2})
                                    verified_username_and_full_name.update({username2: name})
                                    print(f"\033[94m Welcome {verified_user_and_password.get(username2)} \033[0m")
                                    print("\033[93m\nYou have successfully registered\n"
                                          "and your details has been recorded\033[0m\n")
                                    new_user = f"""{username2},{pass2},{name},{age},{phone_num},{email_address}
                                        """

                                    with open('customer.csv', 'a') as file:
                                        file.write(new_user)
                                    password_loop = "end"
                                    signup_loop = "end"
                                else:
                                    print(
                                        "\033[91m Your Password must contain at least one number\nPlease "
                                        "try again\033[0m\n")

                            else:
                                print(
                                    "\033[91m Your Password must contain at least one upper case letter\nPlease "
                                    "try again\033[0m\n")

                        else:
                            print("\033[91m Passwrd cannot be all uppercase.\033[0m\n")

                    else:
                        print("\033[91m Password cannot be all numbers\033[0m\n")

                else:
                    print("\033[91m Your Password must not be less than 8 Characters\nPlease try again\033[0m\n")


def language():
    #Choice of language
    language_loop = "start"
    while language_loop == "start":
        print("\033[94m Please choose your preferred language\033[94m ")
        language_menu = "\n1. English\n2. Igbo \n3. Yoruba\n4. Hausa\n5. Pidgin"
        print(f"\033[94m {language_menu} \033[94m ")
        language_ = input("\033[94m What is your preferred language: \033[0m")
        language_ = language_.lower()
        if language_ == "english" or language_ == "1":
            language_ = "English"
            print(f"\033[94m Your preferred language is {language_}\033[0m")
            service()
        elif language_ == "igbo" or language_ == "2":
            language_ = "Igbo"
            print(f"\033[91m we are currently working on {language_} language\033[0m")
        elif language_ == "yoruba" or language_ == "3":
            language_ = "Yoruba"
            print(f"\033[91m we are currently working on {language_} language\033[0m")
        elif language_ == "hausa" or language_ == "4":
            language_ = "Hausa"
            print(f"\033[91m we are currently working on {language_} language\033[0m")
        elif language_ == "pidgin" or language_ == "5":
            language_ = "Pidgin"
            print(f"\033[91m we are currently working on {language_} language\033[0m")
            language_loop = "end"
        else:
            print(f"\033[91m This are the available language \033[0m")


def service():
    #services offered
    service_list_loop = "start"
    while service_list_loop:
        menu = input(f"\033[94m \n1. Membership Registration \n2. Membership Verification \n3. "
                     "Membership Fee \n4. Speak to Customer Care \n5. Exit \033[0m\n")
        menu = menu.lower()
        if menu == "membership registration" or menu == "1":
            menu1 = input(f"\033[94m Please choose your desired number \n 1. Renew Membership subscription \n "
                          "2. Sign up for  membership \n 3. Know about the organization\033[0m\n")
            if menu1 == "1":
                menu1a = input(f"\033[94m Full name: \033[0m")
                occupation = input(f"\033[94m Your occupation: \033[0m")
                reason = input(f"\033[94m {menu1a} why do you want to join us: \033[0m\n")
                contact = input(f"\033[94m {menu1a} Email address: \033[0m")
                print(
                    f"\033[94m {menu1a} thank you for your response,we would get to you through your email\033[0m")

            elif menu1 == "2":
                menu1b = input(f"\033[94m Full name: \033[0m")
                menu1ba = input(
                    f"\033[94m Which of the following packages are you interested in?\033[0m"
                    f"\n 1. Diamond membership N500,000 \n"
                    f" 2. Silver Membership N1,500,000\n 3. Gold Membership N3,000,000\033[0m\n")
                if menu1ba == "1":
                    menu1ba = "Diamond Membership"
                    print(
                        f"\033[94m Your choice of {menu1ba} has been received and is being processed,"
                        f"\n Please wait.\033[0m\n")
                    print(f"\033[94m What is your preferred method of payment?\033[0m\n")
                    payment = input("\033[94m Choose\n 1 for card\n 2 for transfer: \033[0m")
                    if payment == "1":
                        card_details = input(f"\033[94m Card details: \033[0m")
                        card_details2 = input(f"\033[94m CCV: \033[0m")
                        card_details3 = input(f"\033[94m Date: \033[0m")
                        print(
                            f"\033[94m Your details has been recieved and the payment is been processed\n "
                            f"We would "
                            f"contact you through your email\n Thank you for choosing us.\033[0m")

                    elif payment == "2":
                        print(
                            f"\033[94m make a transfer for {menu1ba} to this account\n  Kuda MFB\n"
                            f"Account Number: 2006668080\033[0m")
                        print(
                            f"\033[94m Your details has been recieved and the payment is been processed\n"
                            f" We would contact you through your email\n Thank you for choosing us.\033[0m")
                        print("Code Designed by Josh :|")

                elif menu1ba == "2":
                    menu1ba = "Silver Membership"
                    print(
                        f"\033[94m Your choice of {menu1ba} has been recieved and is being processed,\n"
                        f"Please wait.\033[0m")
                    print(f"\033[94mWhat is your preferred method of payment?\033[0m")
                    payment = input("\033[94m\n1. for card\n2. for transfer\033[0m\n")
                    if payment == "1":
                        card_details1a = input(f"\033[94m Card details: \033[0m")
                        card_details2a = input(f"\033[94m CCV: \033[0m")
                        card_details3a = input(f"\033[94m Date: \033[0m")
                        print(
                            f"\033[94m Your details has been received and the payment is been processed\n "
                            f"We would "
                            f"contact you through your email\n Thank you for choosing us.\033[0m")
                    elif payment == "2":
                        print(
                            f"\033[94m make a transfer for {menu1ba} to this account\n  Kuda MFB\n"
                            f"Account Number: 2006668080\033[0m")
                        print(
                            f"\033[94m Your details has been recieved and the payment is been processed\n"
                            f" We would contact you through your email\n Thank you for choosing us.\033[0m")
                elif menu1ba == "3":
                    menu1ba = "Gold Membership"
                    print(
                        f"\033[94m Your choice of {menu1ba} has been recieved and is being processed,\n"
                        f"Please wait.\033[0m")
                    print(f"\033[94m What is your preferred method of payment?\033[0m")
                    payment = input("\033[94m\n1. for card\n2. for transfer\033[0m\n")
                    if payment == "1":
                        card_details1a1 = input(f"\033[94m Card details: \033[0m")
                        card_details2a2 = input(f"\033[94m CCV: \033[0m")
                        card_details3a3 = input(f"\033[94m Date: \033[0m")
                        print(
                            f"\033[94m Your details has been received and the payment is been processed\n "
                            f"We would "
                            f"contact you through your email\n Thank you for choosing us.\033[0m")

                    elif payment == "2":
                        print(
                            f"\033[94m make a transfer for {menu1ba} to this account\n  Kuda MFB\n"
                            f"Account Number: 2006668080\033[0m")
                        print(
                            f"\033[94m Your details has been recieved and the payment is been processed\n"
                            f" We would contact you through your email\n Thank you for choosing us.\033[0m")

            elif menu1 == "3":
                print(f"\033[94m The name of the organization  is Elite Global Conglomerate\n our duty is"
                      f" to help "
                      f"mankind to leave a good and healthy lifestyle\n we are group of concerned iondiviuals who "
                      f"are focussed\n on ensuring that life is made easier for people of various class\n and at "
                      f"such there are many benefits that our members are opened to which\n inlcudes but not "
                      f"limited to opportunity to meet up with those that matters in the society\n as well as "
                      f"enjoying travelling to various locations around the world.\n walk into any of our offices "
                      f"over the world to know more.\033[0m")
                service()

        elif menu == "2" or menu == "membership verification":
            mem_verify_loop = "start"
            while mem_verify_loop == "start":
                menu = "Membership Verification"
                print(f"\033[94m Please provide your Fullname and Password\033[0m")
                details = input("\033[94mFullname: \033[0m")
                details = details.capitalize()
                details1 = input("\033[94mPassword: \033[0m")
                if details in verified_username_and_password_data:
                    pass
                    if details1 in verified_username_and_password_data:
                        print(f"\033[94m Welcome {details}, your membership has been verified\033[0m")
                        print(f"\033[94m Would like to view your profiles?\033[0m")
                        ans = input(f"\033[94m Y or N: \033[0m")
                        ans = ans.capitalize()
                        if ans == "Y" or ans == "YES":
                            with open("customer.csv") as file:
                                reader = file.read()
                                list_data = reader.split("\n")
                                if f"{details}," in reader:
                                    for ran in list_data:
                                        if details in ran:
                                            name_Data = ran
                                            name_list = name_Data.split(",")
                                            print(f"\033[93mThese are your details; \nUsername: {name_list[0]}"
                                                  f"\nPassword: {name_list[1]}"
                                                f"\nFullname: {name_list[2]}\nPhone Number: {name_list[4]}\033[0m")
                                else:
                                    print(f"\033[94m Your details is not found \033[0m")
                        elif ans == "N" or ans == "NO":
                            signup()
                        mem_verify_loop = "end"
                    else:
                        print("\033[91m Please enter a correct phone number\033[0m")

                else:
                    print(f"{details} you are not a verified member, Please register!")
                    front_page()

        elif menu == "3" or menu == "membership fee":
            mem_fee_loop = "start"
            while mem_fee_loop == "start":
                menu = "Membership Fee"
                print(f"\033[94m\n1. Diamond membership N500,000 \n"f"2. Silver Membership N1,500,000\n"
                      f"3. Gold Membership N3,000,000\033[0m\n")
                details = input("\033[94m Enter package: \033[0m\n")
                details.lower()
                account = "\nBank Name:Kuda MFB\nAccount Number:2006668080"
                if details == "1" or details == "diamond Membership":
                    details_mem1 = "Diamond Membership"
                    fee1 = 500000
                    print(f"\033[94m Please make a payment of {fee1} for {details_mem1} to \n{account}")
                    print("\033[94m Please provide the name used in the payment\033[0m")
                    details_ver = input("\033[94m Name: \033[0m")
                    print("\033[94m once payment is received, you will be contacted\033[0m")
                    mem_fee_loop = "end"
                    front_page()
                elif details == "2" or details == "silver Membership":
                    details_mem1 = "Silver Membership"
                    fee2 = 1500000
                    print(f"\033[94m Please make a payment of {fee2} for {details_mem1} to \n{account}")
                    print("\033[94m Please provide the name used in the payment\033[0m")
                    details_ver = input("\033[94m Name: \033[0m")
                    print("\033[94m once payment is received, you will be contacted\033[0m")
                    mem_fee_loop = "end"
                    front_page()
                elif details == "3" or details == "Gold Membership":
                    details_mem1 = "Gold Membership"
                    fee3 = 3000000
                    print(f"\033[94m Please make a payment of {fee3} for {details_mem1} to \n{account}")
                    print("\033[94m Please provide the name used in payment\033[0m")
                    details_ver = input("\033[94m Name: \033[0m")
                    print("\033[94m once payment is received, you will be contacted\033[0m")
                    mem_fee_loop = "end"
                    front_page()
                else:
                    print("\033[94m You have entered a wrong value\033[0m")

        elif menu == "4" or menu == "speak to customer care":
            cus_loop = "start"
            while cus_loop == "start":
                menu = "Speak To Customer Care"
                print(f"\033[94m Choose: \n Y for Yes\n N for No\033[0m")
                print(f"\033[94m is this your mobile number {phone_num}\033[0m")
                num_ans = input("\033[94m Response: \033[0m")
                num_ans = num_ans.lower()
                if num_ans == "yes" or num_ans == "y":
                    print(f"\033[94m \n is this your Email address {email_address}\033[0m\n")
                    email_ans = input("\033[94m  Response: \033[0m")
                    if email_ans == "yes" or email_ans == "y":
                        print(f"\033[94m \n Your details has been sent to my supervisor, "
                              f"someone would attend to you\033\n[0m")
                    elif email_ans == "no" or email_ans == "n":
                        print(f"\033[94m Please provide your Email Address \033[0m")
                        email_ans2 = input(f"\033[94m Email address: \033[0m")
                        print(f"\033[94m \n Your details has been sent to my supervisor, "
                              f"someone would attend to you\033[0m\n")
                    cus_loop = "end"
                    front_page()
                    pass
                elif num_ans == "no" or num_ans == "n":
                    print(f"\033[94m Please Input the right number")
                    num_ans2 = input(f"\033[94m Number: \033[0m")

                else:
                    print(f"\033[94m Please provide your Details \033[0m")

        elif menu == "5" or menu == "exit":
            print("\033[93m Thank you for visiting us! Hope to see you soon\033[0m\n")
            front_page()

        else:
            print("\033[94m You have entered a wrong value\033[0m")
            print("Code Designed by Josh :|")


def login_service():
    # services offered
    service_list_loop = "start"
    while service_list_loop:
        menu = input(f"\033[94m \n1. Membership Verification \n2. "
                     "Membership Fee \n3. Speak to Customer Care \n4. Exit \033[0m\n")
        menu = menu.lower()
        if menu == "1" or menu == "membership verification":
            mem_verify_loop = "start"
            while mem_verify_loop == "start":
                menu = "Membership Verification"
                print(f"\033[94m Please provide your name and phone number\033[0m")
                details = input("\033[94mName: \033[0m")
                details = details.capitalize()
                if details in verified_username_and_password_data:
                    print(f"\033[94m \n Welcome {details}, your membership has been verified\033[0m\n")
                    service()
                    mem_verify_loop = "end"
                else:
                    print(f"\033[91m \n {details} you are not a verified member, Please register!\033[0m\n")
                    front_page()

        elif menu == "2" or menu == "membership fee":
            mem_fee_loop = "start"
            while mem_fee_loop == "start":
                menu = "Membership Fee"
                print(f"\033[94m\n1. Diamond membership N500,000 \n"f"2. Silver Membership N1,500,000\n"
                      f"3. Gold Membership N3,000,000\033[0m\n")
                details = input("\033[94m Enter package: \033[0m\n")
                details.lower()
                account = "\nBank Name:Kuda MFB\nAccount Number:2006668080"
                if details == "1" or details == "diamond Membership":
                    details_mem1 = "Diamond Membership"
                    fee1 = 500000
                    print(f"\033[94m Please make a payment of {fee1} for {details_mem1} to \n{account}")
                    print("\033[94m Please provide the name used in the payment\033[0m")
                    details_ver = input("\033[94m Name: \033[0m")
                    print("\033[94m once payment is received, you will be contacted\033[0m")
                    mem_fee_loop = "end"
                    front_page()
                elif details == "2" or details == "silver Membership":
                    details_mem1 = "Silver Membership"
                    fee2 = 1500000
                    print(f"\033[94m Please make a payment of {fee2} for {details_mem1} to \n{account}")
                    print("\033[94m Please provide the name used in the payment\033[0m")
                    details_ver = input("\033[94m Name: \033[0m")
                    print("\033[94m once payment is received, you will be contacted\033[0m")
                    mem_fee_loop = "end"
                    front_page()
                elif details == "3" or details == "Gold Membership":
                    details_mem1 = "Gold Membership"
                    fee3 = 3000000
                    print(f"\033[94m Please make a payment of {fee3} for {details_mem1} to \n{account}")
                    print("\033[94m Please provide the name used in payment\033[0m")
                    details_ver = input("\033[94m Name: \033[0m")
                    print("\033[94m once payment is received, you will be contacted\033[0m")
                    mem_fee_loop = "end"
                    front_page()
                else:
                    print("\033[94m You have entered a wrong value\033[0m")

        elif menu == "3" or menu == "speak to customer care":
            cus_loop = "start"
            while cus_loop == "start":
                menu = "Speak To Customer Care"
                print(f"\033[94m Choose: \n Y for Yes\n N for No\033[0m")
                print(f"\033[94m is this your mobile number {phone_num}\033[0m")
                num_ans = input("\033[94m Response: \033[0m")
                num_ans = num_ans.lower()
                if num_ans == "yes" or num_ans == "y":
                    print(f"\033[94m \n is this your Email address {email_address}\033[0m\n")
                    email_ans = input("\033[94m  Response: \033[0m")
                    if email_ans == "yes" or email_ans == "y":
                        print(f"\033[94m \n Your details has been sent to my supervisor, "
                              f"someone would attend to you\033\n[0m")
                    elif email_ans == "no" or email_ans == "n":
                        print(f"\033[94m Please provide your Email Address \033[0m")
                        email_ans2 = input(f"\033[94m Email address: \033[0m")
                        print(f"\033[94m \n Your details has been sent to my supervisor, "
                              f"someone would attend to you\033[0m\n")
                    cus_loop = "end"
                    front_page()
                    pass
                elif num_ans == "no" or num_ans == "n":
                    print(f"\033[94m Please Input the right number")
                    num_ans2 = input(f"\033[94m Number: \033[0m")

                else:
                    print(f"\033[94m Please provide your Details \033[0m")

        elif menu == "4" or menu == "exit":
            print("\033[93m Thank you for visiting us! Hope to see you soon\033[0m\n")
            front_page()

        else:
            print("\033[94m You have entered a wrong value\033[0m")


front_page()
