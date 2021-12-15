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
    gr = [[int(i) for i in l] for l in lines]

    a1 = 0
    a2 = 100000000000

    for ii in range(10000):
        ng = [i[:] for i in gr]
        n, m = len(ng), len(ng[0])

        for i in range(n):
            for j in range(m):
                ng[i][j] += 1

        d = set(product((-1, 0, 1), (-1, 0, 1)))
        d.remove((0, 0))

        flashed = set()

        while True:
            af = False

            for i in range(n):
                if af:
                    break
                for j in range(m):
                    if af:
                        break

                    if ng[i][j] > 9 and (i, j) not in flashed:
                        ng[i][j] = 0
                        flashed.add((i, j))
                        for di, dj in d:
                            if di + i in range(n) and dj + j in range(m):
                                ng[di + i][dj + j] += 1
                        af = True

            if not af:
                break
        for i, j in flashed:
            ng[i][j] = 0
        if ii < 100:
            a1 += len(flashed)
        if len(flashed) == n*m:
            a2 = min(a2, ii+1)
        gr = ng

    su1(a1)
    su2(a2)


if __name__ == '__main__':
    setup_solve(solve, 11, year=2021)
