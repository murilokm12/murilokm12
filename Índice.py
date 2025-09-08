print('lista:','marcos,Murilo,maria')

nome = input('Digite o nome que voce quer excluir :')



try:
    lista.remove(nome)
    print('nome excluido')
except:
    print('o nome nao existe')



