#Matriz: Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz
#matriz = np.array([[3, 4, 1],[3, 1, 5]])

#IMPORTAÇÃO DO numpy PARA TRABALHAR COM MATRIZ - np É SEU CODINOME
import numpy as np

#DECLARAÇÃO DA MATRIZ
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sumMatriz = 0

#LOOP QUE PRECORRE A MATRIZ E SOMA OS VALORES DE LINHA E COLUNA
for row in range(matriz.shape[0]):
   for col in range(matriz.shape[1]):
      sumMatriz = sumMatriz + matriz[row][col]

#SAÍDA DE DADOS
print("A soma de todos os elementos da matriz é: ", sumMatriz)