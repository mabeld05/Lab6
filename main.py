#Name: Mabel Dowell
#lab 6: Version Control
#Date: 10/25/2023

def show_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()

def encode(password):
    encoded_pass = ''
    for i in password:
        encoded_char = str(int(i) + 3)
        encoded_pass += encoded_char
    return encoded_pass

def decode(password):
    new_password = ''
    for i in password:
        num = int(i) - 3
        if num < 0:
            char = str(9 + (num + 1))
        else:
            char = str(num)
        new_password = new_password + char
    return new_password

def main():
    display_menu = True
    user_continue = True

    while user_continue:
        if display_menu:
            show_menu()

        user_input = int(input('Please enter an option: '))
        if user_input == 1:
            password_to_encode = input('Please enter your password to encode: ')
            encoded_password = encode(password_to_encode)
            print('Your password has been encoded and stored!')
            print()
        elif user_input == 2:
            decoded_password = decode(encoded_password)
            print(decoded_password)
        elif user_input == 3:
            display_menu = False
            user_continue = False
            break



if __name__ == '__main__':
    main()