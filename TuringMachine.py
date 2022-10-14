BLUE = 0
YELLOW = 1
PURPLE = 2

codes = [(b, y, p) for b in range(1,6) for y in range(1,6) for p in range(1,6)]

v4 = lambda c : (c[YELLOW] >= 4) - (c[YELLOW] <= 4) + 1
v9 = lambda c : (c[BLUE] == 3) + (c[YELLOW] == 3) + (c[PURPLE] == 3)
v11 = lambda c : (c[YELLOW] >= c[BLUE]) - (c[BLUE] >= c[YELLOW]) + 1
def v14(c):
    if c[BLUE] < c[YELLOW] and c[BLUE] < c[PURPLE]:
        return 0
    elif c[YELLOW] < c[BLUE] and c[YELLOW] < c[PURPLE]:
        return 1
    elif c[PURPLE] < c[BLUE] and c[PURPLE] < c[YELLOW]:
        return 2
    else:
        return -1

def pre_solve(verifiers):
    results = {c: {v: v(c) for v in verifiers} for c in codes}

    erronous_codes = [code for (code, result) in results.items() if -1 in result.values()]
    indistinguishable_codes = [code for (code, result) in results.items() if any(result == r for (c, r) in results.items() if c != code)]
    superfluous_verifier_codes = [code for (code, result) in results.items() if any(all(any(result[w] != r[w] for w in verifiers if v != w) for (c, r) in results.items() if c != code) for v in verifiers)]
    
    impossible_codes = erronous_codes + indistinguishable_codes + superfluous_verifier_codes
    return set(codes) - set(impossible_codes)


problem01 = [v4, v9, v11, v14]

print("Possible codes:\n")
print("{:<8}{:<8}{:<8}".format("BLUE", "YELLOW", "PURPLE"))
print("-"*24)
for code in pre_solve(problem01):
    print("{:<8}{:<8}{:<8}".format(code[BLUE], code[YELLOW], code[PURPLE]))

