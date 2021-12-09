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
    d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    ans = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):

            good = True
            for di, dj in d:
                if di + i in range(len(lines)) and dj + j in range(len(lines[0])):
                    n1 = int(lines[i][j])
                    n2 = int(lines[di + i][dj + j])

                    if n2 <= n1:
                        good = False

            r = 1 + int(lines[i][j])

            if good:
                ans += r

    su1(ans)

    vis = set()

    def ss(i, j):

        if (i, j) in vis:
            return 0

        vis.add((i, j))

        if int(lines[i][j]) == 9:
            return 0

        ret = 1

        for di, dj in d:
            if i + di in range(len(lines)) and j + dj in range(len(lines[0])):
                n1 = int(lines[i][j])
                n2 = int(lines[di + i][dj + j])

                ret += ss(i + di, j + dj)

        return ret

    si = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            k = ss(i, j)
            if k != 0:
                si.append(k)

    si.sort()

    su2(si[-1]*si[-2]*si[-3])


if __name__ == '__main__':
    setup_solve(solve, 9, year=2021)
