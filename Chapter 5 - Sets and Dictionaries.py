# CHAPTER 5 - SETS AND DICTIONARIES
# marks = {
#     "Harry": 100,
#     "Shubham": 98,
#     "Avisha": 10
# }

# print(marks, type(marks))
# print(marks["Harry"])

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry": 99, "Divyam": 100})
# print(marks['Divyam'])
# print(marks.get("Shivika")) # This will not show an error and will return none, but indexing it will give an error
# print(marks["Shivika"]) # This will give an error

# ------------------> SETS <-------------------------------

s ={10, 20, 30, 30}
e = set() # To make an empty set s = {} will make an empty dictionary

e.add(52)
e.add(52253)
e.add(52242)
print(e)

print(s.intersection(e)) # Will give the common terms in both the sets
print(s.union(e)) # Will generate a new set containing terms of both the sets