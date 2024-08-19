# Initialize an empty list
my_array = []

# Ask the user how many elements they want to add
n = int(input("How many elements do you want to add to the array? "))

# Loop to get input from the user and add it to the array
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    my_array.append(element)

# Print the resulting array
print("Your array:", my_array)