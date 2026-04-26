def get_longest_word(text):
    words = text.split()
    longest = max(words, key=len)
    return longest

t = input("Enter the text: ")
print("The longest word is:", get_longest_word(t))
