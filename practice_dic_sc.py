"""Dictionaries Practice

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """

    set_of_words = set(words)
    return list(set_of_words)


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """
    set_items1 = set(items1)
    set_items2 = set(items2)

    return list(set_items1 & set_items2)

def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """
    # Method:
    # use set to remove duplicates and obtain a list afterwards 
    # create unique key being each par of numbers
    # value of each key is its sum
    # return key(s) (=char) with the highest value
    pair = {}
    for i in range(0,len(numbers)):
        key = number[i]

    # list_pairs =[]
    # numbers_unique = without_duplicates(numbers)
    # print numbers_unique
    # for i in range(0,len(numbers_unique)-3):
    #     # [list_pairs.append([numbers_unique[j],numbers_unique[j+1]]) for j in range (i , len(numbers_unique)-2) if numbers_unique[j] + numbers_unique[j+1] == 0]
    #     for j in range(i+1, len(numbers_unique)):
    #         if (numbers_unique[i] + numbers_unique[j]) == 0:
    #             list_pairs.append([numbers_unique[i],numbers_unique[j]]) 

    # if 0 in numbers_unique:
    #     list_pairs.append([0,0])

    # return sorted(list_pairs)
    # use dictionnary : pair is key/ value is sum 

def sort_pairs(numbers):
    pass

def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    count = {}
    char_max = []
    phrase = phrase.strip()
    phrase = phrase.replace(" ", '')
    for char in phrase:
        count[char] = count.get(char, 0) + 1
    max_times_list = count.values()
    max_times = max(max_times_list)
    set_phrase = set(phrase)
    phrase = list(set_phrase)
    for char in phrase:
        if count[char] == max_times:
            char_max.append(char)
    return char_max



    # I am stuck from here.. I try finding functions to sort the dictionnary by values but was unsuccessful:
       # list1 = sorted(count,key= count.get)
    
    # I tried looking for the max items of the list but unsuccessful too as i am sure there is simpler:
    # lischar=[]
    # for items in count.items:
    #     for element in item:
    #         if m < element[1]
    #         m = element[1]
    #         list1.pop()
    #         listchar.append(element[0])
    #         elif m = element[1]
        # count_list = count.items()
        # max = count_list[0][1]
        # for pair in count_list:
        #     if  pair....
        # return count.values()
       

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
