import matplotlib.pyplot as plt
# Função para imprimir a matriz de adjacência com nomes alinhados
def imprime_matriz_adjacencia(fronteiras, estados):
    # calcula quantos estados tem na lista
    n = len(estados)

    # matriz preenchida com zeros, com n+1 linhas e colunas.
    matriz_adjacencia = [[0] * (n + 1) for _ in range(n + 1)]

    matriz_adjacencia[0][0] = ''

    # preenchendo matriz com estados
    for i, estado in enumerate(estados, start=1):
        # Coloca o nome dos estados nas linahs e colunas da matriz
        matriz_adjacencia[i][0] = estado
        matriz_adjacencia[0][i] = estado

    # colocando as fronteiras na matriz
    for u, v in fronteiras:
        # Obtém os índices dos estados u e v na lista estados.
        i, j = estados.index(u) + 1, estados.index(v) + 1
        # colocando fronteira
        matriz_adjacencia[i][j] = 1
        matriz_adjacencia[j][i] = 1

    # Determinando o comprimento máximo de cada nome de estado
    comprimento_maximo = max(len(estado) for estado in estados)

    print("Matriz de Adjacência:")
    for linha in matriz_adjacencia:
        print(" ".join(f"{celula:<{comprimento_maximo}}" for celula in linha))


# Função para imprimir a matriz de incidência com nomes alinhados
def imprime_matriz_incidencia(fronteiras, estados):
    n_arestas = len(fronteiras)
    n_estados = len(estados)

    # Criando uma matriz de incidência preenchida com zeros
    matriz_incidencia = [[0] * (n_estados + 1) for _ in range(n_arestas)]

    # Colocando nomes das arestas na matriz
    for i, (u, v) in enumerate(fronteiras, start=1):
        matriz_incidencia[i - 1][0] = f"{u}-{v}"

    # Colocando as conexões na matriz
    for i, (u, v) in enumerate(fronteiras):
        j = estados.index(u) + 1
        k = estados.index(v) + 1
        matriz_incidencia[i][j] = 1
        matriz_incidencia[i][k] = 1

    # Determinando o comprimento máximo de cada nome de aresta
    comprimento_maximo = max(len(f"{u}-{v}") for u, v in fronteiras)

    print("\nMatriz de Incidência:")
    estados_centralizados = [estado.center(comprimento_maximo) for estado in estados]
    print(" " * (comprimento_maximo - 1) + " ".join(estados_centralizados))

    # Imprimir a matriz de incidência
    for linha in matriz_incidencia:
        print(" ".join(f"{celula:<{comprimento_maximo}}" for celula in linha))

# ---- Lista indexada ----
        
def alfa(arestas):
    alfa = [0]
    # Verifica se o primeiro elemento da aresta atual é diferente do primeiro elemento da aresta anterior
    for i in range(1, len(arestas)):
        if arestas[i][0] != arestas[i - 1][0]:
            alfa.append(i)
    return alfa

def beta(arestas):
    # lista de tuplas com os estados das arestas
    fronteiras_nomeadas = [(estados[i], estados[j]) for i, j in arestas]
    # Retorna uma lista com os estados do segundo elemento de cada tupla
    return [estado for _, estado in fronteiras_nomeadas]

def vizinhos(indice_alfa, alfa, beta):
    # Verifica se o índice alfa está dentro dos limites da lista alfa
    if 0 <= indice_alfa < len(alfa) - 1:
        # Retorna os vizinhos do estado correspondente ao índice alfa
        return beta[alfa[indice_alfa]:alfa[indice_alfa + 1]]
    # Verifica se o índice alfa é o último elemento da lista alfa
    elif indice_alfa == len(alfa) + 1:
        # retorna os vizinhos do ultimo elemento
        return beta[alfa[indice_alfa]:len(beta)]




def lista_indexada(alfa, beta):
    lista_indexada = {}
    for i in range(len(alfa) - 1):
        vertice = estados[i]
        vizinhos_lista = vizinhos(i, alfa, beta)
        lista_indexada[vertice] = vizinhos_lista
    return lista_indexada

