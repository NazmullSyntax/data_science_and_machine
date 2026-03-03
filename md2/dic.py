# # # print("hi from dic.py")
# # guest = {"name": "John",
# #  "age": 30, 
# #  "city": "New York"
# #  }

# #  print(guest)
# guest = {"name": "John",
#  "age": 30,
#     "city": "New York"
#     }
# print(guest)
# print(guest["name"])
# print(guest["age"])
# print(guest["city"])
# guest["age"]=31
# print(guest)
# guest["country"]="USA"
# print(guest)
# del guest["city"]
# print(guest)
# for key, value in guest.items():
#     print(key, ":", value)
#     print(key)

# nested_dic = {

party_guests = [
    guest1 := {"name": "John", "age": 30, "city": "New York"},
    guest2 := {"name": "Alice", "age": 25, "city": "Los Angeles"},
    guest3 := {"name": "Bob", "age": 35, "city": "Chicago"}
]

print(party_guests)
print(party_guests[0])  # Accessing the first guest
print(party_guests[1]["name"])  # Accessing the name of the second guest
for guest id in party_guests:
    print(guest["name"], "is from", guest["city"])
    




