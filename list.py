#Lista: Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os armazene dentro de uma lista. Após a leitura, crie outra estrutura de repetição para somar todos os valores digitado

#DECLARAÇÃO DA LISTA E VARIÁVEL ACUMULADORA 
numberList = []
sum = 0

#LOOP QUE PREENCHE A LISTA
print("Digite 5 numeros inteiros")
for i in range(5):
   #ENTRADA DE DADOS
   number = int(input("Digite o número: "))
   #ADICIONAR ELEMENTO NA LISTA
   numberList.append(number)

#LOOP QUE CALCULA A SOMA DOS NÚMEROS INSERIDOS
for j in range(5):
   sum =+ numberList[j]

#SAÍDA DA SOMA
print("A soma dos 5 números é: ", sum)