def gsp(dictionary, val, curr, destEle, time):
    if curr[0]:
        return
    curr[0] = True
    if val == destEle:
        curr[0] = False
        return True
    flag = False
    for key, value in curr[1].items():
        if gsp(dictionary, key, dictionary[key], destEle, time + value):
            flag = True
    curr[0] = False
    return flag


if __name__ == "__main__":
    totalMembers, nodes = int(input().strip()), {}

    for _ in range(totalMembers):
        nodes[int(input().strip())] = [False, {}]
    e = int(input().strip())

    for _ in range(e):
        follower, following, t = [int(a) for a in input().strip().split()]
        nodes[follower][1][following] = t

    source = int(input().strip())
    destination = int(input().strip())
    friends = [source]

    for k, v in nodes[source][1].items():
        if gsp(nodes, k, nodes[k], destination, v):
            friends.append(k)

    friends = sorted(friends)
    for frds in friends:
        if frds != destination:
            print(frds, end=" ")
