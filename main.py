import random 

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2, #valor das letras, multliplicador da aposta
}

def checkWinnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines): #checar para ver se há simbolos iguais em uma mesma linha
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break #se dar o break o else não é executado
        else: #se nao quebramos do for loop
            winnings += values[symbol] * bet #pega o valor do dicionario
            winning_lines.append(line + 1) #fala quais linhas foram ganhas
    
    return winnings, winning_lines

def getSlotMachineSpin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): #retorna a chave e o seu valor, symbol = chave, symbol_count = valor
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    current_symbols = all_symbols[:]
    for _ in range(cols):
        current_column = [] #cria uma nova lista para a coluna, cada vez que termina o segundo
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            current_column.append(value)
        
        columns.append(current_column)
    
    return columns

def printSlotMachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="") 
        print()

def deposit():
    while True:
        amount = input("What would you like to deposit! $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("Please write a number!")
    return amount

def getNumbersOfLines():
    while True:
        lines = input("Enter the number of lines to bet (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number!")
    return lines

def getBet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please write a number!")
    return amount

def spin(balance):
    while True:
        lines = getNumbersOfLines()
        bet = getBet()
        totalBet = bet * lines
        if totalBet > balance:
            print(f"You do not have enough money to bet ${totalBet}, your current balance is ${balance}")
        else:
            break
    
    print(f"You are betting {bet} on {lines} lines, the total bet is equal to ${totalBet}")
    
    slots = getSlotMachineSpin(ROWS, COLS, symbol_count)
    printSlotMachine(slots)
    winnings, winning_lines = checkWinnings (slots, lines, bet, symbol_values)
    print(f"You won ${winnings}")
    print("You won on lines: ", *winning_lines) 
    return winnings - totalBet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        answer = input("Press enter to play (q to quit)")
        if answer == "q" or answer == "Q":
            break
        balance += spin(balance)
        
    print (f"You left with ${balance}")
    
    #A função do operador splat no contexto do print() é permitir a impressão de elementos de uma sequência 
    # (como uma lista) de forma mais legível, separando-os por espaços. 
    # Isso é especialmente útil ao imprimir os elementos de uma lista, evitando a necessidade de usar loops ou 
    # outras estruturas de repetição.
    
main()
