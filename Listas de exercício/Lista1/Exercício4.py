#Dado um número inteiro n (com quatro dígitos), exibir o dígito mais à esquerda do valor.

n = int(input('Forneça um número de 4 dígitos:'))

n = n//1000

print('Os 2 dígitos mais à esquerda são %d' %n)
