import time

n=int(input('digite o valor inicial de n: '))

soma=0

inicio = time.time()

for i in range(0,n): #somatorio
    soma += (1 / ((i+1) * ((i+1) + 1) * ((i+1) + 2)))

fim = time.time()
soma = round(soma, 7)

print("o tempo da primeira equacao eh {:.7f}".format(fim - inicio))
print("o valor da primeira equacao eh:", soma)
print('')

inicio = time.time()
soma_formula = ((n**2) + 3*n) / (4*(n**2) + 12 * n + 8)
fim = time.time()
soma_formula = round(soma_formula, 7)

print("o tempo da segunda formula eh {:.7f}".format(fim - inicio))
print("o valor da segunda formula eh", soma_formula)
print('')

if (soma == soma_formula):
    print("O valor da expressão é verdadeiro para n igual a: ", n)
else:
    print("o valor da expressão é falso para n igual a:", n)