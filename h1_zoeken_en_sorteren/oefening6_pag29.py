def som1(n):
    x = 0
    for i in range(1, n + 1):
        x = x + 1
    return x

def som2(n):
    x = 0
    for i in range(1, 2 * n + 1):
        for j in range(1, n + 1):
            x = x + 1
    return x

def som3(n):
    x = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):          # + 1
            for k in range(1, j + 1):      # + 1
                x = x + 1
    return x

def som4(n):
    x = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):          # + 1
            for k in range(1, i + 1):      # i (niet k) en + 1
                x = x + 1
    return x

def som5(n):
    x = 0
    i = n
    while i >= 1:
        x = x + 1
        i = i // 2
    return x

def som6(n):
    x = 0
    i = n
    while i >= 1:
        for j in range(1, i + 1):          # + 1
            x = x + 1
        i = i // 2
    return x

def som7(n):
    x = 0
    i = n
    while i >= 1:
        for j in range(1, n + 1):
            x = x + 1
        i = i // 2
    return x


if __name__ == "__main__":
    print(som1(3), som2(3), som3(3), som4(3), som5(8), som6(8), som7(8))
    # verwacht:  3      18      10      14       4       15      32