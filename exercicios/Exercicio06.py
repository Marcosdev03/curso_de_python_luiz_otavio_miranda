try:

    hora = int(input('Digite a hora: '))
    
    if hora >= 0 and hora <= 11:
        print(f'Bom dia.')
    
    elif hora >= 12 and hora <= 17:
        print('Boa tarde.')
    
    elif hora >= 18 and hora <= 23:
        print('Boa noite.')
except:
    print('Hora invalida, digite novamente...')
        
