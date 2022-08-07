valor = int(input('Informe um número P: '))

divisores = []

for numero in range (1, valor + 1):
    if valor % numero == 0:
        divisores.append(numero)
        
print ('Divisores: {}' .format(divisores))
print ('Quantidade de divisores: {}' .format(len(divisores)))