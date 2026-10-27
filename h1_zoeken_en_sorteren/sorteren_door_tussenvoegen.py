# omzetten psuedocode Algoritme 1.5 Sorteren door tussenvoegen
# pagina 21 in cursus


def cardsort(a):
  n = len(a)

  for i in range(1, n - 1):
    x = a[i]
    j = i
    while j > 0 and x < a[j - 1]:
      a[j] = a[j - 1]
      j = j - 1
    a[j] = x
    print(a)
  return a


if __name__ == "__main__":
    a = [int(_) for _ in input().split()]
    cardsort(a)