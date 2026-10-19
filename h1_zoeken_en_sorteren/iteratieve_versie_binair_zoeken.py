def zoek_binair(zoekItem,rij):
    n = len(rij)
    
    l = 0
    r = n -1

    while l != r:
        print(f"{l}, {r}")
        m = (l + r) // 2
        if rij[m] < zoekItem:
            l = m + 1
        else:
            r = m
    if rij[l] == zoekItem:
        index = l
    else:
        index = -1
    return index

if __name__ == "__main__":
    rij = sorted([5, 9, 8, 10, 4, 3, 7, 45, 6, 12]) 
    print(rij)
    index = zoek_binair(8, rij)
    print(f"index = {index}")