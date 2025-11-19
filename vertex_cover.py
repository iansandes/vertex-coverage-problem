vertices = [1, 2, 3, 4]
edges = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)]

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

cover = greedy_vertex_cover(vertices, edges)
print("Greedy cover:", cover)
print("Size:", len(cover))
