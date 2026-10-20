operators = ["+", "-", "*", "/", "("]

def isOperand(s):
    return s.isnumeric()

def isOperator(s):
    return s in operators

def voerBewerkingUit(operator, getal1, getal2):
    if operator == "+":
        return getal1 + getal2
    elif operator == "-":
        return getal1 - getal2
    elif operator == "*":
        return getal1 * getal2
    elif operator == "/":
        return getal1 / getal2

def prioriteit(operator):
    if operator == "*" or operator == "/":
        return 2
    elif operator == "+" or operator == "-":
        return 1
    elif operator == "(":
        return 0

def evalueer_postfix(rijVanStrings):
    stack = []
    for s in rijVanStrings:
        if isOperand(s):
            stack.append(float(s))                
        elif isOperator(s):
            getal2 = stack.pop()
            getal1 = stack.pop()
            uitkomst = voerBewerkingUit(s, getal1, getal2)
            stack.append(uitkomst)
    return stack.pop()

def infix_naar_postfix(infixRijVanStrings):
    stapel = []                                    
    uitvoer = []                                   
    for s in infixRijVanStrings:
        if isOperand(s):
            uitvoer.append(s)
        elif isOperator(s):
            if len(stapel) == 0 or s == "(" or prioriteit(s) > prioriteit(stapel[-1]):
                stapel.append(s)                   
            else:
                while len(stapel) > 0 and prioriteit(s) <= prioriteit(stapel[-1]):   
                    operator = stapel.pop()
                    uitvoer.append(operator)
                stapel.append(s)
        elif s == ")":
            while stapel[-1] != "(":
                operator = stapel.pop()
                uitvoer.append(operator)
            stapel.pop()
    while len(stapel) > 0:
        uitvoer.append(stapel.pop())
    return uitvoer


def rekenmachine(infix_string):
    infix_tokens = infix_string.split()
    postfix = infix_naar_postfix(infix_tokens)
    return evalueer_postfix(postfix)