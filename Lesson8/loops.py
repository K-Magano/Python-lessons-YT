#while loops

# value = 1 
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1
#   print(value)   

value = 1
# while value <= 10:
#      value += 1
#      if value == 5:
#         continue
#      print(value)
# else:
#     print("Value is now = to" +str(value))

#For Loops 

names = ["Keo", "Olga","Lulu", "Rathi"]
# for name in names:
#     print(name)
    
# for miss in "Mississippi": 
#     print(miss)   

# for name in names:
#     if name == "Olga":
#         break
#     print(name)

# for name in names:
#     if name == "Olga":
#         continue
#     print(name)   

#Rages in for loops

# for name in range(4):
#     print(name)

# for name in range(2,4):
#     print(name)

# for name in range(0, 100, 5):
#     print(name)
# else:
#     print("Glad thats\'s over")
    
names = ["Keo", "Olga","Lulu", "Rathi"]
actions = ["codes", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")