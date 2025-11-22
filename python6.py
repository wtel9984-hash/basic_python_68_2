"""
#
# Part: Functions
#
"""
def myfullname(firsName="Unknowe", lastName="Forger"):
    fullName = firsName + "" + lastName
    return fullName

print(myfullname("Loid", "Forger"))
print(myfullname("Yor", "Forger"))
print(myfullname("Anya", "Forger"))
print(myfullname("Bond", "Forger"))

def redPotion(hp):
    hp += 50
    return hp
 
currentHp = 100
print("Current HP:", currentHp)
currentHp = redPotion(currentHp)
print("After using Red Potion, HP:", currentHp)
