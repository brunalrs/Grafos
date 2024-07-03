# Algoritmo de Dijkstra, computando os valores das distâncias.

def ler_grafo(arquivo):
    grafo = {}
    with open(arquivo, 'r') as f:
        for linha in f:
            origem, destino, custo = linha.strip().split()
            custo = int(custo)
            if origem not in grafo:
                grafo[origem] = {}
            if destino not in grafo:
                grafo[destino] = {}
            grafo[origem][destino] = custo
            # print(grafo)
    return grafo

def dijkstra(grafo, inicio):
    N = set()  # Conjunto de nós processados
    D = {no: float('inf') for no in grafo}  # Inicializa todas as distâncias como infinite
    D[inicio] = 0  # Distância do nó inicial é 0
    predecessores = {no: None for no in grafo}  # Inicializa todos os predecessores como none

    while len(N) < len(grafo):
        # Achar w não em N tal que D(w) é um mínimo
        w = None
        menor_distancia = float('inf')
        for no in D:
            print("n = ", N)
            print("no = ", no)
            print("D[no] = ", D[no])
            
            if no not in N and D[no] < menor_distancia:
                menor_distancia = D[no]
                w = no
                print("menor dist = ", menor_distancia)
                print("w = ", w)

        if w is None:
            break

        # Acrescentar w a N
        N.add(w)

        # Atualizar D(v) para todo v adjacente a w e não em N
        for v, custo in grafo[w].items():
            if v not in N:
                if v not in D:  # Adiciona o nó ao dicionário de distâncias se não estiver presente
                    D[v] = float('inf')
                    predecessores[v] = None
                nova_distancia = D[w] + custo
                if nova_distancia < D[v]:
                    D[v] = nova_distancia
                    predecessores[v] = w

    return D, predecessores

def reconstruir_caminho(predecessores, inicio, fim):
    caminho = []
    atual = fim
    while atual is not None:
        # print(atual)
        caminho.append(atual)
        atual = predecessores[atual]
    caminho.reverse()
    if caminho[0] == inicio:
        return caminho
    else:
        return []

# Exemplo de uso:
arquivo = 'grafo2.txt'
grafo = ler_grafo(arquivo)
no_inicio = 'E'
distancias, predecessores = dijkstra(grafo, no_inicio)

print("Distâncias:")
print(distancias)

print("\nCaminhos:")
for no in grafo:
    if no != no_inicio:
        caminho = reconstruir_caminho(predecessores, no_inicio, no)
        print(f"Caminho de {no_inicio} para {no}: {caminho}")
