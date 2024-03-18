

def maxVowels(s: str, k: int) -> int:
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