import procesar


def sumatoriaCuadrada(fa=[], _x=0):
    suma = 0
    for d in fa:
        suma += (d - _x)**2
    return suma


def deviacionStandar(fa=[]):
    suma = procesar.sumArrayValues(fa)
    n = len(fa)
    _x = suma/n
    sumaPow = sumatoriaCuadrada(fa, _x)
    desviacion = (sumaPow/n)**(1/2)
    return desviacion
