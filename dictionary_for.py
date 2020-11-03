# d = {
#     'key_1' : {'name' : 'Rob', 'age' : 33, 'f_name' : 'Base'},
#     'key_2' : {'car' : 'audi', 'max_speed' : 330, 'color' : 'black'},
#     'key_3' : {'date1' : 2001, 'date2' : 2030},
# } 

 #can be written as k for key and v for value
# for k, v in d.items():
     #print(k,v)
     #print(d[k], v)
     #if k == 'key_3':
     #print(v)

d = {
    'date1' : 1997,
    'date2' : 2003,
    'date3' : 2008,
    'date4' : 2012,
    'date5' : 2020,
}
input_1 = int(input('please enter a date : '))

# for k, v in d.items():
#     if v == int(input_1):
#         print(k)

my_list = [k for (k, v) in d.items() if v == input_1]
print(my_list)
