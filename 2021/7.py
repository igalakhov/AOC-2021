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
    n = intsf(",")

    def c(k):
        return sum(abs(k - j) for j in n)

    def c2(k):
        return sum(abs(k - j)*(1+abs(k - j))/2 for j in n)

    ans1 = 10000000000
    for i in range(min(n), max(n)+1):
        ans1 = min(ans1, c(i))

    su1(ans1)

    ans2 = 10000000000
    for i in range(min(n), max(n) + 1):
        ans2 = min(ans2, c2(i))

    su2(int(ans2))


if __name__ == '__main__':
    setup_solve(solve, 7, year=2021)
