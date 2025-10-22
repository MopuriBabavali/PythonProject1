# Function to display only vowels in a string
# python
def extract_vowels(text):
    vowels = "aeiouAEIOU"
    return ''.join([ch for ch in text if ch in vowels])

# Example usage:
print(extract_vowels("Python Programming"))  # o oai