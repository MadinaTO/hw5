from random import randint

def game_start(slot_number, bet_amount):
    while True:
        slot = randint(1, 31)
        if slot == slot_number:
            print(f'You win! Winning slot: {slot}\n')
            return bet_amount * 2
        elif slot != slot_number:
            print(f'You lose:( Winning slot: {slot}\n')
            return 0









