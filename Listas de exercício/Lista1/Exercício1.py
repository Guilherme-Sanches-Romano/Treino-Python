# Fornecido o preço unitário e a quantidade de uma determinada peça, calcular e exibir o total a pagar
# sabendo que haverá um desconto de 10%.

# Declarando as Variáveis
p = float(input('Quanto custa este item ?'))
q = float(input('Quantos itens vai levar ?'))
# Fazendo a conta para dar o valor final já com o desconto
t = (q * p)*0.90
# Exibindo o valor final com a variável
print('Valor total R$ %.2f' % t)

#Lembrendo que por padrão americano números decimais vem depois do ponto(.) e não vírgula(,) como no Brasil
