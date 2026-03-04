# print("helloworld")
love = {'python', 'java', 'c++', 'javascript'}
love_2 = {'python', 'ruby', 'go'}
print(love)
love.add('ruby')
print(love)
love.remove('c++')
print(love)
love.discard('c++')
print(love)

love.update(love_2)
print(love)


