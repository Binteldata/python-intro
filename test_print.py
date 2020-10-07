a = 33
f = 12.5
name = 'pedram'



print('the numbers are %d and %f ' % (a,f) ) 
print ('hi %s' % name )
print('the numbers are {} and {} and the name is {} '.format (a, f, name))
#print(f'the numbers are {a} and {f} and the name is {name}')

list_1 = ["mookie", "Amana", "john", "whom"]
print(list_1[0])

a = list_1[1]

a = a.title()
print(a)

b = list_1[-1]
c = list_1[-2]
print(b)
print(c)
print(len(list_1))

list_1.append("car")
print(list_1)

a = list_1.pop(0)
print(list_1)

