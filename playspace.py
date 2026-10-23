class Convert:


    def change(self, name):

        small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                      'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        big = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        empty = []
        for i in name:
            if i in small:
                box = small.index(i)
                empty.append(big[box])
            else:
                empty.append(i)
        mean = "".join(empty)

        print(mean)


username = input("Enter name: ")
print(f"welcome {username}")
message = input("Enter message ")
new = Convert()
message.change(message)

