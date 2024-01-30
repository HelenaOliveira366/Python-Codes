#Crie expressões regulares para extrair as seguintes informações do texto abaixo (use a função findall):
#- Números
#- CEPs
#- URLs

#Exemplos:
#'Helena', 'Eldezan', '04112022', '1.2'
#"(93)98425-3614", "68022-160"
#"https://github.com/HelenaOliveira366", "Link", "URL", "https://github.com/HelenaOliveira366/Python-Codes"

#IMPORTAÇÃO DO MÓDULO PARA TRABALHAR COM EXPRESSÕES REGULARES
import re

#LISTAS
numberList = []
CEPsList = []
URLsList = []

#FUNÇÃO QUE RECEBE NÚMEROS DO USER
def inputNumbers():
   print("Digite os números")
   for i in range(4):
      number = input("Entrada de dados: ")
      numberList.append(number)
   return numberList

#FUNÇÃO QUE CAPTURA NÚMEROS
def captureNumber():
   return re.findall('\d+', str(numberList))

#FUNÇÃO QUE RECEBE CEPS DO USER
def inputCeps():
   print("Digite os CEPs")
   for i in range(4):
      cep = input("Entrada de dados: ")
      CEPsList.append(cep)
   return CEPsList

#FUNÇÃO QUE CAPTURA CEP
def captureCEPs():
   return re.findall('\d{5}-\d{3}', str(CEPsList))

#FUNÇÃO QUE RECEBE URLS DO USER
def inputUrls():
   print("Digite as URLs")
   for i in range(4):
      url = input("Entrada de dados: ")
      URLsList.append(url)
   return URLsList

#FUNÇÃO QUE CAPTURA URL
def captureURLs():
   return re.findall('https?://[A-Za-z0-9./|]+', str(URLsList))

#CHAMADA DAS FUNÇÕES
inputNumbers()
print("Número(s) digitado(s): ", captureNumber())
inputCeps()
print("CEP(s) digitado(s): ", captureCEPs())
inputUrls()
print("URL(s) digitado(s): ", captureURLs())