
def maximumOddBinaryNumber(s: str) -> str:
    arr = [ch for ch in s]

    left = 0
    right = 0

    while right < len(arr):
        if arr[right] == '1':
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
        right += 1
    arr[left-1], arr[right-1] = arr[right-1], arr[left-1]

    return ''.join(arr)