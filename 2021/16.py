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
    b = bin(int(lines[0], 16))[2:]
    while len(b) % 4 != 0:
        b = '0' + b

    a1 = 0

    def sol(t, arr):
        if t == 0:
            return sum(arr)

        if t == 1:
            p = 1
            for i in arr:
                p *= i
            return p

        if t == 2:
            return min(arr)

        if t == 3:
            return max(arr)

        if t == 5:
            return 1 if arr[0] > arr[1] else 0
        if t == 6:
            return 1 if arr[0] < arr[1] else 0

        if t == 7:
            return 1 if arr[0] == arr[1] else 0

    def parse(pos):
        nonlocal a1

        ctr = 0

        ver = int(b[pos:pos+3], 2)
        type = int(b[pos+3:pos+6], 2)

        a1 += ver

        ctr += 6

        if type == 4:
            rep = ''

            while True:

                rep += b[pos+ctr+1:pos+ctr+1+4]

                if b[pos+ctr] == '0':
                    ctr += 5
                    break

                ctr += 5

            val = int(rep, 2)

            return ctr, val
        else:
            tid = b[pos+ctr]
            ctr += 1

            if tid == '0':
                # print(b)
                # print(b[7:7+15])
                tl = int(b[pos+ctr:pos+ctr+15], 2)
                ctr += 15

                vals = []

                while tl != 0:
                    nr, val = parse(pos+ctr)
                    vals.append(val)
                    # print(nr)
                    tl -= nr
                    ctr += nr

                return ctr, sol(type, vals)

            else:
                tn = int(b[pos+ctr:pos+ctr+11], 2)
                # print(tn)
                ctr += 11
                vals = []
                for _ in range(tn):
                    nr, val = parse(pos+ctr)
                    vals.append(val)
                    ctr += nr

                return ctr, sol(type, vals)

    _, a2 = parse(0)

    su1(a1)

    su2(a2)


if __name__ == '__main__':
    setup_solve(solve, 16, year=2021)
