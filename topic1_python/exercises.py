import doctest


def get_squares(n: int) -> list:
    """
    Generates and returns a list of squares of the numbers from 1 to n.

    :param n: Upper limit of list.
    :return: List of squared integers.

    >>> get_squares(6)
    [1, 4, 9, 16, 25, 36]
    """
    return [i**2 for i in range(1, n+1)]


def filter_even(l: list) -> list:
    """
    Filters even numbers in a list

    :param l: List of integers.
    :return: List of even elements in l.

    >>> filter_even([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
    [4, 16, 36, 64, 100]
    """
    return [i for i in l if i % 2 == 0]


def sum_even(l: list) -> int:
    """
    Calculates sum of the even numbers in a list.

    :param l: List of integers.
    :return: Sum of even elements in l.

    >>> sum_even([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
    220
    """

    return sum(filter_even(l))


def filter_less_than_n(l: list, n: int) -> list:
    """
    Filters elements of a list of numbers which are less than a given integer
    number.

    :param l: Input list.
    :param n: Integer number.
    :return: Filtered list.

    >>> filter_less_than_n([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 5)
    [1, 1, 2, 3]
    """
    return [i for i in l if i<n]


def remove_duplicates(l: list) -> list:
    """
    Returns a list with all elements of the input list without duplicates.

    :param l: Input list.
    :return: List of all elements of l list without duplicates.

    >>> remove_duplicates([1, 1, 2, 3, 5])
    [1, 2, 3, 5]
    """
    return list(set(l))


def common_elements(l1: list, l2: list) -> list:
    """
    Returns all common elements of two lists without duplicates - in the order
    of appearance in l1.

    :param l1: First list.
    :param l2: Second list.
    :return: List of common elements.

    >>> common_elements([1, 2, 3, 5, 8, 21], [1, 2, 3, 7, 8, 9])
    [1, 2, 3, 8]
    """
    if len(l1)>len(l2):
        return [i for i in l1 if i in l2]
    else:
        return [i for i in l2 if i in l1]


def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    """
    Merges two dictionaries, where values of overlapping keys are summed, e.g.,
    for {'a': 5, 'b': 3} and {'b': 2, 'c': 1}, the result should be
    {'a': 5, 'b': 5, 'c': 1}.

    :param dict1: First dictionary.
    :param dict2: Second dictionary.
    :return: Merged dictionary.

    >>> merge_dictionaries({'a': 5, 'b': 3}, {'b': 2, 'c': 1})
    {'a': 5, 'b': 5, 'c': 1}
    """
    merged=dict1
    for key, value in dict2.items():
        if key in merged.keys():
            merged[key]+=value
        else:
            merged[key]=value

    return merged


def first_and_last(l: list) -> tuple:
    """
    Returns the first and last element of a list.

    :param l: Non-empty list.
    :return: Tuple with first and last element of l.

    >>> first_and_last([1, 2, 3])
    (1, 3)
    """
    return (l[0], l[-1])


def fibonacci(n: int) -> int:
    """
    Return the n-th Fibonacci number. The Fibonacci numbers are defined as:
        - f(1) = 1
        - f(2) = 1
        - f(n) = f(n - 1) + f(n - 2) for n > 2

    :param n: Positive integer.
    :return: n-th Fibonacci number.

    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(7)
    13
    """
    if n<1:
        raise ValueError
    if n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        return 1


def reverse_word_order(text: str) -> str:
    """
    Reverses the word order in a string of words.

    :param text: String with words.
    :return: String with words (separated by blanks) of text reversed.

    >>> reverse_word_order('hello world')
    'world hello'
    """
    return " ".join(reversed(text.split(" ")))


def count_vowels(text: str) -> int:
    """
    Counts vowels (a, e, i, o, u) in a given string

    :param text: Text to check as string.
    :return: Number of vowels in text.

    >>> count_vowels('hello world')
    3
    """
    i=0
    for l in text:
        if l in ["a", "e", "i", "o", "u"]:
            i+=1
    return i


def check_palindrome(word: str) -> bool:
    """
    Checks if a given word is a palindrome (reads the same forwards as
    backwards).

    :param word: Word to check as string.
    :return: True if the word is a palindrome, else False.

    >>> check_palindrome("hello")
    False
    >>> check_palindrome("racecar")
    True
    """
    if len(word)<=1:
        return True
    if word[0]!=word[-1]:
        return False
    else:
        return check_palindrome(word[1:-1])


if __name__ == '__main__':
    doctest.testmod(verbose=True)
