# d - количество символов во входном алфавите

d = 256


# pat -> pattern
# txt -> text
# q -> Простое число


def search(pat, txt, q):
    M = len(pat)

    N = len(txt)

    i = 0

    j = 0

    p = 0  # хэш-значение для шаблона

    t = 0  # хэш-значение для txt

    h = 1

    # Значение h будет равно "pow (d, M-1)% q"

    for i in range(M - 1):
        h = (h * d) % q



    # Рассчитать значение хеша шаблона и первого окна


    for i in range(M):
        p = (d * p + ord(pat[i])) % q

        t = (d * t + ord(txt[i])) % q

    # Переместите шаблон поверх текста один за другим

    for i in range(N - M + 1):

        # Проверьте значения хеш-функции текущего окна текста и

        # шаблон, если значения хеша совпадают, тогда проверять только

        # для персонажей по одному

        if p == t:

            # Проверяйте персонажей по одному

            for j in range(M):

                if txt[i + j] != pat[j]:
                    break

            j += 1

            # если p == t и pat [0 ... M-1] = txt [i, i + 1, ... i + M-1]

            if j == M:
                print("Pattern found at index " + str(i))

        # Рассчитать значение хеша для следующего окна текста: Удалить

        # начальная цифра, добавьте завершающую цифру

        if i < N - M:

            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q

            # Мы можем получить отрицательные значения t, преобразовав его в

            # положительный

            if t < 0:
                t = t + q


#txt = "GEEKS FOR GEEKS"
txt = "mama milk king milk haha "

#pat = "GEEK"
pat = "milk"

q = 101  # Простое число

search(pat, txt, q)
