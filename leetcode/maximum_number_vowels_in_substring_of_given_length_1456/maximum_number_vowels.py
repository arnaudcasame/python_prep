

def maxVowels(s: str, k: int) -> int:
    count = 0
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    num = 0
    for i in range(k):
        if s[i] in vowels:
            num += 1
            count = max(count, num)
        # if i == k-1:
        #     print(s[i], count)

    i, j = 1, k
    while j < len(s):
        # if j == k:
        #     print(s[j], count)
        if s[j] in vowels:
            num += 1
        if s[i-1] in vowels:
            num -= 1
        count = max(count, num)
        i += 1
        j += 1
    return count

def maxVowelsBruteForce(s: str, k: int) -> int:
    count = 0
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    for i in range(len(s)):
        j = i
        num = 0
        while j < i+k and (i+k) <= len(s):
            if s[j] in vowels:
                num += 1
            j += 1
        count = max(count, num)
    print(count)
    return count