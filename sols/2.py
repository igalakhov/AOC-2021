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
def solve(s, ints, intsf, lines, pats, pats2):
    x, y = 0, 0

    for i, j in pats("{} {N}"):
        if i == 'down':
            y += j
        if i == 'up':
            y -= j
        if i == 'forward':
            x += j

    su1(x * y)

    x, y = 0, 0

    aim = 0

    for i, j in pats("{} {N}"):
        if i == 'down':
            aim += j
        if i == 'up':
            aim -= j
        if i == 'forward':
            x += j
            y += j * aim

    su2(x * y)


if __name__ == '__main__':
    setup_solve(solve, 2, year=2021)



# order(k), |G|/|K1|