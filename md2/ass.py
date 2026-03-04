# # Program to remove duplicates and return details in a dictionary

# def process_numbers(number_list):
#     # Remove duplicates using set and convert back to list
#     unique_values = list(set(number_list))
    
#     # Create dictionary result
#     result = {
#         "original_list": number_list,
#         "unique_values": unique_values,
#         "unique_count": len(unique_values)
#     }
    
#     return result


# # Taking input from user
# numbers = input("Enter numbers separated by spaces: ")

# # Convert input string to list of integers
# number_list = list(map(int, numbers.split()))

# # Call the function
# output = process_numbers(number_list)

# # Display result
# print("\nResult:")
# print("Original List:", output["original_list"])
# print("Unique Values:", output["unique_values"])
# print("Count of Unique Values:", output["unique_count"])
# Function to perform set operations

def set_operations(set1=None, set2=None):
    
    # If user does not provide sets, use empty sets as default
    if set1 is None:
        set1 = set()
    if set2 is None:
        set2 = set()
    
    # Perform operations
    union_result = set1.union(set2)
    intersection_result = set1.intersection(set2)
    difference_result = set1.difference(set2)
    
    # Return results in dictionary
    return {
        "Union": union_result,
        "Intersection": intersection_result,
        "Difference (set1 - set2)": difference_result
    }


# Taking input from user
input1 = input("Enter elements of first set separated by space (or press Enter to skip): ")
input2 = input("Enter elements of second set separated by space (or press Enter to skip): ")

# Convert input to sets (if provided)
set1 = set(map(int, input1.split())) if input1 else None
set2 = set(map(int, input2.split())) if input2 else None

# Call function using keyword arguments
result = set_operations(set1=set1, set2=set2)

# Display results clearly
print("\n--- Set Operation Results ---")
print("Union:", result["Union"])
print("Intersection:", result["Intersection"])
print("Difference (set1 - set2):", result["Difference (set1 - set2)"])