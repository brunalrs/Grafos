# Percorre o grafo, lido a partir de um arquivo txt, utilizando busca em
# profundidade (DFS) e implementando as abordagens de recursão e pilha. O vértice 
# inicial é dado pelo usuário. O algoritmo produz a árvore de profundidade.

from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt


def dfs_recursiva(grafo: list, vertice: int, visitados: set = None) -> list:
    if visitados is None:
        visitados = set()
    #vertice atual = u // vizinho = v
    visitados.add(vertice) #marcar o vertice
    arvore = [] #cria caminho
    for aresta in grafo:  #"para cada aresta (u,v)"
        if vertice in aresta:     # se u estiver na aresta
            vizinho = aresta[0] if aresta[1] == vertice else aresta[1]  # encontrar v
            if vizinho not in visitados: #se vizinho n estiver marcado
                arvore.append((vertice, vizinho)) #add na arvore
                arvore.extend(dfs_recursiva(grafo, vizinho, visitados)) #chamadas recursivas
    return arvore


def dfs_pilha(grafo: list, vertice_inicial: int) -> list:
    visitados = set()
    pilha = [(vertice_inicial, None)]  # Incluímos o pai de cada vértice na pilha para rastrear as arestas
    pilha2 = [vertice_inicial]
    arvore = []

    while pilha:
        vertice, pai = pilha.pop()
        pilha2.pop()
        if vertice not in visitados:
            visitados.add(vertice)
            if pai is not None:
                arvore.append((pai, vertice))  # Adicionamos a aresta à árvore
            for aresta in grafo:  #"para cada aresta (u,v)"
                
                if vertice in aresta: 
                    vizinho = aresta[0] if aresta[1] == vertice else aresta[1] # encontrar v
                    if vizinho not in visitados:  
                        pilha.append((vizinho, vertice))  # Adicionamos o vértice e seu pai à pilha
                        pilha2.append(vizinho)
                        print(pilha)
    return arvore


def ler_grafo_de_arquivo(arquivo):
    grafo = []
    with open(arquivo, 'r') as f:
        for linha in f:
            elementos = linha.strip().split()
            if len(elementos) == 2:
                aresta = tuple(map(int, elementos))
                grafo.append(aresta)
    return grafo


arquivo_grafo = "Trabalho 05/arquivo.txt"

dados_grafo = ler_grafo_de_arquivo(arquivo_grafo)

resultado_dfs_recursiva = dfs_recursiva(dados_grafo,int(input("vertice inicial para recursivo:")) )
resultado_dfs_pilha = dfs_pilha(dados_grafo,int(input("vertice inicial para pilha:")) )


plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
T_recursive = nx.Graph(resultado_dfs_recursiva)
nx.draw(T_recursive, with_labels=True, node_color='skyblue', font_size=12, font_weight='bold')
plt.title("Árvore DFS Recursiva")

plt.subplot(1, 2, 2)
T_pilha = nx.Graph(resultado_dfs_pilha)
nx.draw(T_pilha, with_labels=True, node_color='lightgreen', font_size=12, font_weight='bold')
plt.title("Árvore DFS Iterativa")


plt.tight_layout()
plt.show()
