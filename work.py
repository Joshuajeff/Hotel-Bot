fullname = input("\033[34mEnter Fullname:  \033[0m")
fullname = fullname.capitalize()
password = input("\033[34mEnter Password: \033[0m")
with (open('customer.csv', 'r') as file):
    names = file.read()
    new_details = names.split("\n")
    if f"{fullname}," in names:
        print("yes")
        for users in new_details:
            if fullname in users:
                real_name = users
                main_name = real_name.split(",")
                if fullname == main_name[2]:
                    print("yes")
                cus_data = input("\033[34mDo you want to view your details?\n Y or N: \033[0m")
                cus_data = cus_data.capitalize()
                if cus_data == "Y" or cus_data == "YES":
                    print(f"\033[93mThese are your details; \nUsername: {main_name[0]}"
                          f"\nPassword: {main_name[1]}"
                          f"\nFullname: {main_name[2]}\nPhone Number: {main_name[4]}\033[0m")
                elif cus_data == "N" or cus_data == "NO":
                    username_loop = "end"

        else:
            print(f"\033[94m Your details is not found \033[0m")
