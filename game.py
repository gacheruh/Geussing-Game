from random import randrange

count = 0
limit = 3
secret_number = randrange(0, 11)

while count < limit:
    count += 1

    guess = int(input('Guess:'))
    if guess == secret_number:
        print(f'YOU WON!!!!')
        break

    elif count < 3:
        print('Try again')

    if count == limit:
        if guess != secret_number:
            print(f'The secret number was {secret_number}\nBETTER LUCK NEXT TIME')
