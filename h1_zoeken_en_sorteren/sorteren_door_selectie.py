def selection_sort_vooraan(a):                # functie die de lijst a sorteert, kleinste vooraan
    n = len(a)                                # n = aantal elementen in de lijst
    for i in range(0, n - 1):                 # i = 0, 1, ..., n-2: de plaats die we nu juist willen vullen
        positie = i                           # neem voorlopig aan: het kleinste staat op plaats i
        minimum = a[i]                        # en onthoud de waarde ervan
        for j in range(i + 1, n):             # bekijk alle elementen rechts van i
            if a[j] < minimum:                # is dit element kleiner dan het kleinste tot nu toe?
                positie = j                   #   ja: onthoud zijn plaats
                minimum = a[j]                #   en onthoud zijn waarde
        a[positie] = a[i]                     # wissel, deel 1: op de plaats van het kleinste komt a[i]
        a[i] = minimum                        # wissel, deel 2: het kleinste komt op plaats i
        print(a)                              # toon de lijst na deze ronde (vraag van de opgave)
    return a                                  # geef de gesorteerde lijst terug


if __name__ == "__main__":                    # alleen uitvoeren als je dit bestand zelf runt (niet bij pytest)
    a = [int(_) for _ in input().split()]     # lees getallen in, bv. "44 55 12" wordt [44, 55, 12]
    selection_sort_vooraan(a)                 # roep de functie op met die lijst