import time

def fatorial(num):
    if num < 0:
        print('O valor não pode ser negativo')
    
    elif num == 0:
        return 1
    
    else:
        fact = 1
        while(num > 1):
            fact *= num
            num -= 1
        return fact

n=int(input('digite o valor inicial de n: '))

inicio_laco = time.time()

produto = 1

for i in range(1, n):
    produto *= (1 - (1/((i+1)**2)))

fim_laco = time.time()

produto = round(produto, 7)

print('Resultado com o laço de repetição: {}'.format(produto))

print('Tempo necessário: {:.7f}'.format(fim_laco - inicio_laco))

print('')

inicio_formula = time.time()

formula = (((2*(n**2)) + (2*n)) / (2*n)**2)

fim_formula = time.time()

formula = round(formula, 7)

print('Resultado com a fórfmula: {}'.format(formula))

print('Tempo necessário: {:.7f}'.format(fim_formula - inicio_formula))

if produto == formula:
    print('O valor da expressão é verdadeiro para n igual a: {}'.format(n))

else:
    print('O valor da expressão é falso para n igual a {}'.format(n))