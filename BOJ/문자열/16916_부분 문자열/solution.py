import sys


def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    lps = [0]*M

    computeLPS(pat, lps)

    i = 0
    j = 0
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        elif pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

        if j == M:
            return 1
    return 0


def computeLPS(pat, lps):
    leng = 0

    i = 1
    while i < len(pat):
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng-1]
            else:
                lps[i] = 0
                i += 1


if __name__ == "__main__":
    txt = sys.stdin.readline().rstrip()
    pat = sys.stdin.readline().rstrip()
    print(KMPSearch(pat, txt))