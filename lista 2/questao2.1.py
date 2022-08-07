def e_primo(numero):
    primo = True if numero > 1 else False
    
    if not primo:
        return False
    for divisor in range(2, numero-1):
        if numero % divisor == 0:
            return False
    return True

valor = int(input('Informe um valor: '))
if(e_primo(valor)):
    print('O número {} é primo'.format(valor))
else:
    print('O número {} não é primo'.format(valor))

print('')
print('Números primos até o {}:'.format(valor))
primos_ate_valor = []
for numero in range(1, valor + 1):
    if(e_primo(numero)):
        primos_ate_valor.append(numero)
 
if primos_ate_valor :
    print(primos_ate_valor)
else:
    print('Nenhum')