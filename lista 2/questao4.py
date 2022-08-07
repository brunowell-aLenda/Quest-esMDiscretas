a = int(input('Informe o número a: '))

b = int(input('Informe o número b: '))

k = int(input('Informe o número k: '))

if (a - b) % k == 0:
    print('{} é ≡ {} mod({})' .format(a, b, k))
else:
    print('{} não é ≡ {} mod({})' .format(a, b, k))
# O símbolo '≡' significa congruente