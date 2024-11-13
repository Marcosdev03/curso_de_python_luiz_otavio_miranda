while True:
    num_1 = input('Digite um numero: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador (+-*/): ')



    try:
        num_1 = float(num_1)
        num_2 = float(num_2)
        numeros_valido = True
    except ValueError: 
        numeros_valido = None
        
        if numeros_valido is None:
            print('Um ou ambos os números são invalidos')
        continue
    operadores_permitidos = '*/-+'  
    
    
    if operador not in operadores_permitidos:
            print('Operador inválido.')
            continue
        
    if len(operador) > 1:
            print('Digite apenas um operador.')
            continue
        
    print('Realizando sua conta.Confira o resultado abaixo')
    
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2) 
    elif operador == '*':
        print(num_1 *num_2)     

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
    
  