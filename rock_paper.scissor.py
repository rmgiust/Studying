import random

emojis = { 'r': '🪨', 'p': '📄', 's': '✂️'} # Cria um dictionary pra substituir os valores pelos emojis
choices = ('r', 'p', 's') # usar () e nao [], pois TUPLES nao podem ser modificadas e isso e um constante

counter_games = 0
user_wins = 0
computer_wins = 0
counter_tie = 0

while True:
    user_choice = input('Rock, paper or scissor? (r/p/s): ').lower()
    
    if user_choice not in choices:
        print("Invalid choice!")
        continue # Volta para while loop, nao crashando o programa
    counter_games += 1
    computer_choice = random.choice(choices)

    print(f'You choose: {emojis[user_choice]}') # Chama o emoji com user_choice como valor 
    print(f'Computer choose: {emojis[computer_choice]}')
  
    if user_choice == computer_choice:
        print('Tie!')
        counter_tie += 1
    elif ( # usar parenteses aqui e outro no final, apos quebrar linhas, mantem o codigo mais clean e legivel, evitando ficar longo demais
        (user_choice == 'r' and computer_choice == 'p') or 
        (user_choice == 's' and computer_choice == 'p') or 
        (user_choice == 'r' and computer_choice == 's')):
        print("You win ⭐")
        user_wins += 1
    else:
        print("You lose ❌")
        computer_wins += 1

    while True:
        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'y':
            break
        elif should_continue == 'n':
            print(f"\n-> You played {counter_games} times")
            print(f"-> User wins: {user_wins} ⭐\n-> Computer wins: {computer_wins} ❌\n-> Tie's: {counter_tie} 🟠")
            exit()
        else:
            print("Invalid input. Please, enter 'y' or 'n")


