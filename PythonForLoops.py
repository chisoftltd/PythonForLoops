#Python For Loops
family = ["benjmain", "joy","emmanuel","shepherd", "mikael"]
for x in family:
    print(x)

#Looping Through a String
for x in "emmanuel":
    print(x)

#The break Statement
family = ["benjmain", "joy","emmanuel","shepherd", "mikael"]
for x in family:
    print(x)
    if x == "emmanuel":
        break
print()

family = ["benjmain", "joy","emmanuel","shepherd", "mikael"]
for x in family:
    if x == "shepherd":
        break
    print(x)
print()

#The continue Statement
family = ["benjmain", "joy","emmanuel","shepherd", "mikael"]
for x in family:
    if x == "shepherd":
        continue
    print(x)
print()

#The range() Function
for y in range(9):
    print(y)

print()
for z in range(3, 11):
    print(z)
print()

for t in range(3, 29, 4):
    print(t)
print()

#Else in For Loop
for x in range(-2, -111, -14):
    print(x)
else:
    print("Finally finished!")
print()

#Nested Loops
family = ["benjmain", "joy","emmanuel","shepherd", "mikael"]
gender = ["male", "female"]

for x in family:
    for y in gender:
        print(x, y)
    
#The pass Statement
for x in [0, 1, 2]:
    pass