#Uses python3
import sys
import math
import heapq

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
    print("coords: ", coords)
    # print("{0:.9f}".format(minimum_distance(x, y)))
