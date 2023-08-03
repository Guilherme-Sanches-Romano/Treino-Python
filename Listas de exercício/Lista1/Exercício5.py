#Fornecido um número inteiro n (1000 ≤ n ≤ 9999), exibir a soma dos dois dígitos à esquerda com os
#dois dígitos à direita. Exemplo: n = 3689, logo, a saída é 36 + 89 = 125.
n = int(input('Forneça um número de 4 dígitos:'))

p = n//100
b = n %100

m = b + p 

print('A soma dos  dois primeiros dígitos com os dois últimos é: %d' %m) 

