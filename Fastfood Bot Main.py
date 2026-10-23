import math

room_order = ""
room_num = ""
room_price = ""
response = ""
response_input = ""
soup_order = ""
soup_number = ""
swallow_input = ""
swallow_number = ""
menu_order = ""
menu_portion = ""
rice_order = ""
rice_Portion = ""
protein_order = ""
protein_portion = ""
drink_order = ""
drink_portion = ""
water_portion = ""
drink_input = ""
water_order = ""
water_input = ""
total_swallow = 0
total_soup = 0
total_menu_order = 0
total_rice = 0
total_protein = 0
total_drink = 0
total_water = 0
grand_total = 0
room_cost = 0



def listdict(a_list):
    key_value = {}
    key = 0
    value = 0
    add_key = 1
    add_value = 2
    ls_index = 0
    for i in a_list:
        key += 1
        value += 1
        # add key to dictionary
        if key == add_key:
            key_value.update({i: i})
            add_key += 2
        # adds value to dictionary
        if value == add_value:
            key_value.update({a_list[ls_index]: i})
            ls_index += 2
            add_value += 2
    return key_value

#bookins menu
def booking():
    global room_order
    global room_num
    global room_cost
    global room_price
    global response
    global response_input
    booking_loop = "start"
    while booking_loop == "start":
        print(f"\033[93m         Welcome, be rest assured of comfort\033[0m")
        print("\033[93m         These are our Available luxurious Rooms\033[0m\n")
        rooms = {"1. Standard Room": "N250,000",
                 "2. Deluxe Room": "N450,000",
                 "3. Executive Room": "N700,000",
                 "4. Presidential Suite": "N1,200,000"}
        for key, value in rooms.items():
            print(f"\033[93m{key}: {value}\033[0m\n")

        room_order = input(f"\033[34mMake your choice: \033[0m")
        room_order = room_order.capitalize()
        if room_order == "Standard Room" or room_order == "1":
            room_order = "Standard Room"
            print("\033[94m Benefits of choosing this room includes:\n1. A 6 by 6 beds \n2. Art Deco-Style room \n3. "
                  "Marble Bathroom with separate bath, toilet and bidet\n4. Wifi and a wonderful view of the city "
                  "and a one time complimentary coffee\033[0m\n")
            price = 250000
            print("\033[94m How Long do you intend to stay\033[0m\n")
            room_num = int(input("\033[34mDuration in day(s): \n \033[0m"))
            if int(room_num) > 7:
                print("\033[94m You have been granted a 10% discount for\n Your booking\033[0m")
                room_cost = price * int(room_num) - (0.1 * price)
                print(f"\033[94m The Cost of {room_num} Days is N{str(math.ceil(room_cost))}\033[0m\n")
                booking_loop = "end"

            else:
                room_price = price * room_num
                print(f"\033[94m The Cost of {room_num} Days is N{str(math.ceil(room_price))}\033[0m\n")
                booking_loop = "end"

        elif room_order == room_order == "Deluxe Room" or room_order == "2":
            room_order = "Deluxe Room"
            print("\033[94m Benefits of choosing this room includes:\n1. 2 6 by 6 beds \n2. Art Deco-Style room \n3. "
                  "Marble Bathroom with separate bath, toilet and bidet\n4. Wifi and a wonderful view of the city "
                  "and a one time complimentary coffee\033[0m\n")
            price = 450000
            print("\033[94m How Long do you intend to stay\033[0m\n")
            room_num = int(input("\033[34mDuration in day(s): \n \033[0m"))
            if int(room_num) > 7:
                print("\033[94m You have been granted a 10% discount for\n Your booking\033[0m")
                room_cost = price * int(room_num) - (0.1 * price)
                print(f"\033[94m The Cost of {room_num} Days is N{str(math.ceil(room_cost))}\033[0m\n")
                booking_loop = "end"

            else:
                room_price = price * room_num
                print(f"\033[94m The Cost of {room_num} Days is N{str(math.ceil(room_price))}\033[0m\n")
                booking_loop = "end"
        elif room_order == "Executive Room" or room_order == "3":
            room_order = "Executive Room"
            print("\033[94m Benefits of choosing this room includes:\n1. A king size bed \n2. A curved 4k television "
                  "display\n3. Art Deco-Style room \n4. Marble Bathroom with separate bath, toilet and bidet\n5. Wifi "
                  "and a wonderful view of the city, including a complimentary coffee"
                  " depending on your duration\033[""0m\n")
            price = 700000
            print("\033[94m How Long do you intend to stay\033[0m\n")
            room_num = int(input("\033[34mDuration in day(s): \n \033[0m"))
            if int(room_num) > 7:
                print("\033[94m You have been granted a 10% discount for\n Your booking\033[0m")
                room_cost = price * int(room_num) - (0.1 * price)
                print(f"\033[94m The Cost of {room_num} Days is N{str(math.ceil(room_cost))}\033[0m\n")
                booking_loop = "end"

            else:
                room_price = price * room_num
                print(f"\033[94m The Cost of {room_num} Days is N{str(math.ceil(room_price))}\033[0m\n")
                booking_loop = "end"

        elif room_order == "Presidential Suite" or room_order == "4":
            room_order = "Presidential Suite"
            print(
                f"\033[94m This is our peak of luxury, a night here would offer you\na breathtaking view of the city "
                f"and"
                "the ocean, coupled with king size bed,\na cinematic view display for any movies of your choice\na "
                "complimentary breakfast and dinner, 3 cups of coffe daily.\033[0m\n")
            price = 1200000
            print("")
            print("\033[94m How Long do you intend to stay\033[0m\n")
            room_num = int(input("\033[34mDuration in day(s): \n \033[0m"))
            if int(room_num) > 7:
                print("\033[94m You have been granted a 10% discount for\n Your booking\033[0m\n")
                room_cost = price * int(room_num) - (0.1 * price)
                print(f"\033[94m The Cost of {room_num} Days is N{str(math.ceil(room_cost))}\033[0m\n")
                print("\033[94m Would you like a companion for the night, as a courtesy from us?\033[0m\n")
                response = input(f"\033[34mYes or No: \n \033[0m")
                response = response.capitalize()
                if response == "Yes":
                    response_input = input(f"\n\033[34mWhat is your Specification: \n \033[0m")
                    print(f"\033[94mThank you for your response, Your Specification is {response_input}\033[0m\n")
                    print("\033[94mWe would get back to you shortly\033[0m\n")
                    booking_loop = "end"

                else:
                    print("\033[94mThank you for your response\033[0m")
                    booking_loop = "end"

            else:
                room_price = price * room_num
                print(f"\033[94m The Cost of {room_num} Days is N{str(math.ceil(room_price))}\033[0m\n")
                booking_loop = "end"

