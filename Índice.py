lista = ['marcos', 'Murilo', 'maria']
print('lista:', lista)

nome = input('Digite o nome que voce quer excluir :')



try:
    lista.remove(nome)
    print('nome excluido')
except:
    print('o nome nao existe')




