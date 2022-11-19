rb = [6, 15, 25, 50, 75, 100]
tbsIndex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

nome_arquivo = 'valueTBS.txt'
arquivo = open(nome_arquivo)
linhas = arquivo.readlines()

v_TBS = list()
for i in range(len(linhas)):    
    v_TBS.append(linhas[i].replace('\n', '').split(','))

vTBS = list()
for i in range(len(v_TBS)):
    vTBS.append(list(map(int, v_TBS[i])))

def valueTBS(valorIndiceTBS, valorRB):
    id1 = tbsIndex.index(valorIndiceTBS)
    id2 = rb.index(valorRB)
    return vTBS[id1][id2]  # Valor do TBS com base em RB e índice TBS
