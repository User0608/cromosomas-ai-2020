import poblacion as pl
import printData as out
import procesar
import random
import mate
# Variables Globales
LENGTH = 32
N = 16
PROBABILIDAD_CRUZAMIENTO = 0.4
PROBABILIDAD_MUTACION = 0.1
ITERACIONES = 100

# Inicio programa
Traza = []


def init():
    matrizDatos = pl.getData(N, LENGTH)
    for i in range(ITERACIONES):
        randomValues = procesar.generateRandonArray(LENGTH)
        sumFa = 0
        # valors para el cruce
        randomValuesForCruce = procesar.generateRandonArray(LENGTH)
        puntoCruce = random.randint(0, N-1)

        # Valores, matriz para mutación
        randomMatriz = procesar.generarMatrizRandon(N, LENGTH)

        datosFa = procesar.applyFunction(matrizDatos[1])
        sumFa = procesar.sumArrayValues(datosFa)
        kList = procesar.generateArrayK(datosFa, sumFa)
        intervalList = procesar.generateInterval(kList)
        ocurrencias = procesar.setVectorOcurrencias(intervalList, randomValues)
        reproduciones = procesar.arraySeleccionReproducion(
            ocurrencias, matrizDatos[0])
        cruce = procesar.arrayCruze(
            reproduciones, randomValuesForCruce, puntoCruce, PROBABILIDAD_CRUZAMIENTO)
        mutacion = procesar.mutarCromosomas(
            cruce, randomMatriz, PROBABILIDAD_MUTACION)

        matrizDatos.append(datosFa)
        matrizDatos.append(kList)
        matrizDatos.append(intervalList)
        matrizDatos.append(ocurrencias)
        matrizDatos.append(reproduciones)
        matrizDatos.append(cruce)
        matrizDatos.append(mutacion)
        desviacionEstanda = mate.deviacionStandar(datosFa)
        print("Iteración", i+1)
        # out.dibujaMatriz(matrizDatos)
        print("Suma Fa : ", sumFa)
        print("Punto Cruce : ", puntoCruce)
        print("Desviacion estándar : ", desviacionEstanda)
        print(
            "__________________________________________________")
        Traza.append([matrizDatos, desviacionEstanda])
        matrizDatos = procesar.convertArrayBinaryString2Decimal(mutacion)


def analisisData():
    theBestDesviacionEstandar = 99999999999999
    i = 0
    index = -1
    for data in Traza:
        if data[1] < theBestDesviacionEstandar:
            theBestDesviacionEstandar = data[1]
            index = i
        i += 1
    print("")
    print("Analisis de resultados")
    print("")
    print("N: ", N, "Numero total de iteraciones: ", ITERACIONES)
    print("PROBABILIDAD DE MUTACIÓN: : ", PROBABILIDAD_MUTACION)
    print("PROBABILIDAD DE CRUZAMIENTO: : ", PROBABILIDAD_CRUZAMIENTO)
    print("La menor desviacion estándar : ", theBestDesviacionEstandar)
    matriz = Traza[index][0]
    theBestFitness = 0
    index = -1
    i = 0
    for data in matriz[2]:
        if data > theBestFitness:
            theBestFitness = data
            index = i
        i += 1
    cromosoma = ''
    if index != -1:
        cromosoma = matriz[0][index]
    print("El mejor cromosoma es: ", cromosoma,
          ", con un Fa de: ", theBestFitness)


init()
analisisData()
