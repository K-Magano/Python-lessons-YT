# Dictionaries are objects

#Option1
band ={
    "vocals": "Plant",
    "guitar": "Pager",
}

#Option2 
band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2) 
print(type(band))
print(len(band))

print("")


 #Access Items
print(band["vocals"])
print(band.get("guitar"))

#list all keys
print(band.keys())
print("")

#list all values
print(band.values())
print("")

#list of keys/values as tuples 
print(band.items())
print("")

#verify a key exists
print("guitar" in band)
print("triangle" in band)
print(" ")

#change values in dictionary

band["vocals"] = "Coverdale"
band.update({"bass": "jpj"})
print(band)

#Remove Items
print(band.pop("bass"))
print(band)

band["drums"] = "Boham"
print(band)
print("")

#removes what was last added 
print(band.popitem()) #tuple
print(band)

#delete and clear

band["drums"] = "Boham"
del band["drums"]
print(band)

band2.clear() 
print(band2)
del band2
print("")

#Copying dictionaries

# band2 = band # creates a reference
# print("Bad Copy")
# print(band2)
# print(band)

# band2["drums"] = "Keo"

print("Good copy")
band2 = band.copy()
band2["drums"] = "Keo"

print(band)
print(band2)

# Or use the dict( constructor function)
band3 = dict(band)
print("Good Copy")
print(band3)

#Nested Dictionary constructor
print("")
print("Nested Dictionary")
print(" ")
member1 = {
    "name": "Plant",
    "instruments": "vocals",
}

member2 = {
    "name": "Plage",
    "instruments": "guitar",
}

band = {
    "member1": member1,
    "member2": member2,
}

print(" ")
print(band)
print(band["member1"]["name"])
print("")

# Sets 
print("Sets")
nums = { 1,2,3,4,1,2}
nums2 = set((1,2,3,4,6,6))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

#True is dupe of 1, False is dupe of Zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

#Check if value is in set
print(2 in nums)

#Adding a new element to a set
nums.add(8)
print(nums)

morenums = {5,6,7}
nums.update(morenums)
print(nums)

# Merging sets
one = {1,2,3}
two = {5,6,7}

mynewset = one.union(two)
print(mynewset)

# Keeping duplicates

one = {1,2,3}
two = {2,3,4}
one.intersection_update(two)
print(one)

#excluding the duplicates 
one = {1,2,3}
two = {2,3,4}
one.symmetric_difference_update(two)
print(one)