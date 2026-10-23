import random
import time

name = input("\033[92m Enter Name: \033[0m")
mother_loop = "start"
while mother_loop == "start":
    boast_package = ("kid", "adolescence", "teenager", "adult")
    print(f"\033[93m Available boaster Packages\033[0m")
    for p in boast_package:
        print(f"\033[93m {p} \033[0m")
    choice = input("\033[92m Enter choice: \033[0m")
    if choice == "kid":
        kid_loop = "start"
        while kid_loop == "start":
            tap = input("\033[92m Type enter to boast: \033[0m")
            if tap == "":
                tap_balance = 1000 + random.randint(5000, 9999)
                print(f"\033[93m {tap_balance} \033[0m")
                max_tap = tap_balance + random.randint(500, 1000)
                time.sleep(2)
                if max_tap >= 10000:
                    print("\033[93m you cannot upgrade this boaster }\033[0m")
                    kid_loop = "end"

                else:
                    pass

        else:
            print(f"\033[91m Please click on Enter\033[0m\n")

    if choice == "adolescence":
        kid_loop = "start"
        while kid_loop == "start":
            tap = input("\033[92m Type enter to boast: \033[0m")
            if tap == "":
                tap_balance = 3000 + random.randint(15000, 40000)
                print(f"\033[93m {tap_balance} \033[0m")
                max_tap = tap_balance + random.randint(500, 1000)
                time.sleep(2)
                if max_tap >= 45000:
                    print("\033[93m you cannot upgrade this boaster }\033[0m")
                    kid_loop = "end"

                else:
                    pass

            else:
                print(f"\033[91m Please click on Enter\033[0m\n")

    if choice == "teenager":
        kid_loop = "start"
        while kid_loop == "start":
            tap = input("\033[92m Type enter to boast: \033[0m")
            if tap == "":
                tap_balance = 5000 + random.randint(5000, 55000)
                print(f"\033[93m {tap_balance} \033[0m")
                max_tap = tap_balance + random.randint(500, 1000)
                time.sleep(2)
                if max_tap >= 60000:
                    print("\033[93m you cannot upgrade this boaster}\033[0m")
                    kid_loop = "end"

                else:
                    pass

            else:
                print(f"\033[91m Please click on Enter\033[0m\n")

    if choice == "adult":
        kid_loop = "start"
        while kid_loop == "start":
            tap = input("\033[92m Type enter to boast: \033[0m")
            if tap == "":
                tap_balance = 10000 + random.randint(5000, 99999)
                print(f"\033[93m {tap_balance} \033[0m")
                max_tap = tap_balance + random.randint(500, 1000)
                time.sleep(2)
                if max_tap >= 100000:
                    print("\033[93m you cannot upgrade this boaster}\033[0m")
                    kid_loop = "end"

                else:
                    pass

            else:
                print(f"\033[91m Please click on Enter\033[0m\n")
