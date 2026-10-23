import csv
import random
from csv import DictReader

database = []

print("\U0001f600")
with open("hotel details1.csv") as file:
    reader = file.read()
    details = reader.split("\n")
for ran in details:
    if "josh" in ran:
        user_data = ran.split(",")
        print(f"Username: {user_data[0]}")
        print(f"Password: {user_data[1]}")
        print(f"Fullname: {user_data[2]}")
        print(f"Phone Number: {user_data[3]}")
    # grinning face
    #print("\N{grinning face}")

    # slightly smiling face
    #print("\N{slightly smiling face}")

    # winking face
    #print("\N{winking face}")

    #for row in :
    #   name = f"Username: {row['Username']}"
    #  print(f"{name[0], [11]}")

#file = open("customer_data.csv", 'r', encoding="utf8")
#csv_reader = DictReader(file)
#for row in csv_reader:
#print(row)

#file.close()


#data_new = file.read()
#list_new = data_new.split()
#add = " ".join(list_new)
#for new in add:
#print(new)

list = "Wisdom", "Floxy", "Damilola", "Maria", "Telema", "Ernest", "Chinedu",
list_one = ["Josh", "Xta", "emeka", "men"]
list_two = ["Jane", "Jerry", "jeff", "ada"]
random.shuffle(list_one)
data = random.choices(list_two, k=4)
names = random.choices(list_one, k=4)
entries = ("Muzuos Collection", "Mcjoi World", "Sk", "Sophie", "Ahmad D", "Nezuko", "Estelina", "Telema", "Jikeola",
           "Ola", "Haryormhide", "Bangbose", "Best FLoxy", "Thoursy", "Love D")
print(names)

import random

team_1 = ["Samuel",
          "Mercy",
          "Mariam",
          "Ajike",
          ]

team_2 = ["Ibukun",
          "Grace",
          "Love",
          "Lizzy",
          ]

random.shuffle(team_1)
random.shuffle(team_2)
sub = "\033[4m\033[1mALX ACCOUNTABILITY PARTNERS\033[0m\033[0m"
list = "\033[4m\033[1mSECOND LIST\033[0m\033[0m"
print(f"\n{sub:>49}\n")
count = 0
for tutor, topic in zip(team_1, team_2):
    print(f"\033[34m {tutor} and {topic} \033[0m")


#verified_user_and_password = ["josh, 12345678, 08067513974"]
#username_loop = "start"
#while username_loop == "start":
#username = input("\033[34mEnter Username:  \033[0m")
#username = username.lower()
#for users in verified_user_and_password:
#if username in users:
# username_loop = "end"
#pass_loop = "start"
#while pass_loop == "start":
#password = input("\033[34mEnter Password: \033[0m")
#details = users.split(", ")
# if password == details[1]:
#    pass_loop = "end"
#else:
#    print("\033[31mYou have entered a wrong detail \033[0m")
#else:
#  print("\033[31mYou have entered a wrong detail \033[0m")
