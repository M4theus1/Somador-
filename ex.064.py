c = 0
numeros = 0
n = 0
soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma = soma + n
    numeros = numeros + 1
    n = int(input('Digite um número [999 para parar]: '))
print('Foram digitados {} números e a soma deles foi de {}'.format(numeros, soma))