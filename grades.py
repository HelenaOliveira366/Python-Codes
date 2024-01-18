#Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas M1, M2 e M3; passando por um cálculo da média aritmética. Após a média calculada, devemos anunciar se o aluno foi aprovado, reprovado ou pegou exame
#- Se a média estiver entre 0.0 e 4.0, o aluno está reprovado
#- Se a média estiver entre 4.1 e 6.0, o aluno pegou exame
#- Se a média for maior do que 6.0, o aluno está aprovado
#- Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0, está aprovado, senão; está reprovado

#ETRADA DAS NOTAS
print("Digite suas notas em Programação I:")
grade1 = float(input("Primeira nota: "))
grade2 = float(input("Segunda nota: "))
grade3 = float(input("Terceira nota: "))

#VERIFICAÇÃO DA MÉDIA
average = (grade1 + grade2 + grade3)/3
print("Sua média foi ", round(average, 2))

#VERIFICAÇÃO DE APROVAÇÃO E REPROVAÇÃO
if average >= 0.0 and average <= 4.0:
   print("Você está reprovado!")
elif average >= 4.1 and average <= 5.9:
   print("Você precisa fazer prova final! Se já fez e obteve nota, digite abaixo:")
   exameGrade = float(input("Digite a nota da prova final: "))
   if exameGrade >= 6.0:
      print("Você está aprovado!")
   else:
      print("Você está reprovado!")
elif average >= 6.0:
   print("Você está aprovado!")
else:
   print("Valor inválido")