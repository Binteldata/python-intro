# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in my_list:
#     m = i ** 2
#     print(m)

# my_list = list(range(1, 11))

# for i in my_list:
#     m = i ** 2
#     print(m)

squares = []

for value in range(1, 11):
    # square = value**2
    # squares.append(square)
    # print(squares)
#print(squares)
    squares.append(value**2)
    print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#print(min(digits))

minimum = []
minimum.append(min(digits))
print(minimum)
print(max(digits))
print(sum(digits))

a_list = [i for i in range(1, 11)]
print(a_list)

players = ['charles', 'martin', 'michael', 'eli', 'chris', 'john']

for player in players[:3]:
    print(player.title())

