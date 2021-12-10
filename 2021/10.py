from lib import *


# REMEMBER
# REPLACE \n with '' if needed

# s -> raw input
# ints -> integers
# intsf -> integers, custom split
# lines -> raw lines
# pats -> split by pattern like {}{N}{W}
# pats2 -> split by pattern like IWIWI (double split)
# su1() -> submit part 1
# su2() -> submit part 2
def solve(s, ints, intsf, lines, pats, pats2, su1, su2):
    vals = {
        '(': 3,
        '[': 57,
        '{': 1197,
        '<': 25137
    }
    clos = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    clos2 = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }
    good = []
    a1 = 0
    a2 = []
    for l in lines:
        stk = []

        skip = False
        for cr in l:
            if cr in clos:
                stk.append(cr)
            else:
                tp = stk.pop()
                if clos[tp] != cr:
                    a1 += vals[clos2[cr]]
                    skip = True
                    break

        if skip:
            continue

        good.append(l)

        comp = ''.join(stk[::-1])

        c2 = 0
        for c in comp:
            c2 *= 5
            if c in '()':
                c2 += 1
            if c in '[]':
                c2 += 2
            if c in '{}':
                c2 += 3
            if c in '<>':
                c2 += 4
        a2.append(c2)


    su1(a1)
    a2.sort()
    su2(a2[len(a2)//2])


if __name__ == '__main__':
    setup_solve(solve, 10, year=2021)
