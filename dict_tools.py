d = {
    'name' : 'Courageous',
    'age' : 43,
    'family_name' : 'Someguy',
}

#keys() command separates all keys and prints them
print(d.keys())

# l = [1, 32, 3, 4, 5, 6]
# print(l[4])

#The values() method returns a view object that displays a list of all the values in the dictionary.
print(d.values())

#The items() method returns a view object that displays a list of dictionary's (key, value) tuple pairs.
print(d.items())

#The get() method returns the value for the specified key if key is in dictionary.
print(d['name']);print(d.get('name'))
print(d.get('name1', 'name1 not in dictionary'))

# del d['name']
# print(d)

a = d.pop('name');print(d)
print(a);print(type(a))

#The copy() method returns a shallow copy of the dictionary. It doesn't modify the original dictionary.
#d2 = d.copy();print(d2)

#The update() method updates the dictionary with the elements from the another dictionary object or from an iterable of key/value pairs.
d2 = {}
d2.update(d);print(d2)