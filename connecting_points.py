#Uses python3
import sys
import math
import heapq


INFINITY = 9999.999999999


def distance(p, q):
    """Return euclidean distance btween two points. """
    dist = ((p[0] - q[0])**2 + (p[1] - q[1])**2)
    return math.sqrt(dist)


def add_edge(graph, pt1):
    """Add point edges to trhe graph along with weights.

    weight distance is calculated by distance function since
    all keys in the graph are (x, y) points.
    """

    for key in graph:
        if key == pt1:
            continue
        else:
            edge_weight = distance(key, pt1)
            neighbour = [pt1, edge_weight]
            opp_neighbour = [key, edge_weight]
            graph[key].append(neighbour)


def minimum_distance(coords, graph):
    mst = [None for i in range(len(coords))]
    length = len(coords)
    result_vals = [None for i in range(len(coords))]
    pq = []
    dist = [[INFINITY, pt] for pt in coords]
    parent = [None for i in range(len(coords))]
    start = 0
    result = 0.
    dist[start][0] = 0
    parent[start] = start
    heapq.heappush(pq, dist[start])
    i = 1

    while pq:
        mst_dist, mst_vertex = heapq.heappop(pq)
        mst_ind = coords.index(mst_vertex)
        
        # put this value in our mst
        mst[mst_ind] = mst_vertex
        result_vals[mst_ind] = mst_dist
        
        for neighbor_vert, edge_weight in graph[mst_vertex]:
            neighbor_index = coords.index(neighbor_vert)
            if mst[neighbor_index] != neighbor_vert and dist[neighbor_index][0] > edge_weight:
                dist[neighbor_index][0] = edge_weight
                if dist[neighbor_index] not in pq:
                    parent[neighbor_index] = mst_ind
                    heapq.heappush(pq, dist[neighbor_index])
        if mst_vertex in mst and i <= length:
            result += mst_dist
        i = i + 1
    return result


if __name__ == '__main__':
    is_file_input = False
    if len(sys.argv) > 1:
        is_file_input = True
        f = open(sys.argv[1])
        n = int(f.readline())
    else:
        n = int(input())
    coords = [None for i in range(n)]                   # create empty list that will hold coordinate points

    # populate coords with x, y points read in
    for i in range(n):
        if is_file_input:
            x, y = map(int, f.readline().split())
        else:
            x, y = map(int, sys.stdin.readline().split())
        coords[i] = (x, y)
    if is_file_input:
        f.close()
    graph = {pt: [] for pt in coords}
    for my_pt in coords:
        add_edge(graph, my_pt)

    print("{0:.9f}".format(minimum_distance(coords, graph)))
