nome = 'Manoel Nascimento'
altura = 1.80
peso = 87
imc = peso / (altura * altura)

print(nome, 'tem', altura, 'de altura, pesa', peso, 'quilos e seu IMC é de', round(imc, 2))

# "f-strings"

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)