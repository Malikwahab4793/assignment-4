import random

def guess(x):
    random_number=random.randint(1,x)
    guess= 0
    while guess != random_number:
        guess= int (input(f'Guess the number between 1 and {x}:'))
        print(guess)
        if guess < random_number:
            print('Sorry, Guess again. Too low')
        elif guess > random_number:
            print('Sorry guess agian. to high ')

    print(f'yay, congrate. you have guess the number {random_number} correctly!')


def computer_guess(x):
    low= 1
    high= x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could also be high 
        feedback= input((f'is {guess} too high (H), too low (L), or correct (C)')).lower()
        if feedback == 'h':
         high = guess -1
        elif feedback ==  'l':
            low = guess +1

    print(f'yay! Compuetr guessed your number, {guess}, correct!')


computer_guess(1000)
