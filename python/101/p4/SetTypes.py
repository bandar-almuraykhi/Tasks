 # Create a set and frozenset
a = {1, 2, 3}
b = frozenset([2, 3, 4])

# Add and remove
a.add(5)
a.remove(1)

# Union
print(a | b)

# Intersection
print(a & b)

# Difference
print(a - b)

# Symmetric Difference
print(a ^ b)
