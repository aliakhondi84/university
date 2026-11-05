import stdio
import random
range = 1000000
secret = random.randrange(1, range + 1)
print('guess a number between 1 and %d' % range)
guess = 0
while guess != secret:
    print('what is your guess?', end=' ')
    guess = stdio.readint()

    if guess < secret:
        print('Too low')

    elif guess > secret:
        print('Too high')

    else:
        print('You win!')