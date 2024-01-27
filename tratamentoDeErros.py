#Crie uma lista vazia e faça a leitura de dois valores do tipo float, colocando cada um dos valores nas primeiras posições da lista (o valor1 ficará na posição 0 da lista e o valor2 ficará na posição 1 da lista). Faça a divisão dos dois valores e trate as seguintes exceções:
#- ValueError: se o usuário digitar um caracter
#- ZeroDivisionError: se o usuário digitar zero e ocorrer erro na divisão
#- IndexError: caso a divisão seja feita levando em consideração posições que não existem na lista
#- KeyboardInterrupt: caso o usuário interrompa a execução

#Mostre uma mensagem personalizada na ocorrência de cada um desses erros

#CRIAÇÃO DA LISTA
numberList = []

while True:
   try:
      #POPULAR A LISTA COM DADOS INSERIDOS PELO USUÁRIO
      numberList.append(float(input("Digite um número decimal: ")))
      numberList.append(float(input("Digite um número decimal: ")))
      print(numberList[0], "dividido por ", numberList[1], " = ", numberList[0]/numberList[1])
      break
   except ValueError:
      print("Caracter não é permitido, apenas números!")
   except ZeroDivisionError:
      print("Impossível dividir por 0")
      break
   except IndexError:
      print("Posição inesxistente")
   except KeyboardInterrupt:
      print("Execução interrompida")
      break