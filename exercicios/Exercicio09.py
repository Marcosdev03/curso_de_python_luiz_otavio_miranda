import os

palavra_secreta = 'planeta'
letras_acertadas = ''
num_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    num_tentativas += 1
    
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        
        
    palavra_formada = ''  
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
          palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
            
    print('Palavra formada:',palavra_formada)
 
    if palavra_formada == palavra_secreta:
            os.system('clear')
            print('Parabéns, você ganhou!')   
            print(f'A palavra secreta era {palavra_secreta}.')
            print('Números de tentativas:',num_tentativas)
            letras_acertadas = ''
            num_tentativas = 0
            
            