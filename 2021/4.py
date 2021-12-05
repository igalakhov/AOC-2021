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
    nums = list(map(int, lines[0].split(',')))

    ii = 2

    boards = []
    orders = []

    win1 = 10000000000
    win2 = 0
    ans1 = None
    ans2 = None

    while ii < len(lines):

        def f(x):
            if not x:
                return None
            return int(x)

        board = list(map(lambda x: list(filter(lambda x: x is not None, map(f, x.split(' ')))), lines[ii:ii + 5]))

        for idx, n in enumerate(nums):
            for i in range(5):
                for j in range(5):
                    if board[i][j] == n:
                        board[i][j] = None

            done = False
            for i in range(5):
                if all(board[i][j] is None for j in range(5)):
                    done = True
                    break
                if all(board[j][i] is None for j in range(5)):
                    done = True
                    break

            if done:
                s = 0
                for i in range(5):
                    for j in range(5):
                        if board[i][j]:
                            s += board[i][j]

                if idx < win1:
                    ans1 = n * s
                    win1 = idx
                if idx > win2:
                    ans2 = n * s
                    win2 = idx

                break

        ii += 6

    su1(ans1)
    su2(ans2)

    print(crt([(1, 2), (4, 5), (10, 13), (1, 101), (3, 61)]))


if __name__ == '__main__':
    setup_solve(solve, 4, year=2021)
