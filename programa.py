#coloquei meu nome em realce e pra isso criei essa função 
def borda(s1)
    tam = len(s1)
    if tam:
        print('+', '-'*tam, '+')
        print('!', 'Paula de Souza Ribeiro', '!')
        print('+', '-' *tam,'+')
print('olá! seja bem vindo(a) a lojinha de t-shirts da')
borda('Paula de Souza Ribeiro')
print('Promoção de t-shirts!!! \n')
#criação de variáveis
valor = float(input('Insira o valor da t-shirt:'))
quantidade = int(input('Insira a quantidade de t-shirt: '))
#condição para os descontos 
if quantidade < 10:
    desconto = 0
elif quantidade <20:
    desconto = 0.1
else:
    desconto = 0.2
#Parametros para os valores
valor_sem_desconto = quantidade * valor
valor_com_desconto = valor * (1 - desconto)
valor_total = quantidade * valor_com_desconto
valor_desconto = quantidade * valor * desconto 
porcentagem_desconto = desconto * 100
#saida dos dados
print(f'valor total sem desconto: ', valor_sem_desconto)
print(f'valor unitário: R$ {valor: .2f}')
print(f'valor com desconto: R$ {valor_total:.2f} ({porcentagem_desconto: .0f}% de desconto)')
print(f'valor total: R${valor_total: .2f} (desconto total: R$ {valor_desconto: .2f})')