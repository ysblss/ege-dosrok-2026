s = open("17_28762.txt").readlines()
mn =10**10
for x in s:
    x = int(x)
    if x % 23 == 0 and x < mn:
        mn = x
k = 0
A = []
s = [int(x) for x in s]
for i in range(len(s)-1):
    if (s[i] % mn == 0 and s[i+1] % mn != 0) or (s[i] % mn != 0 and s[i+1] % mn == 0) or (s[i] % mn == 0 and s[i+1] % mn == 0):
        k+=1
        A.append(s[i] + s[i+1])


print(k)
print(max(A))