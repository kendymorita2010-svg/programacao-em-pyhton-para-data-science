import statistics 



def criar_notas():
    listas_nomes = ['ana', 'julia', 'fernanda', 'bernardo']
    notas_aluno = []
    for n in range(len(listas_nomes)):
        n1 = float(input('nota 1 >>'))
        n2 = float(input('nota 2 >>'))
        n3 = float(input('nota 3 >>'))
        notas_aluno.append([n1,n2,n3])
    return notas_aluno    
           



def analise():
    listas_notas = criar_notas()   