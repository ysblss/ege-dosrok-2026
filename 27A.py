from math import dist
def f(K):
    c = 0
    mn = 1000000000000000000000000000000
    for t1 in K:
        sm = 0
        for t2 in K:
            sm += dist(t1[:-1], t2[:-1])
        if sm < mn:
            mn = sm
            c = t1
    return c



s = open("27_A_28766.txt").readlines()
for i in range(len(s)):
    s[i] = s[i].replace(",",'.')
    s[i] = s[i].split()
    s[i][0] = float(s[i][0])
    s[i][1] = float(s[i][1])



K1 = []
K2 = []
for t in s:
    x, y, z = t
    if y > 8:
        K1.append(t)
    else:
        K2.append(t)
C1 = f(K1)
G = []
for t in s:
    x, y, z = t
    if z[0] == "Y" and z[-3:] == "III":
        G.append(t)
mns = 10000000000000000000
mxs = 0
for t in G:
    mns = min(dist(C1[:-1], t[:-1]), mns)
for t in G:
    mxs = max(dist(C1[:-1], t[:-1]), mxs)
print(mns * 10000)
print(mxs*10000)
