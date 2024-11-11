nome = input('Digite seu nome: ')   
idade = input('Digite sua idade: ')

if nome and idade:
    print('Seu nome é ',nome )
    print('Sua idade é ',idade)
    print('Seu nome invertido é',nome[::-1])
else:
    print('Desculpe, você deixou campos vazios.')
    
if ' ' in nome:
    print('Seu nome contém espaços.')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Seu nome não cotém espaços.')
    