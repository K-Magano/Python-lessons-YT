person = "Keo"
coins = 4

message = "\n%s has %s coins left."% (person,coins)
print(message)

message = "\n{} has {} coins left".format(person, coins)
print (message)

message = "\n{1} has {0} coins left".format(coins, person)
print (message)

message = "\n{person} has {coins} coins left".format(coins=coins, person=person)
print (message)


player = { "person": "Keo", 'coins': 4 }

message = "\n{person} has {coins} coins left".format(**player)
print (message)

#F_string 

message = f"\n{person} has {coins} coins left."
print (message)

message = f"\n{person} has {2 * 5} coins left."
print (message)

message = f"\n{person.lower()} has {2 * 5} coins left."
print (message)

message = f"\n{player['person']} has {2 * 5} coins left."
print (message)

#You can pass formatting options

num = 10
print(f"\n2.25 times {num} {2.25 * num:.2f}\n")

for num in range(1, 11):
 print(f"2.25 times {num} {2.25 * num:.2f}")


for num in range(1, 11):
 print(f"{num} divided by 4.52 {num / 4.52:.2%}")