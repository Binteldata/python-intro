#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

a = ();print(type(a))

users = ('me', 'myself', 'eye', 'you', 'them', 'us')
#print(users[0])
#print(users.index('me'))
#users[5] = 'admin' will be an error
#del users[3] will also be an error because tuple doesn't support this function.

password = ('123', '1234', '12345', '123456')

l = []
l.append(users);l.append(password)
#print(l[1]);print(type(l[1]));(type(l[0]));print('class l has', type(l))

# del l[0]
# print(l)

print(l[0][0].index('me'))