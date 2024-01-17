"""
file: wordSimilarity.py
author: Raiyan Labeeb
language: python3
purpose:
Outputs information about word similarity.
"""
import wordData
import math
def topSimilar(words, word):
    """
    :param words:  A dictionary mapping words to dictionaries with years and counts. - dict
    :param word: a word, for which we are looking for similar words. - str
    :return: A list of the top five words including the input word in the descending order of
    similarity. If there are less than five words in the file, then return as much words as you
    have. If there is no such a word in the words dictionary, return just one word, itself.
    """

    # Checks if word is in the words dictionary.
    if word not in words:
        return [word]
    # Gets all the lengths for every word, converts it into a dictionary, word: length.
    lengths = {}
    for i in words.items():
        length_1 = 0
        for year in i[1]:
            length_1 += int(i[1][year]) ** 2
        lengths[i[0]] = length_1

    #Multiply every x1/sqrt(length) by y1/sqrt(length)
    similarities = []
    for t in words.items():
        sim = 0
        for year in t[1]:
            if year in words[word]:
                sim += (int(words[t[0]][year]) / math.sqrt(int(lengths[t[0]])) *
                        int(words[word][year]) / math.sqrt(int(lengths[word])))
        similarities.append((t[0], sim))

    # Sorts the list of word, similarity pairs in reversed based on highest similarity
    similarities = sorted(similarities, key = lambda x:x[1], reverse = True)
    word_sim = []
    for pair in similarities:
        if len(word_sim) == 5:
            break
        else:
            word_sim.append(pair[0])
    return word_sim

def main():
    file = str(input("Enter word file: "))
    words = wordData.readWordFile(file)
    word = input("Enter word: ")
    similarities = topSimilar(words, word)

    print("The most similar words are: ")
    if len(similarities) <= 5:
        print(similarities)
    else:
        i = 0
        while i < 5:
            print(similarities[i], end=" ")
            i+=1

if __name__ == "__main__":
    main()