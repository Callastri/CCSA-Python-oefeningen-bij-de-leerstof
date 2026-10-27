# oefening 1.3.2, pagina 28 in cursus
# Implementeer de iteratieve methode voor binair zoeken.


def zoek_binair(zoekItem, rij):
    n = len(rij)

    l = 0
    r = n - 1

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

if __name__ == "__main__":                   # alleen uitvoeren als je dit bestand zelf runt (niet bij pytest)
    rij = sorted([5, 9, 8, 10, 4, 3, 7, 45, 6, 12])   # sorteer eerst: binair zoeken werkt alleen op een gesorteerde rij
    print(rij)                               # toon de gesorteerde rij: [3, 4, 5, 6, 7, 8, 9, 10, 12, 45]
    index = zoek_binair(8, rij)              # zoek 8 in de rij en bewaar het resultaat in index
    print(f"index = {index}")                # toon het resultaat

