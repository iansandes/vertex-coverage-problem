def count_incidence(uncovered):
    counts = {}
    for u, v in uncovered:
        counts[u] = counts.get(u, 0) + 1
        counts[v] = counts.get(v, 0) + 1
    return counts

def choose_vertex(counts):
    best, q = None, -1
    for v in counts:
        if counts[v] > q:
            best, q = v, counts[v]
    return best

def remove_edges(uncovered, v):
    new_list = []
    for u, w in uncovered:
        if u != v and w != v:
            new_list.append((u, w))
    return new_list

def greedy_vertex_cover(vertices, edges):
    uncovered = edges[:]
    cover = []
    while uncovered:
        counts = count_incidence(uncovered)
        v = choose_vertex(counts)
        cover.append(v)
        uncovered = remove_edges(uncovered, v)
    return cover


#### INSTÂNCIA CAMINHO SIMPLES ####
print("===================")
print("CAMINHO SIMPLES")


vertices = [1, 2, 3, 4]
edges = [(1, 2), (2, 3), (3, 4)]

cover = greedy_vertex_cover(vertices, edges)
print("Greedy cover:", cover)
print("Size:", len(cover))

#### INSTÂNCIA CAMINHO COM DIAGONAL ####
print("===================")
print("CAMINHO COM DIAGONAL")

vertices = [1, 2, 3, 4]
edges = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)]

cover = greedy_vertex_cover(vertices, edges)
print("Greedy cover:", cover)
print("Size:", len(cover))


#### INSTÂNCIA GRADE 3X3 ####


print("===================")
print("GRADE 3x3")


vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
edges = [(1, 2), (2, 3), (4, 5), (5, 6), (7, 8), (8, 9), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8), (6, 9)]


cover = greedy_vertex_cover(vertices, edges)
print("Greedy cover:", cover)
print("Size:", len(cover))