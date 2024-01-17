"""
file: wordData.py
author: Raiyan Labeeb
language: python3
purpose:  utility file that defines functions used throughout your
various tasks
"""

def readWordFile(fileName):
    """
    Converts a file with a given format into a dictionary with the format: word: {year: count}
    :param fileName: file
    :return: A dictionary mapping words to dictionaries. The ”inner” dictionary associated
    with each word will use years as keys and counts as values.

    """
    words = {}
    file = "data/" + fileName
    with (open(file) as file):
                line = file.readline()
                if line[0].isalpha() is True:
                    word = line.split("\n")[0]
                    words[word] = {}
                    for num in file:
                            if num[0].isdigit() is True:
                                year, count = num.split(",")[0], num.split(",")[1].split("\n")[0]
                                words[word][year] = count
                            else:
                                word = num.split("\n")[0]
                                words[word] = {}
    return words
def totalOccurrences(word, words):
    """
    :param word:  The word for which to calculate the count.
    :param words: A dictionary mapping words to dictionaries with years and counts.
    :return: total number times word appeared in print
    """

    if word not in words:
        return 0
    else:
        count = 0
        for item in words[word].items():
            count += int(item[1])

    return count
def main():
    file = str(input("Enter word file: "))
    words = (readWordFile(file))
    word = str(input("Enter word: "))
    print(f"Total occurrences of {word}: {totalOccurrences(word, words)}")



if __name__ == "__main__":
    main()