K = map(int,raw_input().split())
N = map(int,raw_input().split())
A = set(map(int,raw_input().split()))
B = set(map(int,raw_input().split()))
H = 0
for i in xrange(K[0]):
    if N[i] in A:
        H = H+1
    elif N[i] in B:
        H = H-1
    else: pass

print H