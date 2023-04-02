import random

TRIES = 10
WORD_LENGTH = 3
GAME_OVER = False

def generate_secret_number():
    numbers = [str(i) for i in range(10)]
    random.shuffle(numbers)
    return numbers[:3] 

def the_number():
    s = ''
    while len(s) != 3:
        s = input()
        print("Please Enter a 3 Digit Number") if len(s) != 3 else print(f"You Guessed {s}")
    return s


def welcome_message(number):
    if number == 1:
        print(
           '''I am thinking of a 3-digit number. Try to guess what it is.
           Here are some clues:
           When I say:    That means:
           Pico         One digit is correct but in the wrong position.
           Fermi        One digit is correct and in the right position.
           Bagels       No digit is correct.
           I have thought up a number.
           You have 10 guesses to get it.''')
            
win = False
i = 1

def process(guess , secret_number):
    if guess == ''.join(secret_number):
        return 'Correct!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            clues.append('Fermi')
        elif guess[i] in secret_number:
            clues.append('Pico')
    if len(clues) == 0 : return 'Bagels'
    else: 
        return ' '.join(clues)
    

secret_number = generate_secret_number()
print(secret_number)
while not win and i < TRIES:
    if i == TRIES:
        print(f"This was your last try .... the number was {secret_number}")
    welcome_message(i)
    
    print("Guess The Number") if i == 1 else print("Guess Again")

    print(f"Guess #{i}")
    
    s = the_number()

    
    i+= 1
    result = process(s ,secret_number)
    
    if result == 'Correct!' :
        print('Correct!')
        break
    else: print(result)
if i == 10:
    print(f"Game Over the correct number is {secret_number}")
    
    




