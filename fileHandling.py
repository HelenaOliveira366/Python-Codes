#Considerando o dicionário com o nome dos alunos e suas respectivas notas abaixo, crie uma estrutura de repetição para percorrer cada elemento do dicionário para gravar cada aluno em um novo arquivo de texto
#- Cada aluno deve ocupar uma linha do novo arquivo de texto
#- O formato deve ser: nome,nota (Pedro,8.0)
#- Após a criação do arquivo de texto, faça a leitura do arquivo e mostre todos os alunos
#alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

#MANIPULAR ARQUIVO COM PERMISSÃO DE ESCRITA
with open('studentGrades.txt', 'w') as txt:
   #LOOP PARA ESCREVER DADOS NO ARQUIVO
   for key, value in alunos.items():
      txt.write(f'{key},{value}\n')

#MANIPULAR ARQUIVO COM PERMISSÃO DE LEITURA
with open('studentGrades.txt', 'r') as txt:
   #LOOP PARA PERCORRER DADOS DO ARQUIVO
   for line in txt:
      print(line)
      #read = txt.readlines()

print("Dados escritos!")