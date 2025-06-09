import random # Importa a biblioteca 'random' para gerar números aleatórios.

count_total_dices_rolled = 0 # Contador para o total de dados rolados em todas as rodadas.

while True:
    choice = input('Roll the dice? (y/n): ').lower() # Pergunta se o usuário quer rolar os dados.

    if choice == 'y':
        try:
            # Solicita ao usuário quantos dados ele quer rolar e tenta converter para inteiro.
            # Se a entrada não for um número válido, um ValueError será gerado.
            num_dices = int(input('How many dice do you want to roll? '))

            # Validação para garantir que o número de dados seja positivo
            if num_dices <= 0:
                print('Please enter a positive number of dice.')
                continue # Volta para o início do loop 'while'
            
            print(f'Rolling {num_dices} dice:')
            results = [] # Cria uma lista vazia para armazenar os resultados de cada dado

            # Loop 'for' para rolar a quantidade de dados que o usuário escolheu
            for i in range(num_dices): # 'range(num_dices)' gera uma sequência de números de 0 até (num_dices - 1)
                die_roll = random.randint(1, 6) # Rola um dado (número entre 1 e 6)
                results.append(die_roll) # Adiciona o resultado do dado à lista 'results'
                
            # Exibe todos os resultados dos dados rolados
            # A função map(str, results) converte cada número da lista 'results' para uma string.
            # O '.join(', ')' junta todas essas strings com ', ' entre elas.
            print(f'Results: {", ".join(map(str, results))}')

            # Opcional: Calcular e exibir a soma dos resultados
            total_sum = sum(results) # 'sum()' é uma função embutida que soma todos os elementos de uma lista
            print(f'Total sum: {total_sum}')

            # Atualiza o contador de dados rolados com a quantidade de dados desta rodada
            count_total_dices_rolled += num_dices

        except ValueError:
            # Captura o erro se o usuário não digitar um número
            print('Invalid input. Please enter a whole number for the number of dice.')
    
    elif choice == 'n':
        print('Thanks for playing!')
        # Exibe o total de dados rolados ao longo de todo o jogo
        print(f'You rolled a total of {count_total_dices_rolled} dice across all rounds.')
        break # Sai do loop 'while True', encerrando o programa
    
    else:
        print('Invalid input. Please enter "y" or "n".') # Mensagem para entradas inválidas no início