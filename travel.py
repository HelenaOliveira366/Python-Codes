#Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro.
#Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem


#DISTÂNCIA PERCORRIDA
time = float(input("Digite o tempo que levou a viagem em horas: "))
averageSpeed = float(input("Digite a velocidade média em quilômetro: "))
distance = time * averageSpeed

#LITROS DE COMBUSTÍVEL UTILIZADA NA VIAGEM
#o automóvel que faz 12 Km por litro
usedLiters = distance/12
usedLiters = round(usedLiters, 2)

#SAÍDA DOS DADOS
print(f'Velocidade média = {averageSpeed}\nTempo gasto na viagem = {time} hrs\nDistância percorrida = {distance} km\nQuantidade de litros utilizados = {usedLiters} l')