with open('rosalind_revc.txt') as file:
    a = file.read()

b = a.replace('A', 't')
c = b.replace('T', 'a')
d = c.replace('C', 'g')
e = d.replace('G', 'c')

f = e.upper()
g = f[::-1]
print(g)

