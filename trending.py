"""
file: trending.py
author: Raiyan Labeeb
language: python3
purpose: compute the top and bottom trending words
between a given starting and ending year
"""
import wordData
def trending(words, startYr, endYr):
    """
    :param words: : A dictionary mapping words to dictionaries with years and counts.
    :param startYr: An integer, the starting year for the computation of the trending words.
    :param endYr: An integer, the ending year for the computation of the trending words
    :return: A list containing a tuple (word, trend) entry for each word for which qualifying data
    exists. The list is sorted in decreasing trend value.
    """
    startYr = str(startYr)
    endYr = str(endYr)
    trend_list = []
    for word in words:
        if startYr in words[word] and endYr in words[word]:
            if int(words[word][startYr]) >= 1000 and int(words[word][endYr]) >= 1000:
                trend_list.append((word, (int(words[word][endYr])/int(words[word][startYr]))))
    trend_list = sorted(trend_list, key=lambda x: x[1], reverse=True)
    return trend_list
def main():
    file = str(input("Enter word file: "))
    words = wordData.readWordFile(file)
    startYr = str(input("Enter starting year: "))
    endYr = str(input("Enter ending year: "))
    trend_lst = (trending(words, startYr, endYr))
    print(f"The top {len(trend_lst) if len(trend_lst) < 10 else 10} trending words from {startYr} to {endYr}: ")
    i=0
    while i < 10 and i < len(trend_lst):
        print(trend_lst[i][0])
        i+=1
    print()
    print(f"The bottom {len(trend_lst) if len(trend_lst) < 10 else 10} trending words from {startYr} to {endYr}: ")
    i = -1
    while -i <= 10 and -i < len(trend_lst)+1:
        print(trend_lst[i][0])
        i -= 1


if __name__ == "__main__":
    main()