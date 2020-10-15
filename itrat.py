I = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
a = len(I)

b = I[0::2]
print(b)
c = I[10::-1]
print(c)
for i in range(0, 11, 2):
    print(i)

L2 = ['jon', 'ron', 'don', 'tom']
b = L2[-1]
print(b[0])