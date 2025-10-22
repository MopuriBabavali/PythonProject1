# Function to calculate the average of numbers in a list
# python
def average_of_list(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# Example usage:
nums = [3, 5, 7, 9]
print("Average:", average_of_list(nums))