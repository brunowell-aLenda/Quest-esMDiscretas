def soma(a, b):
    return 3*a + 3*b

def produto(a, b):
    return ((a*b) / 2)

from soma import soma
def associativo_adicao(a, b, c):
    if(soma(soma(a, b), c) == soma(a, soma(b, c))):
        return True
    return False

from produto import produto
def associativo_multiplicacao(a, b, c):
    if produto(produto(a, b), c) == produto(a, produto(b, c)):
        return True
    return False

from produto import produto
from soma import soma
def associativo(a, b, c):
    if(soma(soma(a, b), c) == soma(a, soma(b, c))) and \ produto(produto(a, b), c) == produto(a, produto(b, c)):
        return True
    return False

from soma import soma
def comutativo_adicao(a, b):
    if soma(a, b) == soma(b, a):
        return True
    return False

from produto import produto
def comutativo_multiplicacao(a, b):
    if produto(a, b) == produto(b, a):
        return True
    return False

from produto import produto
from soma import soma
def comutativo(a, b):
    if soma(a, b) == soma(b, a) and \ produto(a, b) == produto(b, a):
        return True
    return False

from produto import produto
from soma import soma
def distributivo_esquerda(a, b, c):
    if produto(soma(a, b), c) == soma(produto(a, c), produto(b,c)):
        return True
    return False

from produto import produto
from soma import soma
def distributivo(a, b, c):
    if produto(a, soma(b, c)) == soma(produto(a, b), produto(a,c)):
        return True
    return False

from soma import soma
def elemento_neutro_aditivo(a):
    e = -((2*a)/3)
    
    if soma(a, e) == soma(e, a) == a:
        return True
    return False

from produto import produto
def elemento_neutro_multiplicativo(a):
    e = 2
    
    if produto(a, e) == produto(e, a) == a:
        return True
    return False

from produto import produto
from soma import soma
def fechamento(a, b):
    valor_soma = soma(a, b)
    valor_produto = produto(a, b)
    
    if type(valor_soma) == type(a) == type(b) and \ type(valor_produto) == type(a) == type(b):
        return True
    else:
        if valor_produto.is_integer():
            valor_produto = int(valor_produto)
            if type(valor_soma) == type(a) == type(b) and \ type(valor_produto) == type(a) == type(b):
                return True
    return False

from soma import soma
def inverso_aditivo(a):
    e_inverso = -((11*a)/9)
    e_neutro = -((2*a)/3)
    
    if(round(soma(a, e_inverso), 0) == round(e_neutro, 0)):
        return True
    return False

from produto import produto
def inverso_multiplicativo(a):
    e_inverso = 4/a
    e_neutro = 2
    if(round(produto(a, e_inverso), 0) == e_neutro):
        return True
    return False

from associativo_adicao import associativo_adicao
from associativo_multiplicacao import associativo_multiplicacao
from comutativo_adicao import comutativo_adicao
from distributivo import distributivo
from distributivo_esquerda import distributivo_esquerda
from elemento_neutro_aditivo import elemento_neutro_aditivo
from inverso_aditivo import inverso_aditivo
def e_anel(a, b, c):
    if associativo_adicao(a, b, c) and \ comutativo_adicao(a, b) and \ elemento_neutro_aditivo(a) and \ inverso_aditivo(a) and \ associativo_multiplicacao(a, b, c) and \ distributivo(a, b, c) and \ distributivo_esquerda(a, b, c):
        return True
    return False



from associativo import associativo
from comutativo import comutativo
from distributivo import distributivo
from elemento_neutro_aditivo import elemento_neutro_aditivo
from elemento_neutro_multiplicativo import
elemento_neutro_multiplicativo
from inverso_aditivo import inverso_aditivo
from inverso_multiplicativo import inverso_multiplicativo
def e_corpo(a, b, c):
    if comutativo(a, b) and \ associativo(a, b, c) and \ distributivo(a, b, c) and \ elemento_neutro_aditivo(a) and \ elemento_neutro_multiplicativo(a) and \ inverso_aditivo(a) and \ inverso_multiplicativo(a):
        return True
    return False


from associativo import associativo
from elemento_neutro_aditivo import elemento_neutro_aditivo
from elemento_neutro_multiplicativo import
elemento_neutro_multiplicativo
from fechamento import fechamento
from inverso_aditivo import inverso_aditivo
from inverso_multiplicativo import inverso_multiplicativo
def e_grupo(a, b, c):
    if fechamento(a, b) and \ associativo(a, b, c) and \ elemento_neutro_aditivo(a) and \ elemento_neutro_multiplicativo(a) and \ inverso_aditivo(a) and \ inverso_multiplicativo(a): 
        return True 
    return False


from comutativo import comutativo
from grupo import e_grupo
try:
    a = int(input('Informe o a: '))
    b = int(input('Informe o b: '))
    c = int(input('Informe o c: '))

except:
    print('Todos os valores precisam ser inteiros')
    exit(1)

if e_grupo(a, b, c) and comutativo(a, b):
    print('É um grupo comutativo ou abeliano')
else:
    print('Não é grupo comutativo ou abeliano')


from corpo import e_corpo
try:
    a = int(input('Informe o a: '))
    b = int(input('Informe o b: '))
    c = int(input('Informe o c: '))

except:
    print('Todos os valores precisam ser inteiros')
    exit(1)

if e_corpo(a, b, c):
    print('É um corpo')
else:
    print('Não é um corpo')
  

from anel import e_anel
from comutativo_multiplicacao import comutativo_multiplicacao
try:
    a = int(input('Informe o a: '))
    b = int(input('Informe o b: '))
    c = int(input('Informe o c: '))

except:
    print('Todos os valores precisam ser inteiros')
    exit(1)

if e_anel(a, b, c) and comutativo_multiplicacao(a, b):
    print('É um anel comutativo')
else:
    print('Não é um anel comutativo')

    