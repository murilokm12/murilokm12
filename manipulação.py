
try:

 with open('arquivo1','r') as info:

    print(info.read())


except:
  print('Ocorrreu um erro ao tentar ler o arquivo, mas irei criar pra voce')

with open('arquivo1','w') as info:
  info.write('Arquivo criado.')               