def printar_lista():
    alfas = alfa(fronteiras_numeradas)
    betas = beta(fronteiras_numeradas)
    lista = lista_indexada(alfas, betas)
    # Itera sobre os itens do dicionário]
    print("\nLista Indexada:")
    for vertice, vizinhos in lista.items():
        print(f"{vertice}: {', '.join(map(str, vizinhos))}")
                        
def grau_max_min(grafo):
    # Calcula os graus de cada estado no grafo
    graus = {estado: len(set(vizinhos)) for estado, vizinhos in grafo.items()}
    max_grau = max(graus.values())
    min_grau = min(graus.values())
    estados_max_grau = [estado for estado, grau in graus.items() if grau == max_grau]
    estados_min_grau = [estado for estado, grau in graus.items() if grau == min_grau]

    vizinhos_max_grau = {estado: grafo[estado] for estado in estados_max_grau}
    vizinhos_min_grau = {estado: grafo[estado] for estado in estados_min_grau}

    print(f"\nGrau máximo: {max_grau}, Estados com grau máximo: {estados_max_grau}")
    print("Vizinhos dos estados com grau máximo:")
    for estado, vizinhos in vizinhos_max_grau.items():
        print(f"{estado}: {set(vizinhos)}")

    print(f"\nGrau mínimo: {min_grau}, Estados com grau mínimo: {estados_min_grau}")
    print("Vizinhos dos estados com grau mínimo:")
    for estado, vizinhos in vizinhos_min_grau.items():
        print(f"{estado}: {set(vizinhos)}")


def frequencia_graus(grafo):
    #calcula os graus de cada estado
    graus = {estado: len(set(vizinhos)) for estado, vizinhos in grafo.items()}
    frequencia = {}
    # Itera sobre os graus dos estados
    for grau in graus.values():
        # Verifica se o grau já está no dicionário de frequência
        if grau in frequencia:
            frequencia[grau] += 1
        else:
            frequencia[grau] = 1
    print("Frequência dos graus dos vértices:")
    for grau, freq in frequencia.items():
        print(f"Grau {grau}: {freq} vértices")
    return frequencia

def histograma_freq(frequencia):
    # Criar o histograma da frequência dos graus
    plt.bar(frequencia.keys(), frequencia.values(), color='skyblue')
    plt.xlabel('Grau')
    plt.ylabel('Frequência')
    plt.title('Histograma da Frequência dos Graus')
    plt.show()


estados = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PE', 'PI',
           'PR', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

fronteiras = [("AC", "AM"), ("AC", "RO"), ("MA", "BA"), ("AL", "BA"),
              ("AL", "SE"), ("AL", "PB"), ("AP", "PA"), ("AM", "PA"),
              ("AM", "RR"), ("AM", "MT"), ("BA", "SE"), ("BA", "PE"), ("BA", "PI"),
              ("BA", "TO"), ("BA", "GO"), ("CE", "PI"), ("CE", "RN"),
              ("CE", "PB"), ("CE", "PE"), ("DF", "GO"), ("DF", "MG"),
              ("DF", "GO"), ("ES", "MG"), ("ES", "RJ"), ("ES", "BA"),
              ("GO", "TO"), ("GO", "MT"), ("GO", "MS"), ("GO", "MG"),
              ("MA", "PA"), ("MA", "TO"), ("MA", "PI"), ("MT", "TO"),
              ("MT", "MS"), ("MS", "PR"), ("MS", "SP"),
              ("MS", "MG"), ("MS", "GO"), ("MG", "SP"), ("MG", "RJ"),
              ("MG", "BA"), ("MG", "ES"), ("MG", "GO"), ("MG", "DF"),
              ("PA", "RR"), ("PA", "AP"), ("PA", "TO"), ("PA", "MA"),
              ("PA", "MT"), ("PB", "RN"), ("PB", "PE"), ("PB", "PE"),
              ("PE", "PI"), ("PE", "PI"), ("PI", "TO"),
              ("PI", "BA"), ("PI", "MA"), ("PR", "SP"), ("PR", "SC"),
              ("RJ", "SP"), ("RJ", "ES"), ("RN", "CE"), ("RN", "PB"),
              ("RO", "AM"), ("RO", "MT"), ("RR", "AM"), ("RR", "PA"),
              ("RS", "SC"), ("RS", "SC"), ("RS", "SC"), ("SC", "PR"),
              ("SC", "RS"), ("SC", "PR"), ("SE", "BA"),
              ("SP", "MG"), ("SP", "RJ"), ("SP", "MS"), ("SP", "PR"),
              ("TO", "MA"), ("TO", "PA")]

