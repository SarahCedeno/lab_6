# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def encoder(num):
    password = ""
    val = 0
    for i in range(0, len(num)):
        val = int(num[i])+3
        if val >= 10:
            val -= 10
        password += str(val)
    return password


def decoder(num):
    decoded = ""
    for i in range(len(num)):
        temp = int(num[i]) - 3
        if temp < 0:
            temp += 10
        decoded += str(temp)
    return decoded


def main():
    password = ""
    run = True
    while run:
        print("Menu \n ------------ \n 1.encoder \n 2. decoder \n 3. Quit")
        valid = True

        while valid:
            select = int(input("Please enter an option:"))

            if select == 1:
                num = input("Please enter a password to encode:")
                password = encoder(num)
                print(password)
                valid = False
            elif select == 2:
                if password != '':
                    print(f'The encoded password is {password}, and the original password is {decoder(password)}')
                else:
                    print('No password stored.')
                valid = False
            elif select == 3:
                valid = False
                run = False
            else:
                print('Please enter a valid selection.')


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
