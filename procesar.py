import random as ran
DECIMALES = 4


def generateRandonArray(longitud=16):
    numList = []
    for i in range(longitud):
        numList.append(round(ran.random(), DECIMALES))
    return numList


def generarMatrizRandon(n=4, longitud=16):
    numMatriz = []
    for i in range(longitud):
        numMatriz.append(generateRandonArray(n))
    return numMatriz


def generateNumberForSum(dec=DECIMALES):
    r = 1
    for i in range(dec):
        r /= 10
    return r


def applyFunction(data=[]):
    mReturn = []
    for d in data:
        mReturn.append(d**2)
    return mReturn


def sumArrayValues(data=[]):
    suma = 0
    for d in data:
        suma += d
    return suma


def generateArrayK(data=[], sumFa=1):
    mReturn = []
    for d in data:
        mReturn.append(round(d/(sumFa*1.0), DECIMALES))
    return mReturn


def sumar(a, b):
    return a+b


def generarArrayOcurrenciasWithCeros(longitud=16):
    ocurrencias = []
    for i in range(longitud):
        ocurrencias.append(0)
    return ocurrencias


def generateInterval(data=[]):
    sumDecimal = generateNumberForSum(DECIMALES)
    listIntervals = []
    last = 0
    i = 0
    for d in data:
        if i == 0:
            listIntervals.append([0.0000, d])
            last += d
        elif i == len(data)-1:
            listIntervals.append(
                [round(last+sumDecimal, DECIMALES), round(last+d, DECIMALES-1)])
        else:
            listIntervals.append(
                [round(last+sumDecimal, DECIMALES), round(last+d, DECIMALES)])
            last += d
        i += 1
    return listIntervals


def positionValueInInteval(intervalos, value):
    i = 0
    for node in intervalos:
        if node[0] <= value and node[1] >= value:
            return i

        i += 1
    return -1


def setVectorOcurrencias(intervalos=[[0, 0]], randomValues=[]):
    ocurrencias = generarArrayOcurrenciasWithCeros(len(randomValues))
    for value in randomValues:
        i = positionValueInInteval(intervalos, value)
        if i != -1:
            ocurrencias[i] += 1
    return ocurrencias


def arraySeleccionReproducion(ocurrencias=[], cromosomas=[]):
    reproduccion = []
    i = 0
    for value in ocurrencias:
        for n in range(value):
            reproduccion.append(cromosomas[i])
        i += 1
    return reproduccion


def arrayCruze(reproduciones=[], aleatorios=[], puntoCruce=0, probabilidadCruzamiento=0):
    positions = []
    newReproduciones = reproduciones[:]
    i = 0
    for value in aleatorios:
        if value <= probabilidadCruzamiento:
            positions.append(i)
        if len(positions) == 2:
            break
        i += 1
    if len(positions) == 2:
        binary1 = newReproduciones[positions[0]]
        binary2 = newReproduciones[positions[1]]
        tail1 = binary1[puntoCruce:]
        tail2 = binary2[puntoCruce:]
        newReproduciones[positions[0]] = binary1[:puntoCruce] + tail2
        newReproduciones[positions[1]] = binary2[:puntoCruce] + tail1
    return newReproduciones


def mutarCromosomas(listCruce=[], randomMatriz=[[]], probabildadMutacion=0):
    listMutada = listCruce[:]
    i = 0
    for vector in randomMatriz:
        j = 0
        for value in vector:
            if value <= probabildadMutacion:
                cadena = listMutada[i]
                if cadena[j] == '0':
                    cadena = cadena[:j] + '1' + cadena[j+1:]
                else:
                    cadena = cadena[:j] + '0' + cadena[j+1:]
                listMutada[i] = cadena
            j += 1
        i += 1
    return listMutada


def convertArrayBinaryString2Decimal(mutaciones=[]):
    decimales = []
    matriz = []
    for value in mutaciones:
        decimales.append(int(value, 2))
    matriz.append(mutaciones)
    matriz.append(decimales)
    return matriz
