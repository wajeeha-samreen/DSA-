d = 256 #d represents the number of characters in the input alphabet. By convention, d = 256 is used because 256 is the number of possible ASCII characters

def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    p = 0
    t = 0
    h = 1

    for i in range(M-1):
        h = (h*d) % q

    for i in range(M):
        p = (d*p + ord(pat[i])) % q
        t = (d*t + ord(txt[i])) % q

    for i in range(N-M+1):
        if p == t:
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break
            if j == M-1:
                print("Pattern found at index " + str(i))

        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M])) % q
            if t < 0:
                t = t+q

if __name__ == '__main__':
    txt = "THIS IS A TEST TEXT"
    pat = "Test"
    q = 101
    search(pat, txt, q)
