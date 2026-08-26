

# atividade  3 



def criar_notas():
    global lista_nomes
    lista_nomes =  ['ana','Fernanda','Caio','Eloysa']
    l = []
    for n in range(len(lista_nomes)):
        n1  =  float(input('Nota 1'))
        n2  =  float(input('Nota 2'))
        n3 =  float(input('Nota 3'))
        l.append([n1,n2,n3])
        print('---' * 10)
    return l    



def estatistica():
    notas  =  criar_notas()
    nomes  =  lista_nomes
    medias =  []
    for n in range(len(nomes)):
        print('aluno: ', nomes[n])
        media  =  sum(notas[n])/len(notas[n])
        print(media)
        medias.append(media)
    print('medias:', medias)
    maior, menor  = max(medias), min(medias)
    print('maior:', maior, 'menor:', menor)
    maior_i = medias.index(maior)
    menor_i = medias.index(menor)
    print('O aluno com a maior média é ', nomes[maior_i])
    print('O aluno com a menor média  é ', nomes[menor_i])    
        