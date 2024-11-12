try:
    
    num_int = int(input('Digite um número inteiro: '))


    if  num_int %2 == 0 :
        print('O número digitado é par.')
    else:
        print('O número digitado é impar.')
     
except ValueError:
    print('O número digitado não é um número inteiro.')
    