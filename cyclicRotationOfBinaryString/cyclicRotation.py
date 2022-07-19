#s = "10101"
s = '101010'
n = 2
max = ""
p = -1
for i in range(len(s)):
    if max < s:
        max = s
        d = i
    elif max == s:
        p = i - d
        print(p)
        break
    s = s[1:]+s[:1]

if p == -1:
    print(d + (n-1)*len(s))
else:
    print(d + (n-1)*p)