# Tabela de dados 1
bw = ['1.4 MHz', '3 MHz', '5 MHz', '10 MHz', '15 MHz', '20 MHz']
rb = [6, 15, 25, 50, 75, 100]
sp = [72, 180, 300, 600, 900, 1200]

def PRB_SP(dado):  # deve receber o valor de largura de banda (ex.: 20 MHz)
    idBW = bw.index()
    return rb[idBW], sp[idBW]  # retorna uma tupla com dois valores

# Tabela de dados 2: MIMO

mimo = ['without mimo', '2x2', '4x4', '8x8']
valueMIMO = [1, 2, 4, 8]

def MIMO(dado):  # deve receber a configuração de antenas (ex.: 2x2)
    idMIMO = mimo.index(dado)
    return valueMIMO[idMIMO]

# Cyclic Prefix

cyclicPrefix = ['Normal', 'Extended']
valueCP = [7, 6]

def CP(dado):  # deve receber como dado a indicação se o CP é Normal ou Extended
    idCP = cyclicPrefix.index(dado)
    return valueCP[idCP]

# Modulação

MSC = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
tbsIndex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12, 13, 14,
15, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

def modulation(dado):  # deve receber o valor de MSC
    idTBS = MSC.index(dado)
    if 0 <= dado <= 9:
        return 'QPSK', tbsIndex[idTBS]
    elif 9 < dado <= 16:
        return '16 QAM', tbsIndex[idTBS]
    else:
        return '64 QAM', tbsIndex[idTBS]
