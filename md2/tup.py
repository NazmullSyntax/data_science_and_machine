# my = ('apple', 'banana', 'cherry')
# print(my)
# # print(my[1])
# # # my[1] = 'blackcurrant' # This will raise an error because tuples are immutable
# print(len(my))
# print(type(my))
# print(type(my[0]))
# print(type(my[1:3]))

# # my_tuple = ('apple', 'banana', 'cherry', 'apple', 'cherry')
# # print(my_tuple)
# # print(my_tuple.count('apple'))
# # print(my_tuple.count('cherry'))
# # print(my type(my_tuple))
# # print(my type(my_tuple[0]))
# # print(my type(my_tuple[1:3]))
my_tuple = ('apple', 'banana', 'cherry')
print(my_tuple)
x = list(my_tuple)
print(x)
x.append('orange')
my_tuple = tuple(x)
print(my_tuple)



