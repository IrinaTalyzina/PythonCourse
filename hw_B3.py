with open('rosalind_hamm.txt') as file:
    f = file.readlines()
    a = f[0].strip()
    b = f[1].strip()


i = 0
n = 1

if a[0] != b[0]:
    i += 1
 
while n < len(a):
    if a[n] == b[n]:
        n += 1

    elif a[n] != b[n]:
        i += 1
        n += 1

print(i)

