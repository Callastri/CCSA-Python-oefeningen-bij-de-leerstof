# omzetten psuedocode Algoritme 1.6 sorteren door samenvoegen
# pagina 24 in cursus


def mergeSort(a):
  n = len(a)
  mergeSortRecursieve(a, 0, n - 1)
  return a

def mergeSortRecursieve(a, begin, einde):
  if begin < einde:
    midden  = (begin + einde) // 2
    mergeSortRecursieve(a, begin, midden)
    mergeSortRecursieve(a, midden + 1 , einde)

    merge(a, begin, midden, einde)
  return a

def merge(a, begin, midden, einde):
  i = begin
  j = midden +1
  k = i
  hulpa = [None] * len(a)             # een lijst met n lege plaatsen

  while i <= midden and j <= einde:
      if a[i] <= a[j]:
        hulpa[k] = a[i]
        i = i + 1
      else:
        hulpa[k] = a[j]
        j = j + 1
      
      k = k + 1
    

  if i > midden:
      while j <= einde:
        hulpa[k] = a[j]
        j = j +1
        k = k + 1
  else:
      while i <= midden:
        hulpa[k] = a[i]
        i = i + 1
        k = k + 1

  for k in range(begin, einde + 1):
      a[k] = hulpa[k]

  return a


  



if __name__ == "__main__":
    a = [int(_) for _ in input().split()]
    print(mergeSort(a))