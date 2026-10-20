PRIORITEIT = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0}   # Woordenboek: hoe sterk is elk teken? * en / (2) gaan voor + en - (1). "(" krijgt 0, het laagste.

def bereken(a, b, op):              # Hulpfunctie: rekent "a op b" uit, bv. bereken(3, 5, "-") geeft -2
    if op == "+": return a + b      # Is de operator een plus? Dan optellen.
    if op == "-": return a - b      # Min: a - b (de volgorde is belangrijk!)
    if op == "*": return a * b      # Maal
    return a / b                    # Geen van de drie hierboven? Dan is het "/": delen.

def evalueer_postfix(e):            # Rekent een postfix-expressie uit, bv. ["3", "5", "*"] -> 15.0
    stapel = []                     # Lege lijst die we als stapel gebruiken (append = push, pop = pop)
    for token in e:                 # Overloop de tokens één voor één, van links naar rechts
        if token in "+-*/":         # Is het token een operator?
            b = stapel.pop()        # Eerste pop = het RECHTER getal (dat lag bovenaan)
            a = stapel.pop()        # Tweede pop = het LINKER getal
            stapel.append(bereken(a, b, token))   # Reken a op b uit en leg het resultaat terug op de stapel
        else:                       # Geen operator, dus een getal
            stapel.append(float(token))   # Zet de tekst "3" om naar het getal 3.0 en leg het op de stapel
    return stapel.pop()             # Op het einde ligt er nog één getal op de stapel: dat is het antwoord


def infix_naar_postfix(infix):      # Zet infix om naar postfix, bv. ["3", "*", "5"] -> ["3", "5", "*"]
    uitvoer, stapel = [], []        # uitvoer = het resultaat dat we opbouwen; stapel = wachtplaats voor operatoren en "("
    for token in infix:             # Overloop de tokens één voor één
        if token == "(":            # Openend haakje?
            stapel.append(token)    #   -> op de stapel leggen. Het werkt als een "muur".
        elif token == ")":          # Sluitend haakje?
            while stapel[-1] != "(":              # Zolang het bovenste element (stapel[-1] = peek) geen "(" is...
                uitvoer.append(stapel.pop())      #   ...haal het van de stapel en zet het in de uitvoer
            stapel.pop()            # Haal de "(" zelf ook weg, maar zet hem NIET in de uitvoer (postfix heeft geen haakjes)
        elif token in "+-*/":       # Een operator?
            while stapel and PRIORITEIT[stapel[-1]] >= PRIORITEIT[token]:   # Zolang de stapel niet leeg is EN bovenaan een even sterke of sterkere operator ligt...
                uitvoer.append(stapel.pop())      #   ...die eerst naar de uitvoer (die moet eerst uitgerekend worden)
            stapel.append(token)    # Leg daarna de nieuwe operator op de stapel: hij wacht op zijn beurt
        else:                       # Geen haakje en geen operator, dus een getal
            uitvoer.append(token)   #   -> meteen naar de uitvoer
    while stapel:                   # Alle tokens gelezen. Zolang er nog iets op de stapel ligt...
        uitvoer.append(stapel.pop())   #   ...zet het in de uitvoer
    return uitvoer                  # Geef de postfix-lijst terug


def rekenmachine(infix_string):     # De rekenmachine zelf, bv. rekenmachine("3 + 5 * 2") -> 13.0
    return evalueer_postfix(infix_naar_postfix(infix_string.split()))
    # Lees dit van binnen naar buiten:
    # 1. infix_string.split()  -> knip de tekst op bij de spaties: "3 + 5 * 2" wordt ["3", "+", "5", "*", "2"]
    # 2. infix_naar_postfix()  -> maak er postfix van: ["3", "5", "2", "*", "+"]
    # 3. evalueer_postfix()    -> reken het uit: 13.0