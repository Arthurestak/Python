frase = 'asfaaf99999999'

letras = "abcdefghijklmnopqrstuvwxyz"

i = 0

numero_aparicoes = 0
letra_maior_frequencia = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i+=1
        continue

    numero_aparicoes_atual = frase.count(letra_atual)

    if numero_aparicoes < numero_aparicoes_atual:
        numero_aparicoes = numero_aparicoes_atual
        letra_maior_frequencia = letra_atual

    i += 1

if letra_maior_frequencia in letras:
    print(f'A letra que apareceu mais vezes foi "{letra_maior_frequencia}", e apareceu {numero_aparicoes} vezes!')
else:
    print(f'O simbolo que mais apareceu foi "{letra_maior_frequencia}"!')