#kitchen Menu
def kitchen():
    global total_soup
    global total_swallow
    global total_rice
    global rice_toppings
    global total_drink
    global total_water
    global total_rice
    global total_menu_order
    global total_protein
    global soup_order
    global soup_number
    global swallow_input
    global swallow_number
    global menu_order
    global menu_portion
    global rice_order
    global rice_Portion
    global protein_order
    global protein_portion
    global drink_order
    global drink_input
    global drink_portion
    global water_order
    global water_input
    global water_portion
    global grand_total

    kitchen_loop = "start"
    while kitchen_loop == "start":
        print(f"\033[94m Welcome this is our available menu\033[0m\n")

        menu = ["1. Soup"]
        menu.extend(
            ["2. Abacha N1500", "3. Yam Porridge N1500", "4. Rice", "5. Spaghetti Bolognese N3000", "6. Pizza N4000",
             "7. Plantain N1000"])

        (food1, food2, food3, food4, food5, food6, food7,
         ) = menu
        print(f"\033[93m{food1 + "\n" + food2 + "\n" + food3 + "\n" + food4 + "\n" + food5 + "\n" + food6 + "\n"
                         + food7}\033[0m\n")
        menu_order = input("\n\033[34mWhat do we serve you? \n \033[0m")
        menu_order = menu_order.capitalize()
        # soup menu
        if menu_order == "Soup" or menu_order == "1":
            menu_order = "Soup"
            soup_loop = "start"
            while soup_loop == "start":
                print(f"\033[94m Below is our menu for Soup\033[0m\n")
                # soup menu
                soup_menu = "a. Ewedu N1000 \nb. Equsi N1000 \nc. Oha N1000 \nd. Okro N1000 \ne. Vegetable N1500 \n"
                print(f"\033[94m{soup_menu}\033[0m\n")
                soup_order = input("\033[34mWhat Soup do you need? \n \033[0m")
                soup_order = soup_order.capitalize()
                # soup Prices
                if soup_order == "Ewedu" or soup_order == "A":
                    soup_order = "Ewedu"
                    soup_price = 1000
                    soup_number = input(f"\033[34mHow Many portion of  {soup_order} do you need? \n \033[0m")
                    print(f"\033[94mThank you Your order for {soup_number} portion of {soup_order}"
                          f" has been recieved and is being processed\033[0m")
                    total_soup = soup_price * int(soup_number)
                    print(f"\033[91m The cost of your order for {soup_number} Portion of {soup_order}"
                          f"  is N{str(total_soup)}\033[0m\n")
                    soup_loop = "end"

                elif soup_order == "Equsi" or soup_order == "B":
                    soup_order = "Equsi"
                    soup_price = 1000
                    soup_number = input(f"\033[34mHow Many portion of  {soup_order} do you need? \n \033[0m")
                    print(f"\033[94mThank you Your order for {soup_number} portion of {soup_order}"
                          f" has been recieved and is being processed\033[0m")
                    total_soup = soup_price * int(soup_number)
                    print(f"\033[91m The cost of your order for {soup_number} Portion of {soup_order}"
                          f"  is N{str(total_soup)}\033[0m\n")
                    soup_loop = "end"

                elif soup_order == "Oha" or soup_order == "C":
                    soup_order = "Oha"
                    soup_price = 1000
                    soup_number = input(f"\033[34mHow Many portion of  {soup_order} do you need? \n \033[0m")
                    print(f"\033[94mThank you, Your order for {soup_number} portion of {soup_order}"
                          f" has been recieved and is being processed\033[0m")

                    total_soup = soup_price * int(soup_number)
                    print(f"\033[91m The cost of your order for {soup_number} Portion of {soup_order}"
                          f"  is N{str(total_soup)}\033[0m\n")
                    soup_loop = "end"

                elif soup_order == "Okro" or soup_order == "D":
                    soup_order = "Okro"
                    soup_price = 1000
                    soup_number = input(f"\033[34mHow Many portion of  {soup_order} do you need? \n \033[0m")
                    print(f"\033[91m The cost of your order for {soup_number} Portion of {soup_order}"
                          f"  is N{str(total_soup)}\033[0m\n")
                    total_soup = soup_price * int(soup_number)
                    print(f"\033[91m The cost of your order for {soup_number} Portion of {soup_order}"
                          f"  is N{str(total_soup)}\033[0m\n")
                    soup_loop = "end"

                elif soup_order == "Vegetable" or soup_order == "E":
                    soup_order = "Vegetable"
                    soup_price = 1500
                    soup_number = input(f"\033[34mHow Many portion of  {soup_order} do you need? \n \033[0m")
                    print(f"\033[94mThank you, Your order for {soup_number} portion of {soup_order}"
                          f" has been received and is being processed\033[0m")
                    total_soup = soup_price * int(soup_number)
                    print(f"\033[91m The cost of your order for {soup_number} Portion of {soup_order}"
                          f"  is N{str(total_soup)}\033[0m\n")
                    soup_loop = "end"

                else:
                    price = 0
                # swallow menu
            swallow_loop = "start"
            while swallow_loop == "start":
                print(
                    f"\033[94m Below is our swallow menu\na. Amala N100\nb. Fufu N120\nc. Eba N130 \nd. Semo "
                    f"N140\033[0m\n")
                swallow_input = input(f"\033[34mWhat Swallow would you prefer?\n \033[0m")
                swallow_input = swallow_input.capitalize()
                if swallow_input == "Amala" or swallow_input == "A":
                    swallow_input = "Amala"
                    swallow_price = 100
                    swallow_number = input(f"\033[34mHow many portion of {swallow_input} do you need?\n \033[0m")
                    print(
                        f"\033[94mYour order for {swallow_number} portion of {swallow_input}  is been processed\033[0m")
                    total_swallow = swallow_price * int(swallow_number)
                    print(f"\033[94mThe cost of your {swallow_number} portion of {swallow_input}\nis"
                          f" N{str(total_swallow)}\033[0m")
                    swallow_loop = "end"
                elif swallow_input == "Fufu" or swallow_input == "B":
                    swallow_input = "Fufu"
                    swallow_price = 120
                    swallow_number = input(f"\033[34mHow many portion of {swallow_input} do you need?\n \033[0m")
                    print(
                        f"\033[94mYour order for {swallow_number} portion of {swallow_input}  is been processed\033[0m")
                    total_swallow = swallow_price * int(swallow_number)
                    print(f"\033[94mThe cost of your {swallow_number} portion of {swallow_input}\nis"
                          f" N{str(total_swallow)}\033[0m")
                    swallow_loop = "end"
                elif swallow_input == "Eba" or swallow_input == "C":
                    swallow_input = "Eba"
                    swallow_price = 130
                    swallow_number = input(f"\033[34mHow many portion of {swallow_input} do you need?\n \033[0m")
                    print(
                        f"\033[94mYour order for {swallow_number} portion of {swallow_input}  is been processed\033[0m")
                    total_swallow = swallow_price * int(swallow_number)
                    print(f"\033[94mThe cost of your {swallow_number} portion of {swallow_input}\nis"
                          f" N{str(total_swallow)}\033[0m")
                    swallow_loop = "end"

                elif swallow_input == "Semo" or swallow_input == "D":
                    swallow_input = "Semo"
                    swallow_price = 100
                    swallow_number = input(f"\033[34mHow many portion of {swallow_input} do you need?\n \033[0m")
                    print(
                        f"\033[94mYour order for {swallow_number} portion of {swallow_input}  is been processed\033[0m")
                    total_swallow = swallow_price * int(swallow_number)
                    print(f"\033[94mThe cost of your {swallow_number} portion of {swallow_input}\nis"
                          f" N{str(total_swallow)}\033[0m")
                    swallow_loop = "end"
                else:
                    price = 0

        # food menu
        if menu_order == "Rice" or menu_order == "4":
            menu_order = "Rice"
            # Rice Menu
            rice_loop = "start"
            while rice_loop == "start":
                print(f"\033[93mPlease Make your choice\n1. Jellof Rice\n2. Fried Rice\n3. White Rice\n"
                      "4. Coconut Rice\n5. Ofada Rice\n6. Chinese Rice\033[0m\n")
                rice_order = input("\033[34mEnter your choice\n \033[0m")
                rice_order = rice_order.capitalize()
                if rice_order == "Jellof Rice" or rice_order == "1":
                    rice_order = "Jellof Rice"
                    rice_price = 2500
                    rice_portion = input(f"\033[34mHow Many Portion of {rice_order} do you need? \n \033[0m")
                    print(
                        f"\033[94mYour order for {rice_portion} portion of {rice_order} has been received\nand is been "
                        f"processed\033[0m\n")
                    total_rice = rice_price * int(rice_portion)
                    print(f"\033[94mThank you, the cost of your order is N{str(total_rice)}\033[0m")
                    rice_loop = "end"
                elif rice_order == "Fried Rice" or rice_order == "2":
                    rice_order = "Fried Rice"
                    rice_price = 2500
                    rice_portion = input(f"\033[34mHow Many Portion of {rice_order} do you need? \n \033[0m")
                    print(
                        f"\033[94mYour order for {rice_portion} portion of {rice_order} has been received\nand is been "
                        f"processed\033[0m\n")
                    total_rice = rice_price * int(rice_portion)
                    print(f"\033[94mThank you, the cost of your order is N{str(total_rice)}\033[0m")
                    rice_loop = "end"

                elif rice_order == "White Rice" or rice_order == "3":
                    rice_toppings = input(f"\033[94m Do you need Stew or Sauce?\033[0m\n")
                    rice_order = "white Rice and " + rice_toppings
                    rice_price = 2500
                    rice_portion = input(f"\033[34mHow Many Portion of {rice_order} do you need? \n \033[0m")
                    print(
                        f"\033[94mYour order for {rice_portion} portion of {rice_order} has been received\nand is been "
                        f"processed\033[0m\n")
                    total_rice = rice_price * int(rice_portion)
                    print(f"\033[94mThank you, the cost of your order is N{str(total_rice)}\033[0m")
                    rice_loop = "end"

                elif rice_order == "Coconut Rice" or rice_order == "4":
                    rice_order = "Coconut Rice"
                    rice_price = 3000
                    rice_portion = input(f"\033[34mHow Many Portion of {rice_order} do you need? \n \033[0m")
                    print(
                        f"\033[94mYour order for {rice_portion} portion of {rice_order} has been received\nand is been "
                        f"processed\033[0m\n")
                    total_rice = rice_price * int(rice_portion)
                    rice_loop = "end"
                    print(f"\033[94mThank you, the cost of your order is N{str(total_rice)}\033[0m")
                elif rice_order == "Ofada Rice" or rice_order == "5":
                    rice_order = "Ofada Rice"
                    rice_price = 3000
                    rice_portion = input(f"\033[34mHow Many Portion of {rice_order} do you need? \n \033[0m")
                    print(
                        f"\033[94mYour order for {rice_portion} portion of {rice_order} has been received\nand is been "
                        f"processed\033[0m\n")
                    total_rice = rice_price * int(rice_portion)
                    print(f"\033[94mThank you, the cost of your order is N{str(total_rice)}\033[0m")
                    rice_loop = "end"
                elif rice_order == "Chinese Rice" or rice_order == "5":
                    rice_order = "Chinese Rice"
                    rice_price = 3000
                    rice_portion = input(f"\033[34mHow Many Portion of {rice_order} do you need? \n \033[0m")
                    print(
                        f"\033[94mYour order for {rice_portion} portion of {rice_order} has been received\nand is been "
                        f"processed\033[0m\n")
                    total_rice = rice_price * int(rice_portion)
                    print(f"\033[94mThank you, the cost of your order is N{str(total_rice)}\033[0m")
                    rice_loop = "end"


                else:
                    price = 0

        elif menu_order == "Abacha" or menu_order == "2":
            menu_order = "Abacha"
            price = 1500
            menu_portion = input(f"\033[34mHow Many Portion of {menu_order} do you need? \n\033[0m")
            print(f"\033[94mYour order for {menu_portion} portion of {menu_order}"
                  f" has been received\nand is been processed\033[0m\n")

            total_menu_order = price * int(menu_portion)
            print(f"\033[91mThank You, the total cost of your order is N{str(total_menu_order)}\033[0m")

        elif menu_order == "Yam Porridge" or menu_order == "3":
            menu_order = "Yam Porridge"
            price = 1500
            menu_portion = input(f"\033[34mHow Many Portion of {menu_order} do you need? \n\033[0m")
            print(
                f"\033[91mYour order for {menu_portion} portion of {menu_order} has been received\nand is been "
                f"processed\033[0m\n")
            total_menu_order = price * int(menu_portion)
            print(f"\033[94mThank You, the total cost of your order is N{str(total_menu_order)}\033[0m")

        elif menu_order == "Spaghetti Bolognese" or menu_order == "5":
            menu_order = "Spaghetti"
            price = 3000
            menu_portion = input(f"\033[34mHow Many Portion of {menu_order} do you need? \n\033[0m")
            print(f"\033[91mYour order for {menu_portion} portion of {menu_order}"
                  f" has been received\nand is been processed\033[0m\n")
            total_menu_order = price * int(menu_portion)
            print(f"\033[91mThank You, the total cost of your order is N{str(total_menu_order)}\033[0m")
        elif menu_order == "Pizza" or menu_order == "6":
            menu_order = "Pizza"
            price = 4000
            menu_portion = input(f"\033[34mHow Many Portion of {menu_order} do you need? \n\033[0m")
            print(f"\033[91mYour order for {menu_portion} portion of {menu_order}"
                  f" has been received\nand is been processed\033[0m\n")
            total_menu_order = price * int(menu_portion)
            print(f"\033[91mThank You, the total cost of your order is N{str(total_menu_order)}\033[0m")
        elif menu_order == "Plantain" or menu_order == "7":
            menu_order = "Plantain"
            price = 1000
            menu_portion = input(f"\033[34mHow Many Portion of {menu_order} do you need? \n\033[0m")
            print(f"\033[91mYour order for {menu_portion} portion of {menu_order}"
                  f" has been received\nand is been processed\033[0m\n")
            total_menu_order = price * int(menu_portion)
            print(f"\033[91mThank You, the total cost of your order is N{str(total_menu_order)}\033[0m")
        else:
            price = 0

        protein_loop = "start"
        while protein_loop == "start":
            print(
                f"\033[93mWhat Protein do you need?\nWe have:\n1. Chicken \n2. Cat Fish \n3. Turkey \n4. Crocker"
                f"Fish\033[0m\n")
            protein_order = input(f"\033[34mEnter Your choice:\n\033[0m")
            protein_order = protein_order.capitalize()
            if protein_order == "Chicken" or protein_order == "1":
                protein_order = "Chicken"
                protein_price = 1500
                protein_portion = input(f"\033[34mHow Many portion of {protein_order} do you need\n\033[0m")
                print(
                    f"\033[94mYour order for {protein_portion} portion of {protein_order} "
                    f"has been received\nand is been "
                    f"processed\033[0m\n")

                total_protein = protein_price * int(protein_portion)
                print(f"\033[94mThank You, the cost of your order is N{str(total_protein)}\033[0m\n")
                protein_loop = "end"
            elif protein_order == "Cat Fish" or protein_order == "2":
                protein_order = "Cat Fish"
                protein_price = 2500
                protein_portion = input(f"\033[34mHow Many portion of {protein_order} do you need\n\033[0m")
                print(
                    f"\033[94mYour order for {protein_portion} portion of {protein_order} has been received\nand is been "
                    f"processed\033[0m\n")
                total_protein = protein_price * int(protein_portion)
                print(f"\033[94mThank You, the cost of your order is N{str(total_protein)}\033[0m\n")
                protein_loop = "end"
            elif protein_order == "Turkey" or protein_order == "3":
                protein_order = "Turkey"
                protein_price = 2500
                protein_portion = input(f"\033[34mHow Many portion of {protein_order} do you need\n\033[0m")
                print(
                    f"\033[94mYour order for {protein_portion} portion of {protein_order} has been received\nand is been "
                    f"processed\033[0m\n")
                total_protein = protein_price * int(protein_portion)
                print(f"\033[94mThank You, the cost of your order is N{str(total_protein)}\033[0m\n")
                protein_loop = "end"

            elif protein_order == "Crocker" or protein_order == "4":
                protein_order = "Crocker"
                protein_price = 2000
                protein_portion = input(f"\033[34mHow Many portion of {protein_order} do you need\n\033[0m")
                print(
                    f"\033[94mYour order for {protein_portion} portion of {protein_order} has been received\nand is been "
                    f"processed\033[0m\n")
                total_protein = protein_price * int(protein_portion)
                print(f"\033[94mThank You, the cost of your order is N{str(total_protein)}\033[0m\n")
                protein_loop = "end"

            else:
                price = 0
        drink_loop = "start"
        while drink_loop == "start":
            print(f"\033[93mWhat drink would you like?\033[0m\n")
            print(f"\033[93m1. Water\n2. Malt\n3. Fanta\n4. Coke\n5. Sprite\033[0m\n")
            drink_input = input(f"\033[34mEnter: \n\033[0m")
            drink_input = drink_input.capitalize()
            if drink_input == "Water" or drink_input == "1":
                drink_input = "Water"
                print(f"\033[93mMake your choice\n1. Big Size(1.5cl) N2000\n2. Medium Size(75cl) N1500\n3."
                      f" Small Size(50cl) N1000\033[0m\n")
                water_input = input(f"\n\033[34mEnter: \n\033[0m")
                if water_input == "Big Size" or water_input == "1":
                    water_input = "Big Size of water"
                    water_price = 2000
                    water_portion = input(f"\n\033[34mHow many {water_input} do you need?\033[0m")
                    print(f"\033[94mYour order has been received and is being processed \033[0m\n")
                    total_water = water_price * int(water_portion)
                    print(f"\033[94mThank You, the cost of {water_portion} portion of {water_input} of water "
                          f"is N{str(total_water)}\033[0m\n")
                    drink_loop = "end"

                elif water_input == "Medium Size" or water_input == "2":
                    water_input = "Medium Size of water"
                    water_price = 1500
                    water_portion = input(f"\n\033[34mHow many {water_input} do you need?\033[0m")
                    print(f"\033[94m Your order has been received and is being processed \033[0m\n")
                    total_water = water_price * int(water_portion)
                    print(f"\033[94mThank You, the cost of {water_portion} portion of {water_input} of water "
                          f"is N{str(total_water)}\033[0m\n")
                    drink_loop = "end"
                elif water_input == "Small Size" or water_input == "3":
                    water_input = "Small Size of water"
                    water_price = 1000
                    water_portion = input(f"\n\033[34mHow many {water_input} do you need?\033[0m")
                    print(f"\033[94m Your order has been received and is being processed \033[0m\n")
                    total_water = water_price * int(water_portion)
                    print(f"\033[94mThank You, the cost of {water_portion} portion of {water_input} of water "
                          f"is N{str(total_water)}\033[0m\n")
                    drink_loop = "end"
                else:
                    price = 0

            elif drink_input == "Malt" or drink_input == "2":
                drink_varities = input(f"\033[93m We have the following:\n1. Malta Guiness\n2. Grand Malt\n3. Beta Malt\n"
                                       "4. Maltina\nMake your choice: \033[0m")
                if drink_varities == "Malta Guiness" or drink_varities == "1":
                    drink_varities = "Malta Guiness"

                elif drink_varities == "Grand Malt" or drink_varities == "2":
                    drink_varities = "Grand Malt"

                elif drink_varities == "Beta Malt" or drink_varities == "3":
                    drink_varities = "Beta Malt"

                elif drink_varities == "Maltina" or drink_varities == "4":
                    drink_varities = "Maltina"

                drink_input = drink_varities
                drink_price = 1000
                drink_portion = input(f"\n\033[34mHow many {drink_input} do you need?\n \033[0m")
                print(f"\033[94m Your order has been received and is being processed \033[0m\n")
                total_drink = drink_price * int(drink_portion)
                print(f"\033[94mThank You, the cost of {drink_portion} portion of {drink_input} "
                      f"is N{str(total_drink)}\033[0m\n")
                drink_loop = "end"

            elif drink_input == "Fanta" or drink_input == "3":
                drink_input = "Fanta"
                drink_price = 1000
                drink_portion = input(f"\n\033[34mHow many {drink_input} do you need?\n \033[0m")
                print(f"\033[94m Your order has been received and is being processed \033[0m\n")
                total_drink = drink_price * int(drink_portion)
                print(f"\033[94mThank You, the cost of {drink_portion} portion of {drink_input} "
                      f"is N{str(total_drink)}\033[0m\n")
                drink_loop = "end"
            elif drink_input == "Coke" or drink_input == "4":
                drink_input = "Coke"
                drink_price = 1000
                drink_portion = input(f"\033[34mHow many {drink_input} do you need?\n \033[0m")
                print(f"\033[94m Your order has been received and is being processed \033[0m\n")
                total_drink = drink_price * int(drink_portion)
                print(f"\033[94mThank You, the cost of {drink_portion} portion of {drink_input} "
                      f"is N{str(total_drink)}\033[0m\n")
                drink_loop = "end"
            elif drink_input == "Sprite" or drink_input == "5":
                drink_input = "Sprite"
                drink_price = 1000
                drink_portion = input(f"\n\033[34mHow many {drink_input} do you need?\n \033[0m")
                print(f"\033[94m Your order has been received and is being processed \033[0m\n")
                total_drink = drink_price * int(drink_portion)
                print(f"\033[94mThank You, the cost of {drink_portion} portion of {drink_input} "
                      f"is N{str(total_drink)}\033[0m\n")
                drink_loop = "end"

        grand_total = (total_drink + total_swallow + total_soup + total_rice + total_drink + total_water +
                       total_menu_order + total_protein + room_cost)
        kitchen_loop = "end"
    # list of other services we offer
    inquiry = input("\033[34mWould you like to see other of our services?\nYes or No\n \033[0m")
    if inquiry == "no" or inquiry == "No":
        print(f"\033[93m Thank you for your time, hope to see you soon\033[0m\n")

    else:
        services_list = input(
            "What other services do you need?\n 1. Catering \n 2. Outdoor Services\n 3. Barbeque\n 4. Bar\n"
            " 5. Smoothies\n 6. Karoke \n")
        registered_vendors = ["Bakey Eateries\ncontact: 08067479373", "Marine World\nContact: 09074827626",
                              "Kenny Drinks\nContact: 08048826632", "Jay Music\nContact:07029752923"]
        if services_list == "Catering" or services_list == "catering" or services_list == "1":
            print(f"\033[91m        WELCOME TO CHOP LIFE EATERY\033[0m\n")
            print("Your request would be handled by " + registered_vendors[0])
        elif (services_list == "outdoor services" or services_list == "Outdoor Services" or services_list == "2"
              or services_list == "Outdoor services"):
            print("Your request would be handled by  " + registered_vendors[3])
        elif services_list == "barbeque" or services_list == "Barbeque" or services_list == "3":
            print("Your request would be handled by " + registered_vendors[1])
        elif services_list == "Bar" or services_list == "bar" or services_list == "4":
            print("Your request would be handled by " + registered_vendors[3])
        elif services_list == "Smoothies" or services_list == "smoothies" or services_list == "5":
            print("Your request would be handled by " + registered_vendors[2])
        elif services_list == "karoke" or services_list == "karoke" or services_list == "6":
            print("Your request would be handled by " + registered_vendors[3])


#database
username_and_password = {"josh": "7203Josh_",
                         "adun": "3643Adun_",
                         "muspley1": "2345Muspley_",
                         "happy12": "1233Happiness_",
                         "willie11": "3611Williams_"}

username_and_full_name = {"josh": "Joshua Kelechi",
                          "adun": "Adunola Titi",
                          "muspley1": "Muspley Samson",
                          "happy12": "Happiness Braimoh",
                          "willie11": "Williams Ameh"}

username_and_password_data = """Username,Password,Full name,Phone number
josh,7203Josh_,Joshua Kelechi,08067513975
adun,3643Adun_,Adunola Titi,07011196885
muspley1,2345Muspley_,Muspley Samson,07067921429
happy12,1233Happiness_,Happiness Braimoh,08080671679
willie11,3611Williams_,Williams Ameh,08167679209
"""

Admin_portal = {"Joshua": "Joshua1/5"}

with open('hotel details1.csv', 'w') as file:
    file.write(username_and_password_data)

#sign up function
def sign_up():
    global username2
    global full_name
    global phone_num
    global pass2
    full_name_loop = "start"
    while full_name_loop == "start":
        full_name = input("\033[34mEnter full name: \033[0m")
        full_name = full_name.capitalize()
        if len(full_name) < 8:
            print("\033[31mPlease enter full name \033[0m")

        else:
            pass
            full_name_loop = "end"
    phone_num_loop = "start"
    while phone_num_loop == "start":
        phone_num = input("\033[34mPhone Number: \033[0m")
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

    username2_loop = "start"
    while username2_loop == "start":
        username2 = input("\033[34mChoose username: \033[0m")
        username2 = username2.lower()
        if username2 in username_and_password:
            print("\033[91m Sorry that username has been chosen already\n"
                  "Please Choose another username\033[0m\n")
        else:
            pass
            username2_loop = "end"

    password_loop = "start"
    while password_loop == "start":
        pass2 = input("\033[34mChoose password: \033[0m")
        if len(pass2) >= 8:
            if not pass2.isnumeric():
                if not pass2.isupper():
                    if not pass2 == pass2.lower():
                        if (not pass2.find("0") == -1 or not pass2.find("1") == -1 or not pass2.find("2") == -1
                                or not pass2.find("3") == -1 or not pass2.find("4") == -1 or not pass2.find("5") == -1
                                or not pass2.find("6") == -1 or not pass2.find("7") == -1 or not pass2.find("8") == -1
                                or not pass2.find("9") == -1):
                            # verified_password.append(pass2)
                            username_and_password.update({username2: pass2})
                            username_and_full_name.update({username2: full_name})
                            print("\033[94m You have successfully registered\n"
                                  "and your details has been recorded\033[0m\n")
                            new_user = f"""{username2},{pass2},{full_name},{phone_num}
                            """

                            with open('hotel details1.csv', 'a') as file:
                                file.write(new_user)
                            password_loop = "end"
                        else:
                            print("\033[91m Your Password must contain at least one number\nPlease try again\033[0m\n")

                    else:
                        print(
                            "\033[91m Your Password must contain at least one upper case letter\nPlease try again\033["
                            "0m\n")

                else:
                    print("\033[91m Password cannot be all uppercase.\033[0m\n")

            else:
                print("\033[91m Password cannot be all numbers\033[0m\n")

        else:
            print("\033[91m Your Password must not be less than 8 Characters\nPlease try again\033[0m\n")

#login function
def user_login():
    # this make it possible for you to be able to use the username a user entered outside the function
    global username
    # start the loop as soon as the function is invoked
    login_loop = "start"
    while login_loop == "start":
        username = input("\033[34mEnter Username:  \033[0m")
        username = username.lower()
        if username in username_and_password:
            pass
            login_loop = "end"
            password_loop = "start"
            while password_loop == "start":
                password = input("\033[34mEnter Password: \033[0m")
                if password == username_and_password.get(username):
                    print("\033[94mPassword is correct\n\033[0m")
                    # end the loop if password is correct.
                    password_loop = "end"
                else:
                    print("\033[91m wrong password\033[0m\n")

        else:
            print("\033[91mIncorrect Username\033[0m\n")

#admin Portal
def admin_login():
    print("                   \033[7mWELCOME TO ADMIN PORTAL\033[0m")
    print("                        \033[4mSIGN IN\033[0m\n")
    admin_loop = "start"
    while admin_loop == "start":
        admin_log = input("\033[34mEnter username: \033[0m")
        admin_log = admin_log.capitalize()
        if admin_log in Admin_portal:
            password = input("\033[34mEnter Password:  \033[0m")
            if password == Admin_portal.get(admin_log):
                print("\033[94mPassword is correct\n\033[0m")
                # end the loop if password is correct.
                admin_loop = "end"
            else:
                print("\033[91m wrong password\033[0m\n")

        else:
            print("\033[91m Incorrect Username\033[0m\n")


main_loop = "start"
while main_loop == "start":
    print("\033[91m             WELCOME TO OLIVE WORLD HOTEL\033[0m\n")
    login_or_signup = input("\033[34m -login\n -Sign up\n -Admin\n \n \033[0m")
    login_or_signup = login_or_signup.lower()
    if login_or_signup == "login":
        print("                   \033[7mWELCOME TO LOGIN PORTAL\033[0m")
        print("                           \033[4mLOGIN \033[0m\n")
        user_login()
        print(f"\033[94mWelcome {username_and_full_name.get(username)}\033[0m\n")
        booking()
        print(f"\033[94m Would you like to order from our kitchen?\033[0m\n")
        order_response = input("\n\033[34mYes or No: \n \033[0m")
        order_response = order_response.capitalize()
        if order_response == "Yes":
            kitchen()
        elif order_response == "No":
            print()
        print(f"                \033[93mOlive Hotel\033[0m")
        print("             \033[93mReceipt of Payment\033[0m\n")
        details = [
            'Name', username_and_full_name.get(username),
            'Room', room_order,
            'Room Duration', room_num,
            'Room Cost W discount', room_cost,
            'Room Cost WO discount', room_price,
            'Companion', response,
            'Com_Spec', response_input,
            'Soup Order', soup_order,
            'Soup portion', soup_number,
            'Swallow Choice', swallow_input,
            'Swallow portion', swallow_number,
            'Menu Order', menu_order,
            'Menu Portion', menu_portion,
            'Rice order', rice_order,
            'Rice Portion', rice_Portion,
            'Protein Order', protein_order,
            'Protein portion', protein_portion,
            'Drink order', drink_order,
            'Drink input', drink_input,
            'Drink Portion', drink_portion,
            'Water Order', water_order,
            'Water Input', water_input,
            'Total', grand_total]
        teller = f"""Receipt,Order
Name,{username_and_full_name.get(username)}
Room,{room_order}
Room Duration,{room_num}
Room Cost W discount,{room_cost}
Room Cost WO discount,{room_price}
Companion,{response}
Com_Spec,{response_input}
Soup Order,{soup_order}
Soup portion,{soup_number}
Swallow Choice,{swallow_input}
Swallow portion,{swallow_number}
Menu Order,{menu_order}
Rice order,{rice_order}
Rice Portion,{rice_Portion}
Protein Order,{protein_order}
Protein portion,{protein_portion}
Drink order,{drink_order}
Drink input,{drink_input}
Drink Portion,{drink_portion}
Water Order,{water_order}
Water Input,{water_input}
Total,{grand_total}"""

        with open('Receipt1.csv', 'a') as file:
            file.write(teller)

        receipt = listdict(details)
        for key, value in receipt.items():
            column = ":"
            end = "\n"
            if value == "":
                key = ""
                column = ""
                end = ""
            print(f"\033[93m{key}{column} {value}\033[0m", end=end)

    if login_or_signup == "sign up":
        print("                   \033[7mWELCOME TO SIGN UP PORTAL\033[0m")
        print("                             \033[4mSIGN UP\033[0m\n")
        print("                    \033[4mThank You for choosing us,\033[0m")
        print("              \033[4mWe look forward to serving you better\n\033[0m")
        sign_up()
        print(f"\033[94mWelcome {username_and_full_name.get(username2)}\033[0m\n")
        booking()
        print(f"\033[94m Would you like to order from our kitchen?\033[0m\n")
        order_response = input("\n\033[34mYes or No: \n \033[0m")
        order_response = order_response.capitalize()
        if order_response == "Yes":
            kitchen()
        elif order_response == "No":
            print()
        print(f"                \033[93mOlive Hotel\033[0m")
        print("             \033[93mReceipt of Payment\033[0m\n")
        details = [
            'Name', username_and_full_name.get(username2),
            'Room', room_order,
            'Room Duration', room_num,
            'Room Cost W discount', room_cost,
            'Room Cost WO discount', room_price,
            'Companion', response,
            'Com_Spec', response_input,
            'Soup Order', soup_order,
            'Soup portion', soup_number,
            'Swallow Choice', swallow_input,
            'Swallow portion', swallow_number,
            'Menu Order', menu_order,
            'Menu Portion', menu_portion,
            'Rice order', rice_order,
            'Rice Portion', rice_Portion,
            'Protein Order', protein_order,
            'Protein portion', protein_portion,
            'Drink order', drink_order,
            'Drink input', drink_input,
            'Drink Portion', drink_portion,
            'Water Order', water_order,
            'Water Input', water_input,
            'Total', grand_total]
        teller = f"""Receipt,Order
        Name,{username_and_full_name.get(username2)}
        Room,{room_order}
        Room Duration,{room_num}
        Room Cost W discount,{room_cost}
        Room Cost WO discount,{room_price}
        Companion,{response}
        Com_Spec,{response_input}
        Soup Order,{soup_order}
        Soup portion,{soup_number}
        Swallow Choice,{swallow_input}
        Swallow portion,{swallow_number}
        Menu Order,{menu_order}
        Rice order,{rice_order}
        Rice Portion,{rice_Portion}
        Protein Order,{protein_order}
        Protein portion,{protein_portion}
        Drink order,{drink_order}
        Drink input,{drink_input}
        Drink Portion,{drink_portion}
        Water Order,{water_order}
        Water Input,{water_input}
        Total,{grand_total}"""

        with open('Receipt1.csv', 'a') as file:
            file.write(teller)

        receipt = listdict(details)
        for key, value in receipt.items():
            column = ":"
            end = "\n"
            if value == "":
                key = ""
                column = ""
                end = ""
            print(f"\033[93m{key}{column} {value}\033[0m", end=end)

    if login_or_signup == "admin":
        admin_login()
        print(f"                \033[93mOlive Hotel\033[0m")
        print("             \033[93mReceipt of Payment\033[0m\n")
        with (open('Receipt1.csv', 'r') as file):
            database = file.read()
        data = database.split(",")
        add = ":".join(data)
        receipt_list = add.split("\n")
        join_again1 = ",".join(receipt_list)
        split_again = join_again1.split(":")
        join_again2 = ",".join(split_again)
        final_list = join_again2.split(",")
        # for list {
        num = 0
        order_no = 1
        plus = 0
        for i in final_list:
            plus += 1
            # this resets the list so every receipt can be numbered differently
            if i == "Order":
                i_index = final_list.index(i)
                order = "Receipt Order #" + str(order_no) + " for " + final_list[i_index + plus]
                print(f"\n\033[91m   {order:} \033[0m\n")
                order_no += 1
                num = 0
                order = ""

            # this else skip the element on the list at the index of 0
            if plus == 1:
                pass
            # this help so that we loop through only elements that are the prices or order quantity.
            elif plus % 2 == 0:
                if i == "0" or i == "" or i == " ":
                    pass
                # this skips when i == 'Order'
                elif i == "Order":
                    pass

                else:
                    num += 1
                    get_index = final_list.index(i)

                    print(f"\033[93m {num:02}. \033[1m{final_list[get_index - 1]:<22}: {i}\033[0m")

    else:
        print()
