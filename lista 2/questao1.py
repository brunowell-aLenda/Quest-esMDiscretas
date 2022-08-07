import math

a = float(input('Insira o primeiro valor: '))

b = float(input('Insira o segundo valor: '))

c = float(input('Insira o terceiro valor: '))

delta = b*b - 4*a*c

try:
    raiz_delta = math.sqrt(delta)

    if raiz_delta > 0:
        raiz1 = (-1*b + raiz_delta) / (2*a)
        raiz2 = (-1*b - raiz_delta) / (2*a)
        
        print('')
        print('Raízes reais maiores que zero')
        print('Fórmula: Xn = r1 * C1 + r2 * C2')
        print('Resultado: Xn = {} * C1 + {} * C2'.format(raiz1,raiz2))

    elif raiz_delta == 0:
        raiz = (-b / (2*a))
        
        print('')
        
        print('Raiz real igual a zero')
        print('Fórmula: Xn = r * C1 + C2 * r * n'.format(raiz,raiz))
        print('Resultado: Xn = {} * C1 + C2 * {} * n'.format(raiz,raiz))

        
except:
    raiz_delta_complexo = math.sqrt(abs(delta))
    
    raiz_complexa1_parte_esquerda = ((-1*b) / (2*a))
    
    raiz_complexa1_parte_direita = (raiz_delta_complexo / (2*a))
    
    if raiz_complexa1_parte_direita < 0:
        raiz_complexa1_str = '{} + {}*i'.format(raiz_complexa1_parte_esquerda,abs(raiz_complexa1_parte_direita))

    else:
        raiz_complexa1_str = '{} - {}*i'.format(raiz_complexa1_parte_esquerda,raiz_complexa1_parte_direita)
        
        raiz_complexa2_parte_esquerda = ((-1*b) / (2*a))
        
        raiz_complexa2_parte_direita = (raiz_delta_complexo / (2*a))
    
    if raiz_complexa2_parte_direita < 0:
        raiz_complexa2_str = '{} - {}*i'.format(raiz_complexa2_parte_esquerda,abs(raiz_complexa2_parte_direita))
        
    else:
        raiz_complexa2_str = '{} + {}*i'.format(raiz_complexa2_parte_esquerda,raiz_complexa2_parte_direita)

    print('')
    
    print('Fórmula: Xn = C1(r1)^n + C2(r2)^n')
    
    print('Resultado: Xn = C1({})^n + C2({})^n'.format(raiz_complexa1_str,raiz_complexa2_str))

    print('')

    a = raiz_complexa2_parte_esquerda

    b = raiz_complexa2_parte_direita
    
    p = round(math.sqrt((a**2) + (b**2)), 2)
    
    teta = round(math.atan(b/a), 2)
    
    print('Fórmula trigonométrica: p^n [C1*(cos(n*teta) + C2 *sen(n*teta)]')

    print('Resultado: Xn = {}^n [C1 * cos({}n) + C2 *sen({}n)]'.format(p, teta, teta))

# Exemplo maior que zero: 2, 3 e 1
# Exemplo igual a zero: 4, -4 e 1
# Exemplo menor que zero: 1, -4 e 5                                  
                                                