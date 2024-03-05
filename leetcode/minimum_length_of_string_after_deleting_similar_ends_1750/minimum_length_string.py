
def minimumLength(s: str) -> int:
    left, right = 0, len(s)-1

    while left < right and s[left] == s[right]:
        letter = s[left]

        while left <= right and s[left] == letter:
            left += 1
        while left <= right and s[right] == letter:
            right -= 1
    return 0 if left > right else right - left + 1