from lib import *
import heapq
import binascii


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
    print(s)

    def it(x, y):
        return x in range(288, 331) and y in range(-96, -49)

    def sim(dx, dy):
        x = 0
        y = 0

        s = set()

        for _ in range(1000):
            s.add((x, y))

            if it(x, y):
                return True, 0

            if x > 331 or y < -96:
                break

            x += dx
            y += dy

            dx -= 1
            if dx < 0:
                dx = 0
            dy -= 1


        return any(it(i, j) for i, j in s), max(map(lambda x: x[1], s))

    ans = 0
    works = set()
    pi = 0
    for i, j in product(range(0, 400), range(-1000, 1000)):
        if i != pi:
            print(i)
            pi = i

        a, m = sim(i, j)
        if a:
            works.add((i, j))
            ans = max(ans, m)

    print(ans)
    print(len(works))



if __name__ == '__main__':
    setup_solve(solve, 17, year=2021)
