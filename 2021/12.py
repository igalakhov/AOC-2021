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
    adj = pats("{}-{}")
    d = defaultdict(list)

    for i, j in adj:
        d[i].append(j)
        d[j].append(i)

    q = [('start', ('start',))]

    a1 = 0
    vis = set()
    while q:
        n, vs = q.pop()

        if (n, vs) in vis:
            continue

        vis.add((n, vs))

        if n == 'end':
            a1 += 1
            continue

        for j in d[n]:
            if j.islower() and j in vs:
                continue

            q.append((j, tuple(list(vs) + [j])))

    su1(a1)


    a2 = 0
    vis = set()
    q = [('start', ('start',))]
    cnt = set()
    def verify(vs):
        cnt = Counter(vs)

        no = 0
        for i in cnt:
            if i.islower() and cnt[i] > 1:
                no += 1
        return no <= 1



    while q:
        n, vs = q.pop()

        if (n, vs) in vis:
            continue

        vis.add((n, vs))

        if not verify(vs):
            continue

        if n == 'end':
            a2 += 1
            cnt.add(hash(vs))
            continue

        for j in d[n]:
            if j == 'start':
                continue
            if j.islower() and vs.count(j) >= 2:
                continue

            q.append((j, tuple(list(vs) + [j])))

    su2(len(cnt))





if __name__ == '__main__':
    setup_solve(solve, 12, year=2021)
