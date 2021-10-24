import random
secret_num = random.randint(1,10)
def game():
    while True:
        guess = int(input('Enter a guess:'))
        if guess == secret_num:
            print('correct')
        elif guess > secret_num:
            print('too high.')
        else:
            print('too low.')
        break
game()
print('secret number was', secret_num)

def new_game():
    while True:
        one = int(input('For new game press one for exit press two'))
        if one == 1:
            game()
        elif one == 2:
            print('Goodbye')
        else:
            print('Enter correct value')
            break



new_game()
