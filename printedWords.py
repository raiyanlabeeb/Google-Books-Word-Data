"""
file: printedWords.py
author: Raiyan Labeeb
language: python3
purpose: compute the total number of printed words
for each year.
"""
import wordData
import matplotlib.pyplot as plt
def printedWords(words):
    """
    Converts information given in words dict to tuple form.
    :param words: dict mapping words to dictionaries with years and counts
    :return: list containing tuples (year, count total words) for each year for which data
    exists. The list must be sorted in ascending order of year.
    """

    # Creates a sorted list containing the years that contain data.
    years = []
    for item in words.items():
        for i in item[1]:
            years.append(i)
    years = list(set(years))
    years.sort()

    # For every year that has data, add the counts for those years
    counts = {}
    for item in words:
        for year in years:
            if year in words[item]:
                if year not in counts:
                    counts[year]= int(words[item][year])
                else:
                    counts[year] += int(words[item][year])
    tuple_list = []
    # Convert the data from counts into a tuple with the form (year, count)
    for item in counts.items():
        tuple_list.append(item)

    tuple_list = sorted(tuple_list)

    list_of_counts = []
    for tuple in tuple_list:
        list_of_counts.append(tuple[1])


    plt.plot(years, list_of_counts)
    plt.show()

    return tuple_list
def wordsForYear(year, yearList):
    """
    Returns the count for a given year.
    :param year:  an integer representing the year being queried.
    :param yearList:  a list of tuples (year, count total words)
    :return: An integer count representing the total number of printed words for that year.
    If there is no entry in yearList for the requested year, the function returns 0.
    """

    for tuple in yearList:
        if int(tuple[0]) == year:
            return tuple[1]
    return 0
def main():
    file = str(input("Enter word file: "))
    words = wordData.readWordFile(file)
    yearList = printedWords(words)
    year = int(input("Enter year: "))
    count = wordsForYear(year, yearList)
    print(f"Total printed words in {year}: {count}")

if __name__ == "__main__":
    main()