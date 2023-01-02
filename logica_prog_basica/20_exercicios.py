primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite o segundo valor: ')

valor_1 = int(primeiro_valor)
valor_2 = int(segundo_valor)

if valor_1 > valor_2:
    print(f'primeiro_valor, {valor_1=} é maior do que o valor_2, {valor_2=}')
elif valor_2 > valor_1:
    print(f'segundo_valor, {valor_2=} é maior do que o valor_1, {valor_1=}')
elif valor_1 == valor_2:
    print(f'Os valores são iguais, {valor_1=},  {valor_2=}')

else:
    print('Deu merda!')