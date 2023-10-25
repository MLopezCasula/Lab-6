# Marcoaurelio Lopez-Casula

import sys

def encode(password):
    password_list = list(password)
    number_list = [int(digit) for digit in password_list]

    for i in range(0,len(number_list)):
        number_list[i] += 3

    return number_list

def decode(encoded):
    decoded = ""
    for char in encoded:
        decoded += str(int(char) - 3)
    return decoded


if __name__ == "__main__":
    password = input("Please enter your password to encode:")
    user_choice = 0
    plain = 0
    encoded = 0
    while user_choice != 3:
        # print menu
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        # get user input
        user_choice = int(input("Please enter an option: "))

        if user_choice == 1:  # get string and encode it
            plain = input("Please enter your password to encode: ")
            encoded = encode(plain)
            print("Your password has been encoded and stored!")
        elif user_choice == 2:  # print decoded string
            print(f"The encoded password is {encoded}, and the original password is {decode(encoded)}.")
        elif user_choice == 3:  # quit
            sys.exit()
