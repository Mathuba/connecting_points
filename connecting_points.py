#Uses python3
import sys
import math
import heapq



class priority_queue():
    def __init__(self):
        self.queue = list()
        heapq.heapify(self.queue)
        self.index = dict()

    def push(self, priority, label):
        if label in self.index:
            self.queue = [(w, l) for w, l in self.queue if l !=label]
            heapq.heapify(self.queue)
        heapq.heappush(self.queue, (priority, label))
        self.index[label] = priority

    def pop(self):
        if self.queue:
            return heapq.heappop(self.queue)

    def __contains__(self, label):
        return label in self.index

    def __len__(self):
        return len(self.queue)


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
    """Return the total weights of minimum soan tree using prim's algorithm.

    Parameters
    ----------
    coords - list
        List of tuples (x, y) which are poinys for each vertex

    graph - dict
        dictionary that stores unweighted graph of all points
    """

    span_tree = {}
    pq = priority_queue()
    result = 0
    start = 0
    source_vert = coords[start]
    pq.push(0, (source_vert, source_vert))

    while pq:
        edge_weight, (start_node, end_node) = pq.pop()
        if end_node not in span_tree:
            span_tree[end_node] = start_node
            if edge_weight:
                result += edge_weight
            for neighbor_node, neighbor_weight in graph[end_node]:
                pq.push(neighbor_weight, (end_node, neighbor_node))
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
    