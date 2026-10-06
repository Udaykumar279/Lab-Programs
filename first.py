# Facts
parents = {
    'john': ['mary', 'tom'],
    'susan': ['mary', 'tom'],
    'mary': ['alice'],
    'mike': ['alice']
}

gender = {
    'john': 'male',
    'tom': 'male',
    'mike': 'male',
    'susan': 'female',
    'mary': 'female',
    'alice': 'female'
}

# Rules
def is_parent(x, y):
    return y in parents.get(x, [])

def is_male(x):
    return gender.get(x) == 'male'

def is_female(x):
    return gender.get(x) == 'female'

def is_father(x, y):
    return is_parent(x, y) and is_male(x)

def is_mother(x, y):
    return is_parent(x, y) and is_female(x)

def is_grandparent(x, y):
    for child in parents.get(x, []):
        if y in parents.get(child, []):
            return True
    return False


# Queries
print("father(john, mary):", is_father('john', 'mary'))
print("mother(susan, tom):", is_mother('susan', 'tom'))
print("grandparent(john, alice):", is_grandparent('john', 'alice'))

print("father(X, alice):")
for person in gender:
    if is_father(person, 'alice'):
        print("X =", person)

print("grandparent(X, alice):")
for person in gender:
    if is_grandparent(person, 'alice'):
        print("X =", person)