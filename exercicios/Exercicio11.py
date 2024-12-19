cpf = '12092513613'
nove_digitos = cpf[:9]
cont = 10
soma = 0

for num in nove_digitos:
  multiplicacao = int(num) * cont
  soma += multiplicacao
  cont -= 1
  
print(soma)
 