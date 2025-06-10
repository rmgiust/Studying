import random # Importa a biblioteca para gerar números aleatórios

number_to_guess = random.randint(1, 10)
guesses = 0 # Conta o número de vezes em que o usuário tentou acertar
while True:
    try:
        guess = int(input('Guess the number between 1 and 10: '))
        if guess > number_to_guess:
            print('Lower!')
            guesses += 1
        elif guess < number_to_guess:
            print('Higher!')
            guesses += 1
        else:
            print(f'Congratulations, the Number is: {number_to_guess}')
            print(f'You guessed {guesses} times, until hit the number!')
            break
    except ValueError:
        print("Enter a valid number")