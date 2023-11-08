
def f():
    text = input("Input text to make it an acronym: ")
    words = text.split()  # Split the input text into words

    acronym = ""
    for word in words:
        if word:  # Check if the word is not empty
            acronym += word[0].upper()  # Add the first letter of each word to the acronym

    print(acronym)

f()
