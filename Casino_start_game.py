from Casino import game_start
from decouple import config
my_money = config('MY_MONEY', cast=int)
print('Enter your user name')
name = input()
print(f'Welcome to Casino World {name}\nYour bank account: {my_money}$')

while True:
    print('\nDo u wanna play one round? If yes - write number 1, if no - write number 0')
    answer = int(input())
    if answer == 0:
        break
    elif answer == 1:
        print('1) Choose slot number between 1 - 30', '\n2) Write the amount you wnat to bet')
        slot_number = int(input())
        bet_amount = int(input())
        my_money -= bet_amount
        my_money += game_start(slot_number, bet_amount)
    else:
        print("There's only 2 options: 1 - continue, 2 - exit")
    if my_money >= 1000:
        print(f'You still win. Your current accound: {my_money}$')
    else:
        print(f"You're losing. Your current accound: {my_money}$")
