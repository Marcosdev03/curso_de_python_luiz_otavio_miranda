def multiplica(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado
    
numeros = []
    
for c in range(1,5):
       num = (int(input('Digite um número:')))
       numeros.append(num)

def frase():
    frase = f'O resultado da multiplicação de todos os números é {multiplica(*numeros)}.'
    print('='*len(frase))      
    print(frase)
    print('='*len(frase))


frase()    

