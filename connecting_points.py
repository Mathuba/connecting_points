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
            # if opp_neighbour in graph[pt1]:
            #     continue
            # else:
            #     graph[key].append(neighbour)
            graph[key].append(neighbour)


def minimum_distance(coords, graph):
    pq = []
    mst = []
    dist = [[INFINITY, pt] for pt in coords]
    parent =[None for i in range(len(coords))]
    start = 0
    result = 0.

    dist[start][0] = 0
    parent[start] = coords[start]
    heapq.heappush(pq, dist[start])

    while pq:
        u_dist, u_pt = heapq.heappop(pq)
        u_ind = coords.index(u_pt)
        if parent[u_ind] != coords[u_ind]:
            mst.append(coords[u_ind])
            
        for neighbour_pt, edge_weight in graph[u_pt]:
            dist_standard = [edge_weight, neighbour_pt]
            neighbour_ind = coords.index(neighbour_pt)

            print("This is what is in pq: ", pq)
            print("dist_standard: ", dist_standard)
            print("In mst: ", mst)
            print("dist_standard in pq: ", dist_standard in pq)
            print()
            print("----------------------------------------------------")
            if dist_standard in pq and dist[neighbour_ind][0] > edge_weight:
                remove_dist = dist[neighbour_ind]
                dist[neighbour_ind][0] = edge_weight
                parent[neighbour_ind] = coords[u_ind]
                pq.remove(remove_dist)
                heapq.heapify(pq)
                heapq.heappush(pq, dist[neighbour_ind])
            elif parent[neighbour_ind] is None:
                dist[neighbour_ind][0] = edge_weight
                parent[neighbour_ind] = coords[u_ind]
                heapq.heappush(pq, dist[neighbour_ind])
                
    return mst


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

    # print("{0:.9f}".format(minimum_distance(coords, graph)))
    print((minimum_distance(coords, graph)))
