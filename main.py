from time import sleep
from random import randint
from test import enc_main, return_password

inventory = {'points': 0,
             'flashlight': 0,
             'key': 0,
             'is_opened': 0}

chance_to_open = randint(1, 100)
chance_to_find = randint(1, 2)
chance_to_die = randint(1, 2)


def you_win():
    print("Congratulations you won")
    sleep(1)
    print('+1000 points')
    inventory['points'] += 1000
    print('Maximal points is 1220')
    sleep(1)
    print(f'Your points is {inventory["points"]}')
    exit()


def password_problem():
    print("Enter a password or type 'exit'")
    sleep(1)
    password = user_input()
    if password == return_password():
        print("Success, you opened a door.")
        sleep(1)
        print("You received 100 points")
        sleep(1)
        inventory['points'] += 100
        inventory['is_opened'] = 1
        inside_door()
    else:
        print("Wrong password")


def dark_tunnel():
    sleep(1)
    if inventory['flashlight'] == 0:
        print('You can\'t see anything. Do you want to go forward?')
        sleep(1)
        print("yes or no")
        command = user_input()
        if command == 'yes':
            sleep(2)
            print("You got lost in the tunnel")
            game_over()
        else:
            print('You go back to the first location')

    elif inventory['flashlight'] == 1:
        sleep(1)
        print('You are moving forward and you see, a monster in 2 metres.')
        sleep(1)
        print('But you are luckily he is asleep')
        sleep(1)
        print('You sneak over him')
        sleep(1)
        print('You accidentally drop rock on his head')
        chance_to_live = randint(1, 2)
        if chance_to_live == chance_to_die:
            print("Monster didnt wake up you save to go forward")
            you_win()
        else:
            game_over()


def strange_door():
    print('It\'s just a door without a keyhole, you don\'t know how to open it')
    sleep(1)

    if inventory['is_opened'] == 1:
        inside_door()
    else:
        print('1: You can try to open it')
        print('2: Look around  ')
        print('3: Open it with password')
        command = user_input()

        if command == "1":
            random = randint(1, 100)
            if chance_to_open == random:
                sleep(1)
                print("Success, you opened the door")
                inventory['is_opened'] = 1
                inside_door()
            else:
                print("Unlucky, the door is still closed")

        elif command == "2":
            random_chance_to_find_button = randint(1, 100)
            if random_chance_to_find_button == chance_to_open:
                sleep(1)
                print("You found a secret button")
                sleep(1)
                print("Do you want to push it? Yes or No")
                command = user_input()

            elif random_chance_to_find_button != chance_to_open:
                print("You didnt find anything helpful, and you decided to get back in cave")

                if command == 'yes':
                    print('Success, you opened the door')
                    sleep(1)
                    print('Points + 20')
                    inventory['points'] += 20
                    inventory['is_opened'] = 1
                    inside_door()
                else:
                    print('You decided not to touch this button and go back to the first location')
            else:
                print("You didnt find anything helpful, and you decided to get back in cave")

        elif command == "3":
            password_problem()


def inside_door():
    sleep(1)
    print(f'You enter small room with chest in it')
    sleep(1)
    print(f'You see a keyhole')

    if inventory['key'] == 1:
        sleep(1)
        print('You have a key lets try it')
        sleep(1)
        print('You found a flashlight in it')
        inventory['flashlight'] += 1
        sleep(1)
        print('Now you have everything to go in the tunnel')
        dark_tunnel()

    else:
        sleep(1)
        print(f'Chest says: Tiberius Claudius Caesar says = «lxxt>33m2mqkyv2gsq3q=j02ntk»')
        sleep(1)
        print(f'Hint: just type what comes after the name of the organizations that used it in their game')
        command = user_input()

        if command == "3301":
            print('Chest opened and you find a flashlight in it')
            sleep(1)
            print('You got + 100 points')
            sleep(1)
            inventory['points'] += 100
            inventory['flashlight'] += 1
            print('Now you have everything to go in the tunnel')
            dark_tunnel()


def game_over():
    print('Game Over!')
    sleep(1)
    print(f'You got {inventory["points"]} maximal is 1220')
    sleep(1)
    print("Do you want to try again?")
    choose = user_input()

    if choose == "yes":
        game()
    else:
        print("Thanks for playing!")
        exit()


def welcome():
    print('Welcome to the Text Adventure Game!')
    sleep(1)
    print("You find yourself in a dark cave...")
    sleep(1)


def game():
    welcome()
    flag = True
    while flag:
        print('You have different options or')
        print('1: You can try to look around ')
        print('2: Search the cave for some loot')
        sleep(1)
        command = user_input()

        if command == "1":
            inventory['first_location'] = 1
            print('You see three paths')
            sleep(1)
            print('1: A very long dark tunnel')
            sleep(1)
            print('2: A strange door without a keyhole')
            sleep(1)
            print('3: An opened door with light in it')
            sleep(1)
            command = user_input()

            if command == '1':
                dark_tunnel()
            elif command == '2':
                strange_door()
            elif command == "3":
                library()

        elif command == "2":
            if inventory['key'] == 0:
                random_digit = randint(1, 2)
                if random_digit == chance_to_find:
                    sleep(1)
                    print('You found a strange key. Now you need to find a hole for that key.')
                    sleep(1)
                    print('+10 points')
                    inventory['key'] += 1
                    inventory['points'] += 10
                else:
                    sleep(1)
                    print('You didnt find anything')

            elif inventory['key'] == 1:
                sleep(1)
                print('You didnt find anything maybe its time to go forward? ')


def library():
    print('You entered a very big and well-lit room')
    sleep(1)
    print("It's a library")
    sleep(1)
    print("There's one book that's glowing")
    sleep(1)
    print("Inside this book, there is some strange text")
    enc_main()


def user_input():
    return input().lower()


def main():
    game()


if __name__ == '__main__':
    main()
