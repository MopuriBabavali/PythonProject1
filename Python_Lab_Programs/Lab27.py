# Function to check if a string is a palindrome
# python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Example usage:
print(is_palindrome("Madam"))  # True
print(is_palindrome("Python"))  # False