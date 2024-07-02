# Testando se os grafos satisfazem os Teoremas de Dirac, Ore e Bondy & Chvátal

def grau_vertice(arestas, vertice):
    # Conta quantas arestas estão conectadas ao vértice
    grau = 0
    for aresta in arestas:
        if vertice in aresta:
            grau += 1
    return grau

def verifica_dirac(vertices, arestas):
    n = len(vertices)
    for vertice in vertices:
        grau_minimo = n / 2
        grau = grau_vertice(arestas, vertice)
        if grau < grau_minimo:
            return False
    return True

def verifica_ore(vertices, arestas):
    n = len(vertices)
    for i in range(n):
        for j in range(i+1, n):
            # Verifica se os vértices não são adjacentes
            if (vertices[i], vertices[j]) not in arestas and (vertices[j], vertices[i]) not in arestas:
                grau_i = grau_vertice(arestas, vertices[i])
                grau_j = grau_vertice(arestas, vertices[j])
                if grau_i + grau_j < n:
                    return False
    return True

def verifica_bondy(vertices, arestas):
    n = len(vertices)
    arestas_nao_adjacentes = []
    for i in range(n):
        for j in range(i+1, n):
            # Verifica se os vértices não são adjacentes
            if (vertices[i], vertices[j]) not in arestas and (vertices[j], vertices[i]) not in arestas:
                arestas_nao_adjacentes.append((vertices[i],vertices[j]))
    #ordena as somas dos graus do maior para o menor
    arestas_nao_adjacentes = sorted(
        arestas_nao_adjacentes,
        key=lambda aresta: grau_vertice(arestas, aresta[0]) + grau_vertice(arestas,aresta[1]),
        reverse=True) #do maior para o menor

    for aresta in arestas_nao_adjacentes:
        i,j = aresta
        grau_i = grau_vertice(arestas,i )
        grau_j = grau_vertice(arestas,j)
        if grau_i + grau_j >= n:  #verificando se soma dos graus dos vercies é maior ou igual ao numero de vertices
            arestas.append(aresta) #adcionando aresta caso for vdd
        else:
            return False # nao satifaz

    # Verificar se cada vértice tem exatamente 6 arestas
    for vertice in vertices:
        grau_vertice_atual = grau_vertice(arestas, vertice)
        if grau_vertice_atual != n - 1:
            return False

    return True

vertices = [1, 2, 3, 4, 5, 6, 7]

#grafo 1
arestas1 = [(1, 2), (1, 3), (1, 6), (1, 7),
            (2, 3), (2, 4), (2, 6),
            (3, 4), (3, 5),
            (4, 5), (4, 7),
            (5, 6), (5, 7),
            (6, 7)]

#grafo 2
arestas2 = [(1, 2), (1, 3), (1, 6), (1, 7),
            (2, 3), (2, 4), (2, 6),
            (3, 4),
            (4, 5), (4, 7),
            (5, 6), (5, 7),
            (6, 7)]

#grafo 3
arestas3 = [(1, 2), (1, 3), (1, 6), (1, 7),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 6), (5, 7),
            (6, 7)]

#grafo 4
arestas4 = [(1, 2), (1, 3), (1, 6), (1, 7),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 6),
            (6, 7)]



if verifica_dirac(vertices, arestas4):
    print("O grafo satisfaz o Teorema de Dirac.")
else:
    print("O grafo não satisfaz o Teorema de Dirac.")


if verifica_ore(vertices, arestas4):
    print("O grafo satisfaz o Teorema de Ore.")
else:
    print("O grafo não satisfaz o Teorema de Ore.")


if verifica_bondy(vertices, arestas4):
    print("O grafo satisfaz o Teorema de Bondy & Chvátal.")
else:
    print("O grafo não satisfaz o Teorema de Bondy & Chvátal.")
