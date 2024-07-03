# Algoritmo de Bellman-Ford, computando os valores das distâncias.

from json import dumps

def bellmanFord(grafo, vertices, vertice_inicial):
    num_vertices = len(vertices)
    distancias = {vertice: float('inf') for vertice in vertices}
    predecessores = {vertice: None for vertice in vertices}
    distancias[vertice_inicial] = 0

    arestas = []
    for u in grafo:
        for v in grafo[u]:
            arestas.append((u, v, grafo[u][v]))

    for _ in range(num_vertices - 1):
        for u, v, peso in arestas:
            if distancias[u] != float('inf') and distancias[u] + peso < distancias[v]:
                distancias[v] = distancias[u] + peso
                predecessores[v] = u

    for _ in range(num_vertices - 1):
        for u, v, peso in arestas:
            if distancias[u] != float('inf') and distancias[u] + peso < distancias[v]:
                distancias[v] = float('-inf')
                predecessores[v] = u

    for _ in range(num_vertices - 1):
        for u, v, peso in arestas:
            if distancias[u] == float('-inf'):
                distancias[v] = float('-inf')
                predecessores[v] = u

    return distancias, predecessores

def reconstruir_caminho(predecessores, vertice):
    caminho = []
    while vertice is not None:
        caminho.append(vertice)
        vertice = predecessores[vertice]
    caminho.reverse()
    return caminho

if __name__ == '__main__':
    grafo = {}
    with open('grafo1.txt') as arquivo:
        for linha in arquivo:
            u, v, peso = linha.split()
            peso = int(peso)
            if u not in grafo:
                grafo[u] = {}
            grafo[u][v] = peso

    vertices = set(grafo.keys())
    for destinos in grafo.values():
        vertices.update(destinos.keys())
    vertices = list(vertices)

    vertice_inicial = 'S'

    distancias, predecessores = bellmanFord(grafo, vertices, vertice_inicial)
    print(f'Vertice inicial: {vertice_inicial}')
    print(dumps(distancias, indent=4))

    for vertice in vertices:
        if distancias[vertice] == float('inf'):
            print(f"Não há caminho do vértice inicial {vertice_inicial} para {vertice}.")
        elif distancias[vertice] == float('-inf'):
            print(f"O caminho para {vertice} é indefinido devido a um ciclo de peso negativo.")
        else:
            caminho = reconstruir_caminho(predecessores, vertice)
            print(f"Caminho do vértice inicial {vertice_inicial} para {vertice}: {' -> '.join(caminho)} com custo {distancias[vertice]}")
