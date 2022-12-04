BLUE = 0
YELLOW = 1
PURPLE = 2

codes = [(b, y, p) for b in range(1,6) for y in range(1,6) for p in range(1,6)]

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

def pre_solve(verifiers):
    results = {c: {v: v(c) for v in verifiers} for c in codes}

    erronous_codes = [code for (code, result) in results.items() if -1 in result.values()]
    indistinguishable_codes = [code for (code, result) in results.items() if any(result == r for (c, r) in results.items() if c != code)]
    superfluous_verifier_codes = [code for (code, result) in results.items() if any(all(any(result[w] != r[w] for w in verifiers if v != w) for (c, r) in results.items() if c != code) for v in verifiers)]
    
    impossible_codes = erronous_codes + indistinguishable_codes + superfluous_verifier_codes
    return set(codes) - set(impossible_codes)


problem01 = [v4, v9, v11, v14]
problem02 = [v4, v9, v13, v17]
problem03 = [v3, v7, v10, v14]
problem04 = [v3, v8, v15, v16]
problem05 = [v2, v6, v14, v17]
problem06 = [v2, v7, v10, v13]
problem07 = [v8, v12, v15, v17]
problem08 = [v3, v5, v9, v15, v16]
problem09 = [v1, v7, v10, v12, v17]
problem10 = [v2, v6, v8, v12, v15]
problem11 = [v5, v10, v11, v15, v17]
problem12 = [v4, v9, v18, v20]
problem13 = [v11, v16, v19, v21]

problems = [problem01,
problem02,
problem03,
problem04,
problem05,
problem06,
problem07,
problem08,
problem09,
problem10,
problem11,
problem12,
problem13]

for i, problem in enumerate(problems):
    print("\nPossible codes for problem %d:" % (i+1))
    print("{:<8}{:<8}{:<8}".format("BLUE", "YELLOW", "PURPLE"))
    print("-"*24)
    for code in pre_solve(problem):
        print("{:<8}{:<8}{:<8}".format(code[BLUE], code[YELLOW], code[PURPLE]))

