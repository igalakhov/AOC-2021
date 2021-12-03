from lib import *


# REMEMBER
# REPLACE \n with '' if needed

def solve(s, ints, intsf, lines, pats, pats2):
    # print(len(s))
    # print(parse('token word 2 to 2', '{} word {} to {}'))
    # print(parse('10R', '{N}{}'))
    dat = get_pat(s, pat='I')

    ans1 = 0
    for i in range(1, len(dat)):
        if dat[i] > dat[i-1]:
            ans1 += 1

    print('Part 1: %d' % ans1)
    su1(ans1)

    ans2 = 0
    for i in range(4, len(dat)+1):
        if sum(dat[i-3:i]) > sum(dat[i-4:i-1]):
            ans2 += 1

    print('Part 2: %d' % ans2)
    su2(ans2)


if __name__ == '__main__':
    setup_solve(solve, 1, year=2021)
