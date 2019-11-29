class Member:
    def __init__(self, value):
        self.value = value
        self.friends = []

    def setFriend(self, friend):
        self.friends.append(friend)


if __name__ == "__main__":
    totalMembers, d = int(input().strip()), dict()
    for _ in range(totalMembers):
        data = int(input().strip())
        d[data] = Member(data)

    edges = int(input().strip())
    for _ in range(edges):
        follower, following = [int(a) for a in input().strip().split()]
        d[follower].setFriend(d[following])

    source = int(input().strip())
    dest = int(input().strip())

    q = [d[source]]
    while len(q) > 0:
        node = q[0]
        if node.value == dest:
            print(1)
            exit(0)
        del q[0]
        q = [*q, *node.friends]
    print(0)
