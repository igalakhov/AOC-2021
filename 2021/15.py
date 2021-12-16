from lib import *
import heapq

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
    mp = [[int(i) for i in j] for j in lines]

    @lru_cache(None)
    def f(i, j):
        if i not in range(len(mp)) or j not in range(len(mp[0])):
            return float("inf")

        if i == len(mp)-1 and j == len(mp[0])-1:
            return mp[i][j]

        return mp[i][j] + min(f(i+1, j), f(i, j+1))

    q = [(0, (0, 0))]

    vis = set()

    def acc(i, j):
        return (mp[i % len(mp)][j % len(mp[0])] + i//len(mp) + j//len(mp[0]) - 1) % 9 + 1

    mp2 = [[0]*5*len(mp[0]) for i in range(5*len(mp))]

    for i in range(5*len(mp)):
        for j in range(5*len(mp[0])):
            mp2[i][j] = acc(i, j)

    # for i in mp2:
    #     print(''.join(map(str, i)))

    mp = mp2

    def a2(i, j):
        if i not in range(len(mp)) or j not in range(len(mp)):
            return 0
        return mp[i][j]

    while q:
        d, p = heapq.heappop(q)

        i, j = p

        if (i, j) in vis:
            continue

        vis.add((i, j))

        if i not in range(len(mp)) or j not in range(len(mp[0])):
            continue

        if i == len(mp) - 1 and j == len(mp[0]) - 1:
            su2(d)
            break

        if i == len(mp)//5 - 1 and j == len(mp[0])//5 - 1:
            su1(d)
            pass

        heapq.heappush(q, (d + a2(i+1, j), (i+1, j)))
        heapq.heappush(q, (d + a2(i-1, j), (i - 1, j)))
        heapq.heappush(q, (d + a2(i, j+1), (i, j+1)))
        heapq.heappush(q, (d + a2(i, j-1), (i, j-1)))



if __name__ == '__main__':
    setup_solve(solve, 15, year=2021)
