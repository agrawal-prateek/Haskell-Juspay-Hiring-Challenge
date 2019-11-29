def gsp(dictionary, val, curr, destEle, prev, arr):
    if curr[0]:
        return
    curr[0] = True
    if val == destEle:
        arr.append(prev)
        curr[0] = False
    for key in curr[1]:
        gsp(dictionary, key, dictionary[key], destEle, val, arr)
    curr[0] = False


if __name__ == "__main__":
    totalMembers, nodes = int(input().strip()), {}
    for _ in range(totalMembers):
        mem = int(input().strip())
        nodes[mem] = [False, []]
    e = int(input().strip())

    for _ in range(e):
        follower, following = [int(a) for a in input().strip().split()]
        nodes[follower][1].append(following)

    source = int(input().strip())
    destination = int(input().strip())
    arr = []
    for k in nodes[source][1]:
        gsp(nodes, k, nodes[k], destination, source, arr)
    print(*arr)