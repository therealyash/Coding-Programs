import random

jackpot = random.randint(1,100)
guess = int(input('Guess a Number: '))
count = 1


while guess != jackpot:
    if guess < jackpot:
        print('Guess Higher!')
    else:
        print('Guess Lower')

    guess = int(input('Guess a Number: '))
    count += 1

print('Right Answer! Well Done',count)


