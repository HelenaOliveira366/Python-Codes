#Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. 
#A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a temperatura em graus Celsius


print("CONVERSOR DE CELSIUS PARA FAHRENHEIT")

def converterTemp():
   celsius = float(input("Digite a temperatura em graus celsius: "))
   fahrenheit = (9 * celsius + 160)/5
   return print("Temperatura em Fahrenheit: ", fahrenheit) 

converterTemp()