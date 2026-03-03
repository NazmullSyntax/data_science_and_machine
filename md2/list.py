# # # # print("hellow i am list.py")
# # # items = ["apple", "banana", "cherry"]
# # # print(items) 
# # # print(items[0])
# # # print(items[1])
# # # print(items[2])
# # # print(items[-1])
# # # print(items[-2])
# # # print(items[-3])
# # # items[0] = "grape"
# # # print(items)
# # # items.append("orange")
# # # print(items)
# # # items.insert(1, "kiwi")
# # # print(items)
# # # items.remove("banana")
# # # print(items)
# # # items.pop()
# # # print(items)
# # items = ["apple","mango", "banana", "cherry"]
# # items.sort()
# # print(items)
# # items[2] = "grape"
# # print(items)
# # del items[1]
# # print(items)
# # last_item = items.pop()
# # print(last_item)
# # print(items)
# # items.clear()
# # print(items)
# party_bags =[
#  ["candy", "toy car", "doll"],
#  ["candy", "puzzle", "board game"],
#     ["candy", "action figure", "lego set"]

# ]
# # print(party_bags)
# # print(party_bags[0])
# # print(party_bags[1])
# # print(party_bags[2])
# # print(party_bags[0][0])
# # print(party_bags[0][1])
# # print(party_bags[0][2])
# # print(party_bags[1][0])
# # print(party_bags[1][1])
# # print(party_bags[1][2])
# # print(party_bags[2][0])
# # print(party_bags[2][1])
# # print(party_bags[2][2])
# for bag in party_bags:
#     print(bag)

# for item in party_bags:
#     if item == "candy":
#         print("Found candy in the party bag!")

# list item
items = [
    ["apple", "banana", "cherry"],
    ["grape", "kiwi", "orange"],
    ["mango", "peach", "pear"]
]
index = 0
for bag in items:
    if index == 2:
        continue
    print(bag)
    index += 1
    




