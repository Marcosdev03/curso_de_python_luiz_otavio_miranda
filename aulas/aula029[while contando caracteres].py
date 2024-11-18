# Define uma string que será analisada
frase = 'aaaooo'

# Inicializa variáveis para controlar o índice, a quantidade de vezes que uma letra apareceu,
# e qual letra apareceu mais vezes
i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

# Enquanto o índice 'i' for menor que o comprimento da string 'frase', o loop continua
while i < len(frase):
    # Pega a letra atual da string
    letra_atual = frase[i]

    # Se a letra atual for um espaço em branco, pula para a próxima iteração
    if letra_atual == ' ':
        i += 1
        continue

    # Conta quantas vezes a letra atual aparece na string
    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    # Se a quantidade de vezes que a letra atual aparece for maior que a quantidade
    # máxima já registrada, atualiza as variáveis de controle
    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    # Incrementa o índice para passar para a próxima letra
    i += 1

# Imprime o resultado final
print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)
