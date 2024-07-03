# Verificando se os grafos são Eulerianos, Semi-Eulerianos ou Não Eulerianos.
# Se forem Eulerianos ou Semi Eulerianos, o caminho é impresso.
# São atribuídos, arbitrariamente, pesos para cada aresta e é calculada a soma
# dos pesos ao longo do caminho.

import random

def grau_vertice(arestas, vertice):
    grau = 0
    for aresta in arestas:
        if vertice in aresta:
            grau += 1
    return grau

def verifica_grafo(vertices, arestas):
    vertices_impares = []
    n = len(vertices)
    qtd_vertices_impares = 0
    qtd_vertices_pares = 0
    for vertice in vertices:
        grau = grau_vertice(arestas, vertice)
        if grau % 2 == 0:
            qtd_vertices_pares += 1
        else:
            qtd_vertices_impares += 1
            vertices_impares.append(vertice)
    if qtd_vertices_impares == 2:
        return "semi-euleriano", vertices_impares
    elif qtd_vertices_pares == n:
        return "euleriano", vertices_impares
    else:
        return "não euleriano", vertices_impares



def encontrar_caminho_euleriano(arestas, vertices_impares):
    primeiro_vertice = 1
    if len(vertices_impares) == 2:
        primeiro_vertice = vertices_impares[0]
    grafo = {}
    # determina os vizinhos de cada vertice
    for u, v in arestas:
        if u not in grafo:
            grafo[u] = []
        if v not in grafo:
            grafo[v] = []
        grafo[u].append(v)
        
        grafo[v].append(u)
        
    caminho = []
    pilha = [primeiro_vertice]
    
    while pilha:
         #pega o ultimo vertice adj do 1o impar
        v = pilha[-1]
        # se não existem mais vertices nao visitados
        if not grafo[v]:
            #remove um vertice da pilha e aloca ele no caminho
            caminho.append(pilha.pop())
            
        else:
            u = grafo[v].pop()         
            grafo[u].remove(v)
            pilha.append(u)
    return caminho[::-1]

def gerar_pesos (arestas):
    pesos = [random.randint(1, 12) for _ in range(len(arestas))]
    pesos_arestas = {(aresta[0], aresta[1]): pesos for aresta, pesos in zip(arestas, pesos)}
    return pesos_arestas

def calcular (caminho, pesos_arestas):
    contador_pesos = 0
    for i in range(len(caminho)):
        if i == len(caminho) - 1:
            break
        aresta_atual = (caminho[i], caminho[i + 1])
        if aresta_atual not in pesos_arestas:
            aresta_atual = (caminho[i+1], caminho[i])
        contador_pesos = contador_pesos + pesos_arestas[aresta_atual]
    return contador_pesos

vertices = [1, 2, 3, 4, 5, 6, 7]

# grafo 1
arestas1 = [(1, 2), (1, 3), (1, 6), (1, 7),
            (2, 3), (2, 4), (2, 6),
            (3, 4), (3, 5),
            (4, 5), (4, 7),
            (5, 6), (5, 7),
            (6, 7)]

# grafo 2
arestas2 = [(1, 2), (1, 3), (1, 6), (1, 7),
            (2, 3), (2, 4), (2, 6),
            (3, 4),
            (4, 5), (4, 7),
            (5, 6), (5, 7),
            (6, 7)]

# grafo 3
arestas3 = [(1, 2), (1, 3), (1, 6), (1, 7),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 6), (5, 7),
            (6, 7)]

# grafo 4
arestas4 = [(1, 2), (1, 3), (1, 6), (1, 7),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 6),
            (6, 7)]

# Verifica se o grafo é euleriano, semi-euleriano ou não euleriano
tipo_grafo, vertices_impares = verifica_grafo(vertices, arestas4)
print(f"O grafo é {tipo_grafo}")

# Chamada da função para encontrar o caminho Euleriano
if "euleriano" in tipo_grafo:
    caminho_euleriano = encontrar_caminho_euleriano(arestas2, vertices_impares)
    print("Ciclo Euleriano:", caminho_euleriano)
    pesos_arestas = gerar_pesos(arestas2)
    print("Pesos das arestas:", pesos_arestas)
    peso_do_caminho = calcular(caminho_euleriano, pesos_arestas)
    print("Peso do ciclo Euleriano:", peso_do_caminho)

if "semi-euleriano" in tipo_grafo:
    caminho_euleriano = encontrar_caminho_euleriano(arestas4, vertices_impares)
    print("Caminho Euleriano:", caminho_euleriano)
    pesos_arestas = gerar_pesos(arestas4)
    print("Pesos das arestas:", pesos_arestas)
    peso_do_caminho = calcular(caminho_euleriano, pesos_arestas)
    print("Peso do caminho Euleriano:", peso_do_caminho)
