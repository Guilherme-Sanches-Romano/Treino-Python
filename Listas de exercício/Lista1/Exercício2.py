#Fornecido um número inteiro n (n ≥ 0), exibir o dígito mais à direita do valor, para tanto utilize o
#operador de resto (%).

#Declarando a variável 
n = int(input('Forneça um número:'))

#Fazendo o cálculo que retorna o ultimo dígito de qualquer número
n  = n%10 

#Monstrando o resultado 
print('O número mais à direita é o  %d' %n)
