import sys

mt = sys.maxsize


def calculateMinTime(nodes, nodeValue, node, B, currTime):
    global mt
    if node[0]:
        return
    node[0] = True
    if nodeValue == B:
        mt = min(mt, currTime)
        node[0] = False
        return
    for key, value in node[1].items():
        calculateMinTime(nodes, key, nodes[key], B, currTime + value)
    node[0] = False


if __name__ == "__main__":
    totalMembers, nodes = int(input().strip()), {}
    for _ in range(totalMembers):
        nodes[int(input().strip())] = [False, {}]

    edges = int(input().strip())
    for _ in range(edges):
        follower, following, t = [int(a) for a in input().strip().split()]
        nodes[follower][1][following] = t

    source = int(input().strip())
    dest = int(input().strip())
    calculateMinTime(nodes, source, nodes[source], dest, 0)
    print(mt)
