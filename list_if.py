# l = []

# if l:
#     for i in l:
#         print(l)
# else:
#     print('there is no item in l')

# n = str(input('please enter your name: '))

# if n:
#     print('welcome {}'.format(n))
# else:
#     print('please enter your name jhk')

l = ['root', 'admin', 'administrator', 'general']

user_name = str(input('please eneter your user name '))

if user_name not in l:
    print('user name is not in l ')
    print('but I added your user name in list')
    print('welcome {}'.format(user_name))
    l.append(user_name)
else:
    print('welcome {}'.format(user_name))

