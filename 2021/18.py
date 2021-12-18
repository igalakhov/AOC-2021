from lib import *
import heapq
import binascii
import copy


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
    class BT:

        def __init__(self, v, l, r):
            self.v = v
            self.l = l
            self.r = r
            self.nxt = None
            self.prev = None

        def ts(self):
            if self.v is None:
                return [self.l.ts(), self.r.ts()]
            return self.v

        def leaf(self):
            return self.v is not None

        def iord(self, d=0):
            if self.leaf():
                return [[self, d]]
            return self.l.iord(d + 1) + self.r.iord(d + 1)

    def fix(lst):
        def unmap(l, d=0):

            if isinstance(l, list):
                return BT(None, unmap(l[0]), unmap(l[1]))
            else:
                return BT(l, None, None)

        unmap(lst)
        return unmap(lst)

    ss = [fix(eval(i)) for i in lines]
    safe = [eval(i) for i in lines]

    def add(b1, b2):
        return BT(None, b1, b2)

    def reduce(bt):

        while True:
            op = False

            # explode
            iord = bt.iord()

            for i in range(1, len(iord)):
                iord[i][0].prev = iord[i - 1][0]
            for i in range(len(iord) - 1):
                iord[i][0].nxt = iord[i + 1][0]

            def split_dfs(cur):
                nonlocal op
                if op:
                    return

                if cur.leaf():
                    if cur.v >= 10:
                        op = True
                        num = cur.v
                        cur.v = None
                        cur.l = BT(num//2, None, None)
                        cur.r = BT(num - num//2, None, None)

                    return

                split_dfs(cur.l)
                split_dfs(cur.r)

            def explode_dfs(cur, d=0):
                nonlocal op

                if op:
                    return

                if cur.leaf():
                    return

                if d >= 4 and cur.l.leaf() and cur.r.leaf():
                    if cur.r.nxt is not None:
                        cur.r.nxt.v += cur.r.v

                    if cur.l.prev is not None:
                        cur.l.prev.v += cur.l.v

                    cur.v = 0
                    cur.l = None
                    cur.r = None

                    op = True
                    return

                explode_dfs(cur.l, d+1)
                explode_dfs(cur.r, d+1)

            explode_dfs(bt)
            split_dfs(bt)

            if not op:
                break

    a1 = ss[0]

    for i in range(1, len(ss)):
        a1 = add(a1, ss[i])
        reduce(a1)


    def mag(lst):
        if isinstance(lst, list):
            return 3*mag(lst[0]) + 2*mag(lst[-1])

        return lst


    su1(mag(a1.ts()))

    def m2(b1, b2):
        res = add(fix(b1), fix(b2))
        reduce(res)
        return mag(res.ts())

    a2 = 0

    for i in safe:
        for j in safe:
            if i == j:
                continue
            a2 = max(a2, m2(i, j))

    su2(a2)


    # def add(a, b):
    #     def shift(x):
    #         ret = []
    #         for i, j in x:
    #             ret.append([i, j+1])
    #         return ret
    #
    #     ll = copy.deepcopy(shift(a) + shift(b))
    #     # print(lst)
    #     # ll = []
    #
    #     # def unmap(l, d=0):
    #     #     nonlocal ll
    #     #
    #     #     for i in l:
    #     #         if isinstance(i, list):
    #     #             unmap(i, d + 1)
    #     #         else:
    #     #             ll.append([i, d])
    #
    #     # unmap(lst)
    #
    #     while True:
    #         nl = copy.deepcopy(ll)
    #         cont = False
    #
    #         # explode
    #         for i in range(1, len(nl)):
    #             if cont:
    #                 continue
    #
    #             if nl[i][1] >= 4 and nl[i-1][1] >= 4:
    #                 # print(nl)
    #                 # print('explode', i-1, i)
    #                 v2 = nl[i][0]
    #                 v1 = nl[i-1][0]
    #
    #                 # print(v1, v2)
    #
    #                 nl[i][0] = 0
    #                 nl[i-1][0] = 0
    #                 nl[i-1][1] -= 1
    #                 nl[i][1] -= 1
    #
    #                 if i < len(nl)-1:
    #                     # print(i, nl[i + 1][0])
    #                     nl[i+1][0] += v2
    #                     # del nl[i]
    #
    #                 if i >= 2:
    #                     nl[i-2][0] += v1
    #                     # del nl[i-1]
    #
    #
    #                 del nl[i]
    #
    #
    #
    #                 ll = nl
    #                 cont = True
    #                 break
    #
    #         # split
    #         for i in range(1, len(nl)):
    #             if nl[i][0] >= 10:
    #                 nm = nl[i][0]
    #                 nl[i][0] = nm//2
    #                 nl[i][1] += 1
    #                 nl.insert(i+1, [nm - nm//2, nl[i][1]])
    #
    #                 ll = nl
    #                 cont = True
    #                 break
    #
    #         if cont:
    #             continue
    #
    #         break
    #
    #     return ll
    #
    #
    # aa = ss[0]
    #
    # print('???')
    #
    # for i in range(1, len(ss)):
    #     print(aa)
    #     aa = add(copy.deepcopy(aa), copy.deepcopy(ss[i]))
    # print(aa)
    # print(mag(aa))
    #
    # 1 / 0


if __name__ == '__main__':
    setup_solve(solve, 18, year=2021)
