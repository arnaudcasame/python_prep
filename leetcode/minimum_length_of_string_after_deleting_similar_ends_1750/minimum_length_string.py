
def minimumLength(s: str) -> int:
    left, right = 0, len(s)-1

    while left < right:
        if s[left] == s[right] and left != right:
            letter = s[left]

            while s[left] == letter and left < right:
                    left += 1
            while s[right] == letter and left < right:
                    right -= 1

            print(s, left, right)
            s = s[left+1:] if left == right else s[left:]
            s = s[:right+1-left]
            print(s, left, right)
            left = 0
            right = len(s)-1
        else:
            break
    return len(s)