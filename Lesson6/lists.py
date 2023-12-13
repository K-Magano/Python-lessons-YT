# List is Array

users = ["Keo", "Pelo", "Magano"]

data = ["Keo", 33, True]

emptylist = []

print("Pelo" in users)

print(users[0])
print(users[-1 ])
print(users.index("Pelo")) 

print("")
print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(" ")
print(len(data))

# Appending lists @ the end
print(" ")
users.append("Mama")
print(users)

print("")
users += ["Tshepo"]
print(users)

print(" ")
users.extend(["Tebogo", "Joey"])
print(users)

# print("")
# users.extend(data)
# print(users)

# Appending lists @ the start

print(" ")
users.insert(0, "Debby")
print(users)

# inserted
print("")
users[2:2] = ["eDDY", "Alex"]
print(users)

# replaced
print("")
users[1:3] =["Dad", "Me"]
print(users)

# removing

print("")
users.remove("Debby")
print(users)

print("")
print(users.pop())
print(users)

print("")
del users[0]
print(users)

#del data

data.clear()
print(data)

#Sorting
print("")
users[1:2] = ["keo"]
users.sort()
print(users)
print("")
users.sort(key=str.lower)
print(users)

# sorting numbers
print(" ")
nums = [5, 25, 56, 3]
nums.reverse()
print(nums)

# highest to lowest
# print("")
# nums.sort(reverse=True)
# print(nums)

print(" ")
print(sorted(nums, reverse=True))
print(nums)

#making a copy
print("")
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]
print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

#Checking types

print(type(nums))

mylist =list([1, "Neo", True])
print(mylist)


#TUPLES 

mytuple = tuple(("Dev" , 42, True))

nogatuple = (1,2,3,4,5,6,7,8,8)

print(mytuple)
print(type(mytuple))
print(type(nogatuple))

#packing a tuple

newlist = list(mytuple)
newlist.append("bob")
newtuplw = tuple(newlist)
print(newtuplw)

# unpacking

(one, *two, three, hey) = nogatuple
print(one)
print(two)
print(hey)
#methods check

print("")

print(nogatuple.count(8))