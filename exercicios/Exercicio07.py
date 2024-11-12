try:

    nome = int(input('Digite um nome: '))   
    nome1 = len(nome)

    if nome1 <= 4:
        print('Seu nome é curto')
    elif nome1 >= 5 and nome1 <= 6 : 
        print('Seu nome é normal.')
    elif nome1 >= 7:
        print('Seu nome é muito grande.')
except:
    print('Digite um nome válido')