# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as file:
        content = file.read()
    return content


def count_words():
    text = read_file_content("./story.txt")
    # first we turn the text read from the text file and place it in an array and format it
    formated_text = text.replace(".", '')
    formated_text = formated_text.replace("?", '')
    formated_text = formated_text.replace("\n", '')
    text_array = formated_text.split(" ")
    # now we must create a unique list of words from the original text list
    unique_array = []
    result = {}
    # the result is a dictionary that will be populated later
    for word in text_array:
        if word not in unique_array:
            unique_array.append(word)
    # we append the word to the list if the list did not already have the word as an element
    # we must now tally the number of repeated words
    for unique_word in unique_array:
        result[unique_word] = text_array.count(unique_word)

    return result


print(count_words())
