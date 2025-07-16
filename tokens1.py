# Keywords
import keyword
print(keyword.kwlist)

a = 10
print(id(a))

b = 20
print(id(b))

c = 30
print(id(c))

d = 10
print(id(d))

b = 40
print(id(b))

# Multiple variables at a time
a, b, c = 10, 20, 30
print(id(a))
print(id(b))
print(id(c))

# Creating new variable with existing value
a = 10
b = a
b = 10
print(id(a))
print(id(b))

# Swapping values of variables
a = 10
b = 20
a, b = b, a
print("a after swap:", a)
print("b after swap:", b)
