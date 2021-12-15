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
    pts = set()
    mode = True
    ins = []
    for i in lines:
        if i == '':
            mode = False
            continue
        if mode:
            pts.add(tuple(parse(i, "{},{}")))
        else:
            ins.append(parse(i, "fold along {}={}"))

    a1 = None
    for a, d in ins:
        ns = set()
        if a == 'x':
            for x, y in pts:
                if x >= d:
                    ns.add((x - d, y))
                else:
                    ns.add((d - x, y))
        if a == 'y':
            for x, y in pts:
                if y >= d:
                    ns.add((x, y - d))
                else:
                    ns.add((x, d - y))
        mx = min(x[0] for x in ns)
        my = min(y[1] for y in ns)

        pts = set((x - mx, y - my) for x, y in ns)
        if a1 is None:
            a1 = len(pts)
    su1(a1)

    grid = [[' ']*100 for i in range(100)]

    for i, j in pts:
        grid[j][i] = '1'

    for line in grid:
        print(''.join(line))

    print(ins)


if __name__ == '__main__':
    setup_solve(solve, 13, year=2021)
