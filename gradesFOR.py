#Ler 5 notas e informar a média

average = 0.0
for i in range(1, 6):
   grade = float(input("Digite a nota: "))
   average = average + grade
average = average/5
print("A média das 5 notas é : ", average)