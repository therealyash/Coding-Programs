# Program to randomly generate Heads & Tails

import random
n = random.randint(0,1)
coin_stat = 'Heads' if n==0 else 'Tails'
print(coin_stat)
