# a = [1, 2, 3] + [4, 5, 6]
# print(a)

#print(['hi'] * 3)

#make a list into string
print(str([1, 2]) + '34')

#make a string into a list
a = list('34');print(a)

for x in [1, 2, 3]:
    #print(x, end= ' ') for spaces between the numbers and horizontal
    print(x)
#make 4 of each letter in the string
rec = [i * 3 for i in 'spam']
print(rec)

#3 different ways to code the same outcome including line 15
res = []
for c in 'spam':
    res.append(c * 3)
print(res)
res = [c *3 for c in 'spam']
print(res)

#remove minus using abs
a = list(map(abs, [1, 2, -4, -70, -23]))
print(a)
b = -90
print(abs(b))

