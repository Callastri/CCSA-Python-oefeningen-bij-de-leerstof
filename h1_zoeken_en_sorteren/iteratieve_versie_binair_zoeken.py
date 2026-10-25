def zoek_binair(zoekItem, rij):              # functie die zoekItem zoekt in een GESORTEERDE rij
    n = len(rij)                             # n = aantal elementen in de rij

    l = 0                                    # l = linkergrens van het zoekgebied (eerste vakje)
    r = n - 1                                # r = rechtergrens van het zoekgebied (laatste vakje)

    while l != r:                            # herhaal zolang het zoekgebied meer dan 1 vakje heeft
        print(f"{l}, {r}")                   # toon de grenzen (controle-uitvoer van de opgave)
        m = (l + r) // 2                     # m = midden van het zoekgebied, naar beneden afgerond
        if rij[m] < zoekItem:                # is het middelste element kleiner dan wat we zoeken?
            l = m + 1                        #   ja: het zit rechts van m, dus zoek verder in de rechterhelft
        else:                                # nee: het zit op m of links ervan
            r = m                            #   dus zoek verder in de linkerhelft (m blijft erbij!)
    if rij[l] == zoekItem:                   # er blijft 1 vakje over: is dat wat we zoeken?
        index = l                            #   ja: gevonden op plaats l
    else:
        index = -1                           #   nee: niet gevonden, -1 betekent "zit er niet in"
    return index                             # geef het resultaat terug


if __name__ == "__main__":                   # alleen uitvoeren als je dit bestand zelf runt (niet bij pytest)
    rij = sorted([5, 9, 8, 10, 4, 3, 7, 45, 6, 12])   # sorteer eerst: binair zoeken werkt alleen op een gesorteerde rij
    print(rij)                               # toon de gesorteerde rij: [3, 4, 5, 6, 7, 8, 9, 10, 12, 45]
    index = zoek_binair(8, rij)              # zoek 8 in de rij en bewaar het resultaat in index
    print(f"index = {index}")                # toon het resultaat

