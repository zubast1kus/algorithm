def simple_search(string, substring):
    len_string = len(string)
    len_substring = len(substring)
    for i in range(len_string):
        j = 0
        while j < len_substring:
            if substring[j] != string[i+j]:
                break
            j += 1
        if j == len_substring:
            return i
    return -1


def find_all(string, substring):
    arr=[]
    len_string = len(string)
    len_substring = len(substring)
    for i in range(len_string):
        j = 0
        while j < len_substring:
            if substring[j] != string[i+j]:
                break
            j += 1
        if j == len_substring:
            arr.append(i)
    return arr

# def prefix(s):
#     v = [0]*len(s)
#     for i in range(1, len(s)):
#         k = v[i-1]
#         while k > 0 and s[k] != s[i]:
#             k = v[k-1]
#         if s[k] == s[i]:
#             k = k + 1
#         v[i] = k
#     return v
#
#
# def kmp(s,t):
#     arr=[]
#     index = -1
#     f = prefix(s)
#     k = 0
#     for i in range(len(t)):
#         while k > 0 and s[k] != t[i]:
#             k = f[k-1]
#         if s[k] == t[i]:
#             k = k + 1
#         if k == len(s):
#             index = i - len(s) + 1
#             break
#     return index


def KnuthMorrisPratt(text, pattern):
    pattern = list(pattern)

    shifts = [1] * (len(pattern) + 1)
    shift = 1
    for pos in range(len(pattern)):
        while shift <= pos and pattern[pos] != pattern[pos-shift]:
            shift += shifts[pos-shift]
        shifts[pos+1] = shift

    startPos = 0
    matchLen = 0
    for c in text:
        while matchLen == len(pattern) or \
              matchLen >= 0 and pattern[matchLen] != c:
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == len(pattern):
            yield startPos




def forming_d(pattern):
    """ Формируем массив d."""
    d = [len(pattern) for i in range(1105)]
    new_p = pattern[::-1]

    for i in range(len(new_p)):
        if d[ord(new_p[i])] != len(new_p):
            continue
        else:
            d[ord(new_p[i])] = i
    return d


def search(string, pattern):
    """ Поиск Бойера - Мура."""

    d = forming_d(pattern)
    # x - начало прохода по string
    # j - проход по pattern
    # k - проход по string
    len_p = x = j = k = len(pattern)
    # число смещений
    counter = 0

    while x <= len(string) and j > 0:
        if pattern[j - 1] == string[k - 1]:
            j -= 1
            k -= 1
        else:
            x += d[ord(string[k - 1])]
            k = x
            j = len_p
            counter += 1

    if j <= 0:
        return "Нашли. Число смещений равно %d." % counter
    else:
        return "Не нашли!"


# string = "mama milk king mil haha "
# pattern = "milk"
# print("")
# print(search(string, pattern))

#----------------------------------KNUT
print(KnuthMorrisPratt("mama milk king milk haha ", "milk"))
g = KnuthMorrisPratt("mama milk king milk haha ", "milk")
for i in g:
    print(i)

#
# print(find_all("mama milk king milk haha ", "milk"))