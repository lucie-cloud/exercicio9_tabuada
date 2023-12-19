# Tabuada

print('\n\t\t\t -- Consulte a tabuada -- \n')

def tabuada(x):
    tabuada = []
    for i in range(1, 11):
        tabuada.append(str(x) + ' x ' + str(1) + ' = ' + str(x*i))
    return tabuada

# Teste tabuada
for x in tabuada(5):
    print(x)