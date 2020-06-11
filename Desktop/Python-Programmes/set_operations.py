my_set = set([1, 2, 3, 4])
my_set2 = {1, 2, 5, 6}

# iterating over set
for element in my_set:
    print(element, end=", ")
print()

print("Adding 5 to ", my_set, end=" = ")
my_set.add(5)
print(my_set)

print("Removing 4 from", my_set, end=" = ")
my_set.remove(4)
print(my_set)

print("discarding 2 from", my_set, end=" = ")
my_set.discard(2)
print(my_set)

print(my_set, "intersection", my_set2, "=", my_set.intersection(my_set2))

print(my_set, "difference", my_set2, "=", my_set.difference(my_set2))

print(my_set, "is disjoint", my_set2, "=", my_set.isdisjoint(my_set2))

my_set3 = my_set.union(my_set2)
print(my_set, "union", my_set2, "=", my_set3)

print("Symmetric difference of", my_set, my_set2, "=", my_set.symmetric_difference(my_set2))

print(my_set, "is subset of", my_set3, "=", my_set.issubset(my_set3))

print(my_set, "is superset of", my_set3, "=", my_set.issuperset(my_set3))