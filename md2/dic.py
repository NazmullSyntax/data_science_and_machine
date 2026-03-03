# # print("hi from dic.py")
# guest = {"name": "John",
#  "age": 30, 
#  "city": "New York"
#  }

#  print(guest)
guest = {"name": "John",
 "age": 30,
    "city": "New York"
    }
print(guest)
print(guest["name"])
print(guest["age"])
print(guest["city"])
guest["age"]=31
print(guest)
guest["country"]="USA"
print(guest)
del guest["city"]
print(guest)
for key, value in guest.items():
    print(key, ":", value)
    print(key)
    




