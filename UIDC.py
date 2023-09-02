with open('dados.txt') as dados:
    lines = dados.readlines()
    

code1 = lines[1]
code4 = lines[4]
code7 = lines[7]
code10 = lines[10]

def Uniao(conjuntos):
    conjuntos1 = conjuntos['conjunto1'].replace(",","").split()
    conjuntos2 = conjuntos['conjunto2'].replace(",","").split()
    uniao = [] 
    for item in conjuntos1:
        if (item not in uniao):
            uniao.append(item)
    for item in conjuntos2:
        if item not in uniao:
            uniao.append(item)
    print('União: conjunto 1 ' + '{' + f'{", ".join(conjuntos1)}'+ '},' + f' conjunto2 ' + '{' + f'{", ".join(conjuntos2)}'+ '}' + '. Resultado: '+'{'+f'{", ".join(conjuntos1)}' + '}')

def Intersecao(conjuntos):
    conjuntos1 = conjuntos['conjunto1'].replace(",","").split()
    conjuntos2 = conjuntos['conjunto2'].replace(",","").split()
    Intersecao = [] 
    for item in conjuntos1:
        if (item in conjuntos2):
            Intersecao.append(item)
    print('Interseção: conjunto 1 ' + '{' + f'{", ".join(conjuntos1)}'+ '},' + ' conjunto2 ' + '{' + f'{", ".join(conjuntos2)}' + '}' + f'. Resultado: ' + '{' + f'{", ".join(Intersecao)}' + '}')

def Diferenca(conjuntos):
    conjuntos1 = conjuntos['conjunto1'].replace(",","").split()
    conjuntos2 = conjuntos['conjunto2'].replace(",","").split()
    diferenca = conjuntos['conjunto1'].replace(",","").split()
    for item in conjuntos2:
        if (item in conjuntos1):
            diferenca.remove(item)
    print('Diferença: conjunto 1 ' + '{' + f'{", ".join(conjuntos1)}'+ '},' + ' conjunto2 ' + '{' + f'{", ".join(conjuntos2)}' + '}' + f'. Resultado: ' + '{' + f'{", ".join(diferenca)}' + '}')

def Produto(conjuntos):
    conjuntos1 = conjuntos['conjunto1'].replace(",","").split()
    newConjunto1 = []
    for item in conjuntos1:
        if item not in newConjunto1:
            newConjunto1.append(item)
    conjuntos2 = conjuntos['conjunto2'].replace(",","").split()
    newConjunto2 = []
    for item in conjuntos2:
        if item not in newConjunto2:
            newConjunto2.append(item)
    Produto = [] 
    for item in newConjunto1:
        for item2 in newConjunto2:
            Produto.append(f'{item, item2}')
    print('Produto cartesiano: conjunto 1 ' + '{' + f'{", ".join(conjuntos1)}'+ '},' + ' conjunto2 ' + '{' + f'{", ".join(conjuntos2)}' + '}' + f'. Resultado: ' + '{' + f'{", ".join(Produto)}' + '}')


def ReadCode(code, conjunto):
    match code.split()[0]:
        case 'U':
            Uniao(conjunto)
        case 'I':
            Intersecao(conjunto)
        case 'D':
            Diferenca(conjunto)
        case 'C':
            Produto(conjunto)         
    
conjunto1 = {
    'conjunto1': lines[2],
    "conjunto2": lines[3]
}
conjunto2 = {
    'conjunto1': lines[5],
    "conjunto2": lines[6]
}
conjunto3 = {
    'conjunto1': lines[8],
    "conjunto2": lines[9]
}
conjunto4  = {
    'conjunto1': lines[11],
    "conjunto2": lines[12]
}


ReadCode(code1, conjunto1)
ReadCode(code4, conjunto2)
ReadCode(code7, conjunto3)
ReadCode(code10, conjunto4)
