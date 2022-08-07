def fatorial(numero):
    if numero < 0:
        print('O valor não pode ser negativo')
    elif numero == 0:
        return 1
    else:
        resultado = 1
        while(numero > 1):
            resultado *= numero
            numero -= 1
            return resultado
n = 8
p = 5
resultado = fatorial(n) / (fatorial(p) * fatorial(n - p))
print('Resultado: {}'.format(resultado))