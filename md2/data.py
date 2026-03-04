# # # print("helloworld")
# # love = {'python', 'java', 'c++', 'javascript'}
# # love_2 = {'python', 'ruby', 'go'}
# # print(love)
# # love.add('ruby')
# # print(love)
# # love.remove('c++')
# # print(love)
# # love.discard('c++')
# # print(love)

# # love.update(love_2)
# # print(love)
# # x = love.pop()
# # print(x)
# # print(love)
# # set union function
# love = {'python', 'java', 'c++', 'javascript'}
# love_2 = {'python', 'ruby', 'go'}
# love_union = love.union(love_2)
# print(love_union)
set1 = {1, 2, 3, 4,'b'}
set2 = {3, 4, 5, 6,'b'}
set3 = set1.union(set2)
print(set3)
set4 = set1.intersection(set2)
print(set4)
set5 = set1.difference(set2)
print(set5)
set6 = set1.symmetric_difference(set2)
print(set6)



