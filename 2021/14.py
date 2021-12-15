from lib import *
import string

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
    p = lines[0]
    pp = lines[0]

    pat = mp(lambda x: parse(x, "{} -> {}"), lines[2:])

    trans = dict()
    for j, k in pat:
        trans[j] = j[0] + k + j[1]

    for i in range(10):

        s = []

        for i in range(len(p)-1):
            if p[i]+p[i+1] in trans:
                s.append(trans[p[i]+p[i+1]][:2])
        s.append(p[-1])

        p = ''.join(s)

    c = Counter(p)

    su1(max(c.values()) - min(c.values()))

    c2 = Counter()
    for i in range(len(pp)-1):
        c2[pp[i:i+2]] += 1

    for i in range(40):
        nc = Counter()

        for k in c2:
            if k in trans:
                s1 = k[0] + trans[k][1]
                s2 = trans[k][1] + k[1]

                nc[s1] += c2[k]
                nc[s2] += c2[k]
            else:
                nc[k] += c2[k]

        c2 = nc

    tf = Counter()
    for i in c2:
        tf[i[0]] += c2[i]
        tf[i[1]] += c2[i]
    tf[pp[0]] += 1
    tf[pp[-1]] += 1
    for i in tf:
        tf[i] /= 2

    su2(int(max(tf.values())-min(tf.values())))




if __name__ == '__main__':
    setup_solve(solve, 14, year=2021)
