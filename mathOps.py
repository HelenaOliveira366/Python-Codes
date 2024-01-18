#Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição, subtração, multiplicação e divisão

#ENTRADA DE DADOS
print("Este programa recebe 2 números e mostra o resultado da adição, subtração, multiplicação e divisão")
number1 = int(input("Digite um número: "))
number2 = int(input("Digite outro número: "))

#OPERAÇÕES MATEMÁTICAS
sum = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2

#IMPRESSÃO NA TELA
print(f'{number1} + {number2} = {sum}')
print(f'{number1} - {number2} = {subtraction}')
print(f'{number1} * {number2} = {multiplication}')
print(f'{number1} / {number2} = {division}')