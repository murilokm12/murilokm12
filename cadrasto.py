listaUser=['jose','paulo']
while True:
    option=input('Digite uma opção:')

    if option == '1' :

     nome=input('Digite seu nome: ')

     listaUser.append(nome)

    elif option == '2':

     print(listaUser)  

    elif option =='3':

        nomeDelete=input('Digite o nome que quer deletar: ')
    
        for item in listaUser:
         if item == nomeDelete:
          listaUser.remove(nomeDelete)
          print('Nome deletado')
        
         else:
           print('Não achei esse nome na lista!')
       
    elif option == '0':
        print('Tchau Tchau')

        break;

    

