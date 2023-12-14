squared = lambda num : num * num 

print(squared(2))

addTwo = lambda num : num + 2

print(addTwo(12))

sum_total = lambda a, b : a + b 

print(sum_total(2,2))

#######################

#function that you dont wanna save for later

def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

###############

#Higher Order Functions

numbers = [3, 7, 12, 18 ,20, 21]

squared_nums = map(lambda num : num * num, numbers)
print(list(squared_nums))

#############



odd_nums = filter(lambda num : num % 2 != 0, numbers)
print(list(odd_nums))

######################
#reduce adds numbers together
from functools import reduce 

numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)
print(total)

#simpler version
print(sum(numbers, 10))

#Counting all chrs in the list 
lambda acc, curr : acc + len(curr)

names = ["Keo M", "Sara Ito", "John Jacob Jingleheimerschidt"]

char_count = reduce(lambda acc, curr : acc + len(curr), names, 0)

print(char_count)