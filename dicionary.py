#Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos, fazendo a leitura dos valores por meio de uma estrutura de repetição. Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média

#DECLARAÇÃO DO DICIONÁRIO
studentsGrade = {}
average = 0.0

#LOOP PARA PREECHER O DICIONÁRIO COM NOMES E NOTAS (ENTRADA DE DADOS)
for i in range(3):
   name = input("Digite o nome do aluno: ")
   grade = float(input("Digite a nota do aluno: "))
   studentsGrade[name] = grade

#LOOP PARA EXIBIR OS DADOS DO DICIONÁRIO
print("NOME e NOTAS")
for key, value in studentsGrade.items():
   print(key, value)

#LOOP QUE PERCORRE E ARMAZENA TODOS OS VALORES DO DICIONÁRIO
for key, value in studentsGrade.items():
   average = average + value

#CÁLCULO DA MÉDIA DAS NOTAS
average /= 3

#SAÍDA DE DADOS
print("A média das notas dos 3 alunos é: ", round(average, 2))
