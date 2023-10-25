# Marcoaurelio Lopez-Casula

def encode(password):
    password_list = list(password)
    number_list = [int(digit) for digit in password_list]

    for i in range(0,len(number_list)):
        number_list[i] += 3

    return number_list


if __name__ == "__main__":
    password = input("Please enter your password to encode:")
    encode(password)
