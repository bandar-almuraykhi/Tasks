 # Create a function with one parameter
def count_vowels(text):
    # Start the counter
    count = 0

    # Loop through each character
    for char in text.lower():
        # Check if the character is a vowel
        if char in "aeiou":
            count += 1

    # Return the total count
    return count


# Test the function
print(count_vowels("Education"))
print(count_vowels("PYTHON"))
