# # # Program to remove duplicates and return details in a dictionary

# # def process_numbers(number_list):
# #     # Remove duplicates using set and convert back to list
# #     unique_values = list(set(number_list))
    
# #     # Create dictionary result
# #     result = {
# #         "original_list": number_list,
# #         "unique_values": unique_values,
# #         "unique_count": len(unique_values)
# #     }
    
# #     return result


# # # Taking input from user
# # numbers = input("Enter numbers separated by spaces: ")

# # # Convert input string to list of integers
# # number_list = list(map(int, numbers.split()))

# # # Call the function
# # output = process_numbers(number_list)

# # # Display result
# # print("\nResult:")
# # print("Original List:", output["original_list"])
# # print("Unique Values:", output["unique_values"])
# # print("Count of Unique Values:", output["unique_count"])
# # Function to perform set operations

# def set_operations(set1=None, set2=None):
    
#     # If user does not provide sets, use empty sets as default
#     if set1 is None:
#         set1 = set()
#     if set2 is None:
#         set2 = set()
    
#     # Perform operations
#     union_result = set1.union(set2)
#     intersection_result = set1.intersection(set2)
#     difference_result = set1.difference(set2)
    
#     # Return results in dictionary
#     return {
#         "Union": union_result,
#         "Intersection": intersection_result,
#         "Difference (set1 - set2)": difference_result
#     }


# # Taking input from user
# input1 = input("Enter elements of first set separated by space (or press Enter to skip): ")
# input2 = input("Enter elements of second set separated by space (or press Enter to skip): ")

# # Convert input to sets (if provided)
# set1 = set(map(int, input1.split())) if input1 else None
# set2 = set(map(int, input2.split())) if input2 else None

# # Call function using keyword arguments
# result = set_operations(set1=set1, set2=set2)

# # Display results clearly
# print("\n--- Set Operation Results ---")
# print("Union:", result["Union"])
# print("Intersection:", result["Intersection"])
# print("Difference (set1 - set2):", result["Difference (set1 - set2)"])
# Define a tuple with mixed data types
my_tuple = (10, "Nazmul", 3.14, True)

# Unpacking tuple values into separate variables
number, name, pi_value, status = my_tuple

# Display unpacked values
print("Unpacked Values:")
print("Number:", number)
print("Name:", name)
print("Pi Value:", pi_value)
print("Status:", status)

# Define another tuple for comparison
another_tuple = (10, "Nazmul", 2.71, False)

# Comparing tuples using comparison operators
print("\nTuple Comparisons:")
print("Are tuples equal? ->", my_tuple == another_tuple)
print("Is my_tuple greater than another_tuple? ->", my_tuple > another_tuple)
print("Is my_tuple less than another_tuple? ->", my_tuple < another_tuple)
print("Are tuples not equal? ->", my_tuple != another_tuple)


# ---------------------------------------------------------
# Difference Between List and Tuple (Important Notes)
# ---------------------------------------------------------

# 1. Lists are mutable → You can change, add, or remove elements.
#    Example:
#    my_list = [1, 2, 3]
#    my_list[0] = 100   # This is allowed

# 2. Tuples are immutable → You cannot change their elements after creation.
#    Example:
#    my_tuple = (1, 2, 3)
#    my_tuple[0] = 100  # This will cause an error

# 3. Lists use square brackets: []
# 4. Tuples use parentheses: ()

# 5. Tuples are generally faster and safer when data should not change.