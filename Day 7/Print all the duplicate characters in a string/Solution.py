# Python3 program to count all duplicates
# from a string using a dictionary

def printDups(Str):
    # Dictionary to store character counts
    count = {}

    # Count each character in the string
    for char in Str:
        count[char] = count.get(char, 0) + 1  # increment count if character exists, else set to 1

    # Print duplicates with their counts
    for char, char_count in count.items():
        if char_count > 1:  # duplicate found if count is greater than 1
            print(f"{char}, count = {char_count}")

# Driver code
Str = "test string"
printDups(Str)


