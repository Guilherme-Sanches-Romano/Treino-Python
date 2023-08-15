#Dado um salário atual em reais e uma idade em anos, calcular o novo salário, que será o salário atual
#acrescido da idade em porcentagem. Exemplo: salário atual = R$ 1000,00 e idade = 23, logo,
#novo salário = R$ 1000,00 + 23% de R$ 1000,00 = R$ 1230,00. Exiba apenas o novo salário.

s = float(input('Fale seu salário atual:'))
i = int(input('Fale sua idade:'))

p = i/100
s = s + (s*p)

print('Seu novo salário é R$ %d' %s)
