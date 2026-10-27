def selection_sort_achteraan(a):
    n = len(a)
    for i in range(n - 1, 0, -1):         # i = n-1 ... 1
        positie = i                       # i, niet 1
        maximum = a[i]
        for j in range(i - 1, -1, -1):    # j = i-1 ... 0  (tot -1, zodat 0 meedoet)
            if a[j] > maximum:
                positie = j
                maximum = a[j]
        a[positie] = a[i]
        a[i] = maximum
        print(a)                          # toon de rij na elke ronde
    return a


if __name__ == "__main__":
    a = [int(_) for _ in input().split()]
    selection_sort_achteraan(a)