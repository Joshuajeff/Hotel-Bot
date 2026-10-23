# josh
import random
import datetime
import calendar
# happiness
import time

# muspley
names = """Josh
Muspley
Happiness
Titi
"""
# count = 0
# for i in range(100):
# count += 1
# print(f"{count} \033[{count}mCOLOUR\033[0m")
try:
    with open("Presentation.csv", "r") as file:
        book = file.read()
    if book == "":
        with open("Presentation.csv", "w") as file:
            file.write(names)

except:
    with open("Presentation.csv", "w") as file:
        file.write(names)

    with open("Presentation.csv", "r") as file:
        book = file.read()
#
try:
    with open("Presented.csv", "r") as file:
        file.read()
except:
    with open("Presented.csv", "w") as file:
        file.write("")
#
try:
    with open("Presenting.csv", "r") as file:
        file.read()  # ERROR-IS-HERE
except:
    with open("Presenting.csv", "w") as file:
        file.write("")

presenters = book.split()
period = datetime.datetime.now()
today = period.strftime('%A')
######
todays_date = datetime.datetime.now()
year = todays_date.year
month = todays_date.month
day = todays_date.day
week_day = calendar.weekday(year, month, day)
daily = period.day

weekday = ""
######
# while presenters != []:
if week_day == 0:
    this_day = "Monday"
elif week_day == 1:
    this_day = "Tuesday"
elif week_day == 2:
    this_day = "Wednesday"
elif week_day == 3:
    this_day = "Thursday"
elif week_day == 4:
    this_day = "Friday"
elif week_day == 5:
    this_day = "Saturday"
elif week_day == 6:
    this_day = "Sunday"
else:
    pass

with open("Presentation.csv", "r") as file:
    remaining_names = file.read()

if remaining_names == "":
    with open("Presentation.csv", "w") as file:
        file.write(names)

# changing  the month from integer to name of month
the_month = period.month
if the_month == 1:
    this_month = "Jan."
elif the_month == 2:
    this_month = "Feb."
elif the_month == 3:
    this_month = "Mar."
elif the_month == 4:
    this_month = "Apr."
elif the_month == 5:
    this_month = "May"
elif the_month == 6:
    this_month = "June"
elif the_month == 7:
    this_month = "July"
elif the_month == 8:
    this_month = "Aug."
elif the_month == 9:
    this_month = "Sept."
elif the_month == 10:
    this_month = "Oct."
elif the_month == 11:
    this_month = "Nov."
elif the_month == 12:
    this_month = "Dec."
else:
    this_month = "Month is not defined"

# Adding 1st, 2nd etc to day of the month
teent = ""
if str(daily)[-1] == "1":
    teent = "st"
elif str(daily)[-1] == "2":
    teent = "nd"
elif str(daily)[-1] == "3":
    teent = "rd"
else:
    teent = "th"

