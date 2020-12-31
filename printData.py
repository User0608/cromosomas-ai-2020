def dibujaMatriz(M):
    ii = len(M)
    if ii > 0:
        jj = len(M[1])
    else:
        return
    for j in range(0, jj, 1):
        fila = ''
        for i in range(ii):
            fila = fila + str(M[i][j]) + "\t"
        print(fila)
