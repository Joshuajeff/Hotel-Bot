class Example:

    def encrypt(self, string):

        original = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v',
                    'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                    'Q', 'R',
                    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', " "]

        crypt = ['T', '7', 'l', '5', 'p', 'A', 'm', 'Y', 'P', 'I', 'o', '1', 'i', 'F', 'B', '9', 'J', 'H', 'k', 'x',
                 'y',
                 'E', 'U', 'K', 't', '6', 'q', 'N', 'c', '2', 'C', 'b', 'u', 'g', '0', 'W', 'd', 'G', 'f', 'Q', '4',
                 'D',
                 'O', 'j', 'a', 'S', 'v', 'r', ' ', 'V', 'R', 'w', 'X', 'M', 'h', '3', 'e', '8', 'L', 'Z', 's', 'z',
                 'n']

        empty = []

        for i in string:
            if i in original:
                plan = original.index(i)
                empty.append(crypt[plan])

            else:
                empty.append(i)

        back_to_string = "".join(empty)
        return back_to_string


encrypt_response = input("Message: ")
convert_encrypt = Example()
result_encrypt = convert_encrypt.encrypt(encrypt_response)
print(result_encrypt)


class Example2:

    def decrypt(self, string):

        original = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v',
                    'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                    'Q', 'R',
                    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', " "]

        crypt = ['T', '7', 'l', '5', 'p', 'A', 'm', 'Y', 'P', 'I', 'o', '1', 'i', 'F', 'B', '9', 'J', 'H', 'k', 'x',
                 'y',
                 'E', 'U', 'K', 't', '6', 'q', 'N', 'c', '2', 'C', 'b', 'u', 'g', '0', 'W', 'd', 'G', 'f', 'Q', '4',
                 'D',
                 'O', 'j', 'a', 'S', 'v', 'r', ' ', 'V', 'R', 'w', 'X', 'M', 'h', '3', 'e', '8', 'L', 'Z', 's', 'z',
                 'n']

        empty = []

        for x in string:
            if x in crypt:
                plan = crypt.index(x)
                empty.append(original[plan])

            else:
                empty.append(x)

        back_to_string = "".join(empty)
        return back_to_string


convert_decrypt = Example2()
result_decrypt = convert_decrypt.decrypt(result_encrypt)
print(result_decrypt)