fronteiras_numeradas = [
    (0, 2), (0, 21),
    (1, 4), (1, 15), (1, 25),
    (2, 0), (2, 10), (2, 13), (2, 21), (2, 22),
    (3, 13),
    (4, 1), (4, 7), (4, 8), (4, 9), (4, 12), (4, 15), (4, 16), (4, 25), (4, 26),
    (5, 14), (5, 15), (5, 16), (5, 19),
    (6, 8), (6, 12),
    (7, 4), (7, 12), (7, 18),
    (8, 4), (8, 6), (8, 10), (8, 11), (8, 12), (8, 26),
    (9, 4), (9, 13), (9, 16), (9, 26),
    (10, 2), (10, 8), (10, 11), (10, 13), (10, 21), (10, 26),
    (11, 8), (11, 10), (11, 12), (11, 17), (11, 24),
    (12, 4), (12, 6), (12, 7), (12, 8), (12, 11), (12, 18), (12, 24),
    (13, 2), (13, 3), (13, 9), (13, 10), (13, 22), (13, 26),
    (14, 5), (14, 15), (14, 19),
    (15, 1), (15, 4), (15, 5), (15, 14), (15, 16),
    (16, 4), (16, 5), (16, 9), (16, 15), (16, 26),
    (17, 11), (17, 23), (17, 24),
    (18, 7), (18, 12), (18, 24),
    (19, 5), (19, 14),
    (20, 23),
    (21, 0), (21, 2), (21, 10),
    (22, 2), (22, 13),
    (23, 17), (23, 20),
    (24, 11), (24, 12), (24, 17), (24, 18),
    (25, 1), (25, 4),
    (26, 4), (26, 8), (26, 9), (26, 10), (26, 13), (26, 16)
]

arestas = [(0, 2),  # AC - AM
               (0, 21),  # AC - RO
               (1, 15),  # AL - PE
               (1, 4),  # AL - BA
               (1, 25),  # AL - SE
               (2, 22),  # AM - RR
               (2, 21),  # AM - RO
               (2, 13),  # AM - PA
               (2, 10),  # AM - MT
               (3, 13),  # AP - PA
               (4, 7),  # BA - ES
               (4, 8),  # BA - GO
               (4, 9),  # BA - MA
               (4, 12),  # BA - MG
               (4, 15),  # BA - PE
               (4, 16),  # BA - PI
               (4, 25),  # BA - SE
               (4, 26),  # BA - TO
               (5, 16),  # CE - PI
               (5, 19),  # CE - RN
               (5, 14),  # CE - PB
               (5, 15),  # CE - PE
               (6, 8),  # DF - GO
               (6, 12),  # DF - MG
               (7, 12),  # ES - MG
               (7, 18),  # ES - RJ
               (8, 10),  # GO - MT
               (8, 11),  # GO - MS
               (8, 12),  # GO - MG
               (8, 26),  # GO - TO
               (9, 13),  # MA - PA
               (9, 16),  # MA - PI
               (9, 26),  # MA - TO
               (10, 11),  # MT - MS
               (10, 13),  # MT - PA
               (10, 21),  # MT - RO
               (10, 26),  # MT - TO
               (11, 12),  # MS - MG
               (11, 17),  # MS - PR
               (11, 24),  # MS - SP
               (12, 18),  # MG - RJ
               (12, 24),  # MG - SP
               (13, 26),  # PA - TO
               (13, 22),  # PA - RR
               (14, 19),  # PB - RN
               (14, 15),  # PB - PE
               (15, 16),  # PE - PI
               (16, 26),  # PI - TO
               (17, 23),  # PR - SC
               (17, 24),  # PR - SP
               (18, 24),  # RJ - SP
               (20, 23),  # RS - SC
               ]

imprime_matriz_adjacencia(fronteiras, estados)
imprime_matriz_incidencia(fronteiras, estados)

printar_lista()

grafo = lista_indexada(alfa(fronteiras_numeradas), beta(fronteiras_numeradas))
grau_max_min(grafo)
frequencia = frequencia_graus(grafo)
histograma_freq(frequencia)