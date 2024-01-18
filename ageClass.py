#Leia a idade do usuário e classifique-o em:
#- Criança – 0 a 12 anos
#- Adolescente – 13 a 17 anos
#- Adulto – acima de 18 anos
#-Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida

#ENTRADA DA IADADE DO USUÁRIO
age = int(input("Digite sua idade: "))

#CHECAGEM DAS FAIXA ETÁRIAS
if age >= 0 and age <= 12:
   print("Você é uma criança")
elif age >= 13 and age <= 17:
   print("Você é um adolescente")
elif age >= 18:
   print("Você é um adulto")
else:
   print("Idade inválida")