# Create a tuple
fruits = ("apple","banana","cherry")

# Accessing elements in a tuple
print(fruits[0]) # Output: "apple"
print(fruits[-1]) # Output: "cherry"

# Looping through a Tuple
for fruit in fruits:
    print(fruit)

# Tuple slicing
print(fruits[1:3])  

# Tuple length
print(len(fruits))

# Count the number of occurrences of a value in a tuple
print(fruits.count("apple"))  #Output: 1

# Get the index of the first occurrence of a value in a tuple
print(fruits.index("banana")) #Output: 1

# Concatenate two tuples
fruits2 =("orange","grape")
fruits += fruits2
print(fruits)  # Output: ("apple", "banana", "cherry", "orange", "grape")