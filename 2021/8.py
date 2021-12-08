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
    p1 = 0

    for i in lines:
        d = i.split(' | ')[1].split(' ')

        for j in d:
            if len(j) in (2, 4, 3, 7):
                p1 += 1

    d = {
        0: '1110111',
        1: '0010010',
        2: '1011101',
        3: '1011011',
        4: '0111010',
        5: '1101011',
        6: '1101111',
        7: '1010010',
        8: '1111111',
        9: '1111011'
    }
    b = dict()
    for i in d:
        b[d[i]] = i

    p2 = 0

    for i in lines:
        d = i.split(' | ')[0].split(' ')
        dec = i.split(' | ')[1].split(' ')

        for perm in permutations(range(7)):
            ons = set()

            mp = {
                'a': 0,
                'b': 1,
                'c': 2,
                'd': 3,
                'e': 4,
                'f': 5,
                'g': 6,
            }

            for s in d:
                t = ['0'] * 7
                for c in s:
                    t[perm[mp[c]]] = '1'
                built = ''.join(t)
                if built in b:
                    ons.add(b[built])

            if len(ons) == 10:
                anst = []
                for s in dec:
                    t = ['0'] * 7
                    for c in s:
                        t[perm[mp[c]]] = '1'
                    built = ''.join(t)
                    if built in b:
                        anst.append(b[built])
                ad = int(''.join(map(str, anst)))
                p2 += ad
                break

    su1(p1)
    su2(p2)


if __name__ == '__main__':
    setup_solve(solve, 8, year=2021)
