def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i,elem in enumerate(a):
        if elem > b[i]:
            alice += 1
        elif elem < b[i]:
            bob += 1
        elif elem == b[i]:
            pass
    return '{}{}'.format(alice,bob)