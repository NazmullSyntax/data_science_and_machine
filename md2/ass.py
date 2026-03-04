# Program to remove duplicates and return details in a dictionary

def process_numbers(number_list):
    # Remove duplicates using set and convert back to list
    unique_values = list(set(number_list))
    
    # Create dictionary result
    result = {
        "original_list": number_list,
        "unique_values": unique_values,
        "unique_count": len(unique_values)
    }
    
    return result


# Taking input from user
numbers = input("Enter numbers separated by spaces: ")

# Convert input string to list of integers
number_list = list(map(int, numbers.split()))

# Call the function
output = process_numbers(number_list)

# Display result
print("\nResult:")
print("Original List:", output["original_list"])
print("Unique Values:", output["unique_values"])
print("Count of Unique Values:", output["unique_count"])