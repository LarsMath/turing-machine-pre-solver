import Problems as p

BLUE = 0
YELLOW = 1
PURPLE = 2

codes = [(b, y, p) for b in range(1,6) for y in range(1,6) for p in range(1,6)]

def pre_solve(verifiers):
    results = {c: {v: v(c) for v in verifiers} for c in codes}

    erronous_codes = [code for (code, result) in results.items() if -1 in result.values()]
    indistinguishable_codes = [code for (code, result) in results.items() if any(result == r for (c, r) in results.items() if c != code)]
    superfluous_verifier_codes = [code for (code, result) in results.items() if any(all(any(result[w] != r[w] for w in verifiers if v != w) for (c, r) in results.items() if c != code) for v in verifiers)]
    
    impossible_codes = erronous_codes + indistinguishable_codes + superfluous_verifier_codes
    return set(codes) - set(impossible_codes)


for i, problem in enumerate(p.problems):
    print("\nPossible codes for problem %d:" % (i+1))
    print("{:<8}{:<8}{:<8}".format("BLUE", "YELLOW", "PURPLE"))
    print("-"*24)
    for code in pre_solve(problem):
        print("{:<8}{:<8}{:<8}".format(code[BLUE], code[YELLOW], code[PURPLE]))

