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
    gamma = []
    eps = []

    for i in range(len(lines[0])):
        cnt = Counter()
        for j in lines:
            cnt[j[i]] += 1

        if cnt['0'] > cnt['1']:
            gamma.append('0')
            eps.append('1')
        else:
            gamma.append('1')
            eps.append('0')

    # print(gamma, int(''.join(gamma), 2))
    # print(eps, int(''.join(eps), 2))
    su1(int(''.join(gamma), 2)*int(''.join(eps), 2))

    ox = None

    ls = lines[:]

    bt = 0
    while len(ls) != 1:
        cnt = Counter()
        nl = []
        for i in ls:
            cnt[i[bt]] += 1

        good = '1'
        if cnt['0'] > cnt['1']:
            good = '0'

        for i in ls:
            if i[bt] == good:
                nl.append(i)

        ls = nl

        bt += 1

    ox = int(''.join(ls[0]), 2)

    ls = lines[:]

    p2 = None

    bt = 0
    while len(ls) != 1:
        cnt = Counter()
        nl = []
        for i in ls:
            cnt[i[bt]] += 1

        good = '0'
        if cnt['0'] > cnt['1']:
            good = '1'

        for i in ls:
            if i[bt] == good:
                nl.append(i)

        ls = nl

        bt += 1

    p2 = int(''.join(ls[0]), 2)
    su2(ox*p2)


if __name__ == '__main__':
    setup_solve(solve, 3, year=2021)