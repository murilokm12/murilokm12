lista = ['marcos', 'Murilo', 'maria']
print('lista inicial:', lista)

while True:
    nome = input('Digite o nome que você quer excluir: ')

    if nome in lista:
        lista.remove(nome)
        print('Nome excluído!')
        print('Lista atualizada:', lista)
        break   
    else:
        print('O nome não existe, tente novamente.')
        
