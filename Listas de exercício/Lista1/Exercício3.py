#Fornecido um número inteiro n (n > 10), exibir o valor correspondente aos dois dígitos mais à direita de
#n, sem utilizar o operador de resto.

n = int(input('Forneça um valor maior que 10:'))

m = n//100

r = n - m *100  

print('Os dois números à direita são os %d' %r)
