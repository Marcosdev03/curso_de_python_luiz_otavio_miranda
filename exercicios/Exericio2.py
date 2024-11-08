nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura ** 2)

print('Nome:',nome)
print('Altura:',altura)
print('Peso:',peso)
print('IMC:{:.3f}'.format(imc)) 

