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
    def pp(l):
        return list(mp(int, x.split(',')) for x in l.split(" -> "))

    ii = mp(pp, lines)

    d = defaultdict(int)
    d1 = defaultdict(int)

    for s, e in ii:
        if s[0] == e[0]:
            for i in range(min(s[1], e[1]), max(s[1], e[1]) +1):
                d[(s[0], i)] += 1
                d1[(s[0], i)] += 1
        elif s[1] == e[1]:
            for i in range(min(s[0], e[0]), max(s[0], e[0]) + 1):
                d[(i, s[1])] += 1
                d1[(i, s[1])] += 1
        else:
            r1 = range(s[0], e[0] + (-1 if s[0] > e[0] else 1), -1 if s[0] > e[0] else 1)
            r2 = range(s[1], e[1] + (-1 if s[1] > e[1] else 1), -1 if s[1] > e[1] else 1)

            for x, y in zip(r1, r2):
                d[(x, y)] += 1

    ans1 = 0
    ans2 = 0

    for i in d1:
        if d1[i] > 1:
            ans1 += 1

    for i in d:
        if d[i] > 1:
            ans2 += 1

    su1(ans1)
    su2(ans2)

if __name__ == '__main__':
    setup_solve(solve, 5, year=2021)
