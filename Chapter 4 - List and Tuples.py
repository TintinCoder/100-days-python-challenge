# Chapter 4 - List and Tuples

friends = ["Apple", ["Harry", "Tuple", "Kirti"] , "Orange", 5, 345.53, False, "Harry", "Rohan"]
print(friends[0])

# List are mutable i.e they can be changed. ---> Unlike strings

# friends[0] = "Papita"
# print(friends)

### LIST METHODS
friends.append('Divyam') # To add anything at the end of the list

l2 = [1, 53, 3763, 41, 1516, 12, 0]
# l2.reverse()
# print(l2)

l2.insert(3, 33333)
print(l2)

l2.pop()
print(l2)