endless_loop = "Yes"
while endless_loop == "Yes":
    print("\033[51m CYBER SECURITY PRESENTERS RANDOMIZER \033[0m")
    # This helps make sure choose a number from the option
    number_only = "False"
    while number_only == "False":
        print()
        choose = input(
            "1. Presenting now\n2. Presented last\n3. Presenting next\n4. Presented list\n5. Run Randomizer\n")
        if choose.isnumeric():
            # convert choose to integer
            if int(choose) >= 1 and int(choose) <= 5:
                number_only = "True"
                # break
            else:
                print("\033[31mPlease enter a number between 1 and 5.\033[0m")
        else:
            print("\033[31mPlease enter a number between 1 and 5.\033[0m")

    if str(choose) == "1":
        with open("Presenting.csv", "r") as file:
            check = file.read()

        if check == "":
            print("Please run the Randomizer first.")
        else:
            today_presenter = check.split()
            name = today_presenter[0]
            print()

            message = (f"\033[1m{name}\033[0m is schedule to present at \033[1m9:00pm\033[0m today \033[1m{this_day}, "
                       f"{daily}{teent} of {this_month}, {period.year}.\033[0m\n")
            print(message)
            print()
            input("\033[94mEnter any key to continue. \033[0m")

    if str(choose) == "2":
        with open("Presented.csv", "r") as file:
            check = file.read()

        if check == "":
            print("Please run the Randomizer first.")
        else:
            convert_to_list = check.split("\n")
            get_last_element = convert_to_list[-2]
            print()
            print(get_last_element)

            input("\033[94mEnter any key to continue. \033[0m")

    # work in progress
    if str(choose) == "3":
        pass
    if str(choose) == "4":
        print()

        # this helps print the last 10 people who has presented.
        with open("Presented.csv", "r") as file:
            check_presented = file.read()
        convert_to_list = check_presented.split("\n")
        last_ten_presented = convert_to_list[-11:]
        for i in last_ten_presented:
            print(i)

        input("\033[94mEnter any key to continue. \033[0m")

        pass
    elif str(choose) == "5":
        print()

        with open("Presenting.csv", "r") as file:
            check_for_empty = file.read()

        check_for_name = check_for_empty.split()

        if check_for_empty == "":
            random.shuffle(presenters)
            presenting_now = presenters.pop()
            remaining_presenters = "\n".join(presenters)

            with open("Presentation.csv", "w") as file:
                file.write(remaining_presenters)

            message = (
                f"\033[1m{presenting_now}\033[0m is presenting from \033[1m9:00pm\033[0m today \033[1m{this_day}, "
                f"{daily}{teent} of {this_month}, {period.year}.\033[0m\n")
            print(message)
        else:
            first_name = check_for_name[0]
            message = (f"\033[1m{first_name}\033[0m is presenting from \033[1m9:00pm\033[0m today \033[1m{this_day}, "
                       f"{daily}{teent} of {this_month}, {period.year}.\033[0m\n")
            print(message)

        timer = 3
        # print(seconds)

        # print(minutes)
        import sys

        for i in range(timer, -1, -1):
            time.sleep(1)
            seconds = int(i % 60)
            minutes = int((i / 60) % 60)
            timer -= 1
            sys.stdout.write("\r" + f"\033[1mTIME LEFT:\033[0m \033[51m {minutes:02}:{seconds:02} \033[0m")
        print("\n")
        # print(timer)

        if check_for_empty == "":
            has_presented = f"{presenting_now} presented on {this_day} {daily} - {period.month} - {period.year}\n"

            with open("Presented.csv", "a") as file:
                file.write(has_presented)
        else:
            has_presented = f"{first_name} presented on {this_day} {daily} - {period.month} - {period.year}\n"

            with open("Presented.csv", "a") as file:
                file.write(has_presented)

        # This helps us to increment the daily to a future date
        week_day += 1
        daily += 1

        if week_day == 0:
            this_day = "Monday"
        elif week_day == 1:
            this_day = "Tuesday"
        elif week_day == 2:
            this_day = "Wednesday"
        elif week_day == 3:
            this_day = "Thursday"
        elif week_day == 4:
            this_day = "Friday"
        elif week_day == 5:
            this_day = "Saturday"
        elif week_day == 6:
            this_day = "Sunday"
        else:
            pass

        # presenting_next = presenters.pop()
        with open("Presentation.csv", "r") as file:
            book_2 = file.read()
        presenting_next = book_2.split()
        random.shuffle(presenting_next)
        presenting_next2 = presenting_next.pop()
        new_message = "\n".join(presenting_next)

        with open("Presentation.csv", "w") as file:
            file.write(new_message)

        #### ERROR
        with open("Presentation.csv", "r") as file:
            check_if_empty = file.read()
        if check_if_empty == "":
            with open("Presentation.csv", "w") as file:
                file.write(names)
        ## ERROR
        message_2 = (
            f"\033[1m{presenting_next2}\033[0m is scheduled to present by \033[1m9:00pm\033[0m tomorrow \033[1m{this_day}, "
            f"{daily}{teent} of {this_month}, {period.year}.\033[0m\n")
        with open("Presenting.csv", "w") as file:
            file.write(message_2)
        print(message_2)

        input("\n\n033[94mPress enter to continue.\033[0m")
        # reset the week_day and daily
        week_day -= 1
        daily -= 1


    elif str(choose) == "2":
        pass