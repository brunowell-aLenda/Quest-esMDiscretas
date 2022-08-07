import math
import numpy
import time

def fatorial_sem_recursao(numero):
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

def fatorial_com_recursao(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial_com_recursao(numero-1)

numero = numpy.longdouble(input('Informe um número: '))

inicio_simples = time.time()
resultado_simples = fatorial_sem_recursao(numero)
fim_simples = time.time()

resultado_simples = round(resultado_simples, 7)
tempo_simples = fim_simples - inicio_simples

print('Fatorial simples: {}'.format(resultado_simples))

print('Tempo necessário: {:.7f}\n'.format(tempo_simples))

#------------------------------------#

inicio_recursivo = time.time()

resultado_recursivo = fatorial_com_recursao(numero)

fim_recursivo = time.time()

resultado_recursivo = round(resultado_recursivo, 7)

tempo_recursivo = fim_recursivo - inicio_recursivo


print('Fatorial recursivo: {}'.format(resultado_recursivo))

print('Tempo necessário: {:.7f}\n'.format(tempo_recursivo))

#------------------------------------#

inicio_formula = time.time()

resultado_formula=math.sqrt(2*(math.pi)*numero)*((numero/math.e)**numero)

fim_formula = time.time()

resultado_formula = round(resultado_formula, 7)

tempo_formula = fim_formula - inicio_formula

print('Fatorial de Stirling: {}'.format(resultado_formula))

print('Tempo necessário: {:.7f}\n'.format(tempo_formula))

#------------------------------------#

if resultado_simples == resultado_recursivo:
    print('Erro comparado ao dois resultados anteriores: {}'.format(resultado_simples - resultado_formula))

else:
    print('Erro comparado ao fatorial simples: {}'.format(resultado_simples - resultado_formula))
    
    print('Erro comparado ao fatorial recursivo: {}'.format(resultado_recursivo - resultado_formula))


print('')

print('Tempos:')

print('Fórmula de Stirling: {:.7f}'.format(tempo_formula))

print('Sem recursão: {:.7f}'.format(tempo_simples))

print('Com recursão: {:.7f}'.format(tempo_recursivo))