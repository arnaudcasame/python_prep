
def rangeBitwiseAnd(left: int, right: int) -> int:
    rightShiftCount = 0

    while left < right:
        left >>= 1
        right >>= 1
        rightShiftCount += 1

    return left << rightShiftCount