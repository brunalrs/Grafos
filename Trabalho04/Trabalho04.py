# Leitura um grafo a partir de um arquivo. O projeto percorre o grafo utilizando 
# busca em largura (BFS). O vértice inicial é dado pelo usuário e o algoritmo produz
# a distância de cada vértice ao nó raiz bem como o caminho.Por fim, é gerado um arquivo 
# com a árvore gerada.

from math import inf
import igraph as ig
from collections import deque

def criar_vertices(num_vertices):
    vertices = []
    for i in range(int(num_vertices)):
        vertices.append(i)
    return vertices

def ler_dados(arquivo):
    dados = []
    with open(arquivo, 'r') as arquivo:
        for linha in arquivo:
            elemento = linha.strip().split()
            dados.append(elemento)
    return dados

def gerar_arvore(grafo, vertice_inicial):
    # print(grafo)
    estado_vertice = {vertice: "não visitado" for vertice in range(len(grafo))}
    print(estado_vertice)
    profundidade_vertice = [inf] * len(grafo)
   
    queue = deque()
    
    vertice_inicial = int(vertice_inicial) - 1
    queue.append(vertice_inicial)
    profundidade_vertice[vertice_inicial] = 0

    arvore_bfs = []
    grafo_aux = grafo
    
    # grafo_aux.deepcopy(grafo) = grafo

    while queue:
        vertice_atual = queue.popleft()
        vizinhos = [i for i, arestas in enumerate(grafo_aux[vertice_atual]) if arestas == 1]
        print(vizinhos)
        for vizinho in vizinhos:
            if estado_vertice[vizinho] == "não visitado":
                estado_vertice[vizinho] = "descoberto"
                queue.append(vizinho)
                # print(grafo_aux)
                grafo_aux[vertice_atual][vizinho] = 0 #linha-coluna
                
                grafo_aux[vizinho][vertice_atual] = 0 #coluna-linha

                profundidade_vertice[vizinho] = profundidade_vertice[vertice_atual] + 1
                arvore_bfs.append((vertice_atual, vizinho))
        print(arvore_bfs)        
        estado_vertice[vertice_atual] = "visitado"
    return arvore_bfs, profundidade_vertice

def desenha_arvore(arvore, profundidade, raiz):
    g = ig.Graph(directed=True)
    g.add_vertices(len(profundidade))

    # Adiciona rótulos aos vértices com a distância à origem
    labels = [f'{i+1}\n({profundidade[i]})' for i in range(len(profundidade))]
    g.vs["label"] = labels

    g.add_edges(arvore)

    layout = g.layout_reingold_tilford(root=[int(raiz) - 1])

    plot = ig.plot(g, layout=layout, vertex_size=30, vertex_color="lightblue",
                   vertex_label_size=14, vertex_label_color="black", vertex_label_font="Arial",
                   edge_color="brown", edge_arrow_size=1)
    plot.save(f"Raiz-{raiz}.png")



def menor_caminho(arvore, raiz, destino):
    raiz = int(raiz) - 1
    destino = int(destino) - 1
    caminhos = {raiz: [raiz]}

    visitados = {raiz}
    queue = deque([raiz])

    while queue:
        print(queue)
        vertice_atual = queue.popleft()
        for parente, filho in arvore:
            if parente == vertice_atual and filho not in visitados:
                caminhos[filho] = caminhos[parente] + [filho]
                visitados.add(filho)
                queue.append(filho)
    caminho = caminhos.get(destino, None)
    if caminho:
        str_caminho = " -> ".join(str(vertice + 1) for vertice in caminho)
    else:
        str_caminho = None
    return str_caminho

if __name__ == '__main__':
    grafo_input = ler_dados("arquivo.txt")
    num_vertices = int(grafo_input.pop(0)[0])

    arestas = [[int(valor) for valor in sublista] for sublista in grafo_input]

    vertices = criar_vertices(num_vertices)
    grafo = [[0] * num_vertices for _ in range(num_vertices)]
    for aresta in arestas:
        grafo[aresta[0] - 1][aresta[1] - 1] = 1
        grafo[aresta[1] - 1][aresta[0] - 1] = 1

    vertice_inicial = input("Digite o vértice inicial: ")
    arvore_bfs, profundidade = gerar_arvore(grafo, vertice_inicial)
    desenha_arvore(arvore_bfs, profundidade, raiz=vertice_inicial)

    destino = input("Digite o vértice final: ")
    menor_caminho = menor_caminho(arvore_bfs, raiz=vertice_inicial, destino=destino)

    if menor_caminho:
        print(f"O menor caminho do {vertice_inicial} para {destino} é {menor_caminho}")
    else:
        print(f"Nenhum caminho encontrado do vértice {vertice_inicial} para o {destino}")
