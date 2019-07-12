#Uses python3
import sys
import math
import heapq


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
            if opp_neighbour in graph[pt1]:
                continue
            else:
                graph[key].append(neighbour)


def minimum_distance(x, y):
    result = 0.
    #write your code here
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

    # print("{0:.9f}".format(minimum_distance(x, y)))
