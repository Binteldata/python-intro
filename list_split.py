#name = str(input('Please enter your name: '))

#l = []
#l.append(name)
#print(l)

#this is where I use split to separate each part of the sentence below
#n = 'Who are you and what are you doing here'
#quote = n.split()
#print(quote)

#testing the separated areas with dots
#n = 'Ann.Mary.Jan.Zuzu.Fefe'
#dots = n.split('.')
#print(dots)

#on to a little more complex use of split
database = [
    ['jo', 'jack', 'jon'],
    ['johnson', 'kirby', 'witherspoon'],
    [21, 44, 43],
]

first_name = database[0]
last_name = database[1]
age = database[2]

input_1 = str(input('please enter user or pass : '))
if input_1 == 'f' or input_1 == 'firstname':
    print(first_name)
elif input_1 == 'l' or input_1 == 'lastname':
    print(last_name)
elif input_1 == 'age':
    print(age)
else:
    print('please enter the correct info')