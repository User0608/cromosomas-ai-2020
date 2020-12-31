
def intervaloToString(dd=[]):
    if len(dd) == 2:
        if dd[0] == 0.0 or dd[1] == 1.0:
            return "["+str(dd[0]) + " - " + str(dd[1])+"]    "
        return "["+str(dd[0]) + " - " + str(dd[1])+"]"
    return "null"


def dibujaMatriz(M):
    ii = len(M)
    if ii > 0:
        jj = len(M[1])
    else:
        return
    for j in range(0, jj, 1):
        fila = ''
        for i in range(ii):
            if type(M[i][j]) is list:
                fila = fila + intervaloToString(M[i][j]) + "\t"
            else:
                fila = fila + str(M[i][j]) + "\t"
        print(fila)
