

def pivotInteger(n: int) -> int:
    table = [i for i in range(1, n+1)]
    # print(table)
    toTheRight = []
    for i in range(0, n):
        if i == 0:
            toTheRight.append(table[i])
        elif i < n:
            toTheRight.append(table[i] + toTheRight[i-1])
    # print(toTheRight)
    toTheLeft = [0]*n
    for i in range(n-1, -1, -1):
        if i == n-1:
            toTheLeft[i] += table[i]
        elif i >= 0:
            toTheLeft[i] += table[i] + toTheLeft[i+1]
    # print(toTheLeft)
    for i in range(len(toTheRight)):
        if toTheRight[i] == toTheLeft[i]:
            return table[i];
    return -1

def pivotIntegerOptimized(n: int) -> int:
    return 0
