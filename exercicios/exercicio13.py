num = int(input('Digite um número:'))


def par_ou_impar():
   if num % 2  == 0:
      return f'O número {num} é par!'
   return f'O número {num} é impar!'


def frase():
    frase = par_ou_impar()
    print('='*len(frase))      
    print(frase)
    print('='*len(frase))

frase()
   



