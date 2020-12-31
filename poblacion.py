import random as r


def buildData(n=16, longitud=16):
    num = 0
    nums = []
    for i in range(longitud):
        num = r.randint(0, 2**n)
        nums.append(num)
    return nums


def generateZeros(n=0):
    zeros = ''
    for i in range(n):
        zeros = zeros+"0"
    return zeros


def convertBinary2String(listaNumeros=[], n=16):
    binaryNums = []
    for num in listaNumeros:
        bbb = "{0:b}".format(num)
        if n - len(bbb) > 0:
            bbb = generateZeros(n - len(bbb))+bbb
        binaryNums.append(bbb)
    return binaryNums


def getData(n=16, longitud=16):
    data = []
    retorno = buildData(n, longitud)
    data.append(retorno)
    data.insert(0, convertBinary2String(retorno, n))

    return data
