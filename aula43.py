# nome = 'Gabriel Cerqueira'.lower()

# vogal = 'aeiou'
# consoante = 'bcdfghjklmnpqrstvwxyz'

# for letra in nome:
#     if letra in vogal:    
#         print(f'{letra.upper()}, é uma vogal')
#     elif letra in consoante:
#         print(f'{letra.upper()}, é uma consoante')
    
tabuada = input("Digite um número o qual você deseja saber a tabuada: ")
max = input("Até qual número você deseja saber a tabuada? ")

tabuadaNum = int(tabuada)
maxNum = int(max)

numeros = range(0,(maxNum),(tabuadaNum))

for numero in numeros:
    print(numero)