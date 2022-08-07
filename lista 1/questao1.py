import time

n = int(input('Informe o n: '))

print('')

#------------------------------------#

somatorio = 0

inicio = time.time()

for i in range(0, n):
    somatorio += ( 1 / (((2*(i+1))-1)*((2*(i+1))+1)) )

fim = time.time()

somatorio = round(somatorio, 7) #Arredondando o valor da fórmula para 7 casas decimais

#------------------------------------#

inicio_formula = time.time()

somatorio_formula = n / ((2*n)+1)

fim_formula = time.time()

somatorio_formula = round(somatorio_formula, 7) #Arredondando o valor da fórmula para 7 casas decimais

print('Somatório: {}'.format(somatorio))

print('Fórmula: {}\n'.format(somatorio_formula))

print('O tempo necessário com os laços foi: {:.7f}'.format(fim - inicio))

print('O tempo necessário com a fórmula foi: {:.7f}\n'.format(fim_formula - inicio_formula))

print('Fórmula válida para o valor: {}'.format(n))

if somatorio == somatorio_formula:
    print('Fórmula válida para o valor: {}'.format(n))

else:
    print('Fórmula inválida para o valor: {}'.format(n))