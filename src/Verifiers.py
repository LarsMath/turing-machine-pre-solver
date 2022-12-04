BLUE = 0
YELLOW = 1
PURPLE = 2

v1 = lambda c : c[BLUE] > 1
v2 = lambda c : (c[BLUE] >= 3) - (c[BLUE] <= 3) + 1
v3 = lambda c : (c[YELLOW] >= 3) - (c[YELLOW] <= 3) + 1
v4 = lambda c : (c[YELLOW] >= 4) - (c[YELLOW] <= 4) + 1
v5 = lambda c : (c[BLUE]) % 2
v6 = lambda c : (c[YELLOW]) % 2
v7 = lambda c : (c[PURPLE]) % 2
v8 = lambda c : (c[BLUE] == 1) + (c[YELLOW] == 1) + (c[PURPLE] == 1)
v9 = lambda c : (c[BLUE] == 3) + (c[YELLOW] == 3) + (c[PURPLE] == 3)
v10 = lambda c : (c[BLUE] == 4) + (c[YELLOW] == 4) + (c[PURPLE] == 4)
v11 = lambda c : (c[YELLOW] >= c[BLUE]) - (c[BLUE] >= c[YELLOW]) + 1
v12 = lambda c : (c[PURPLE] >= c[BLUE]) - (c[BLUE] >= c[PURPLE]) + 1
v13 = lambda c : (c[PURPLE] >= c[YELLOW]) - (c[YELLOW] >= c[PURPLE]) + 1
def v14(c):
    if c[BLUE] < c[YELLOW] and c[BLUE] < c[PURPLE]:
        return 0
    elif c[YELLOW] < c[BLUE] and c[YELLOW] < c[PURPLE]:
        return 1
    elif c[PURPLE] < c[BLUE] and c[PURPLE] < c[YELLOW]:
        return 2
    else:
        return -1
def v15(c):
    if c[BLUE] > c[YELLOW] and c[BLUE] > c[PURPLE]:
        return 0
    elif c[YELLOW] > c[BLUE] and c[YELLOW] > c[PURPLE]:
        return 1
    elif c[PURPLE] > c[BLUE] and c[PURPLE] > c[YELLOW]:
        return 2
    else:
        return -1
v16 = lambda c : 0 if ((c[BLUE] % 2) + (c[YELLOW] % 2) + (c[PURPLE] % 2) <= 1) else 1
v17 = lambda c : (c[BLUE] % 2) + (c[YELLOW] % 2) + (c[PURPLE] % 2)
v18 = lambda c : (c[BLUE] + c[YELLOW] + c[PURPLE]) % 2
v19 = lambda c : (c[BLUE] + c[YELLOW] >= 6) - (c[BLUE] + c[YELLOW] <= 6) + 1
def v20(c):
    if c[BLUE] == c[YELLOW] and c[BLUE] == c[PURPLE]:
        return 0
    elif c[YELLOW] == c[BLUE] or c[YELLOW] == c[PURPLE] or c[BLUE] == c[PURPLE]:
        return 1
    else:
        return 2
v21 = lambda c : v20(c) == 1