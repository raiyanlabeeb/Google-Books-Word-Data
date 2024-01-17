"""
file: letterFreq.py
author: Raiyan Labeeb
language: python3
purpose: compute the relative frequency of English
characters occurring in print.
"""
import wordData
import matplotlib.pyplot as plt

def letterFreq(words):
    """
    :param words: dictionary mapping words to dictionaries with years and count
    :return: A string containing the 26 lowercase characters in the English alphabet, sorted in
    decreasing order of frequency of occurrence of each character
    """
    string = "abcdefghijklmnopqrstuvwxyz"
    words_more = {}
    # Puts words in the empty dictionary.
    for word in words:
        words_more[word] = {}
    # Puts all letters of the english alphabet in the dictionary.
    for key in words_more.keys():
        for c in string:
            words_more[key][c] = 0

    # Counts every instance of all characters, and updates the dictionary values.
    for word in words_more:
        count = wordData.totalOccurrences(word, words)
        # Add the count into every character of the word.
        for c in word:
            words_more[word][c] += count

    char_count = {}
    # Populate char_count with letter:count
    for letter in string:
        for word in words_more:
            if letter not in char_count:
                char_count[letter] = words_more[word][letter]
            else:
                char_count[letter] += words_more[word][letter]

    # Sort the characters from most to least.
    total_count = []
    for item in char_count.items():
        total_count.append(item)
    total_count = sorted(total_count, key=lambda x: x[1], reverse=True)

    # Adds all the counts to a new list.
    letter_count = []
    for item in char_count:
        letter_count.append(char_count[item])


    # Sorts the string
    sorted_string = ""
    for letter in total_count:
        sorted_string+= letter[0]

    # Plots the letters
    plt.bar(list(string), list(letter_count), color="skyblue")
    plt.show()
    return sorted_string

def main():
    file = str(input("Enter word file: "))
    words = wordData.readWordFile(file)
    print(f"Letters sorted by decreasing frequency: {letterFreq(words)}")


if __name__ == "__main__":
    main()
