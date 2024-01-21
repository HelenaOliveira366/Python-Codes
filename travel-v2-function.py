#Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. 
#Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem


#ENTRADA DE DADOS
time = float(input("Digite o tempo gasto na viagem em hora: "))
speed = float(input("Digite a velocidade média em quilômetro: "))

#CÁLCULO DA DISTÂNCIA PERCORRIDA
def calculateDistance(time = time, speed = speed):
   distance = time * speed
   return distance

#CÁLCULO DO COMBUSTÍVEL USADO
def calculateFuel():
   usedLiters = distance/12
   return usedLiters

#IMPRESSÃO DOS RESULTADOS
print(f'O tempo de viagem foi: {time}')
print(f'A velocidade média na viagem foi: {speed}')

distance = calculateDistance()
print(f'A distância percorrida foi: {distance}')

usedLiters = calculateFuel()
print(f'A quantidade de combustível utilizado foi: {usedLiters}')