import poblacion as pl
import printData as out
import procesar
matrizDatos = pl.getData(4, 10)
matrizDatos.append(procesar.applyFunction(matrizDatos[1]))

out.dibujaMatriz(matrizDatos)
