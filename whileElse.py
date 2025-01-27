string = 'Thalia, amor da minha vida'.lower()
vogais = 'aeiou'
consoantes = 'bcdfghjklmnpqrstvwxyz'

i = 0
while i < len(string):
    letra = string[i]

    if letra in vogais:
         print(f'{letra}, é uma vogal')
    elif letra in consoantes:
         print(f'{letra}, é uma consoante')
    
    i += 1
else:
    print('O else foi executado.')
print('fora do while')