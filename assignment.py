# Question 1

# Write a function that prints "Fizz" when the number is divisible by 3, "Buzz" when the number is divisible by 5
# and "FizzBuzz" when the number is divisible by both 3 and 5.
# If the number is not divisible by either 3 or 5, the function should return the number itself.


def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
    return
fizz_buzz(3)
fizz_buzz(5)
fizz_buzz(15)


"""Returns Fizz if number is divisible by 3, Buzz if divisible by 5, FizzBuzz if divisible by both 3 and 5.
    If not divisible by either 3 or 5, returns the number itself.
    >>> fizz_buzz(3)
    'Fizz'
    >>> fizz_buzz(5)
    'Buzz'
    >>> fizz_buzz(15)
    'FizzBuzz'
    """



# Question 2

# Write a function that takes a list of numbers and returns the sum of the squares of all the numbers.


def sum_of_squares(numbers):
    """Returns the sum of the squares of all the numbers in a list.
    >>> sum_of_squares([1, 2, 3])
    14
    >>> sum_of_squares([2, 4, 6])
    56
    """
    
    return sum([x**2 for x in numbers])

numbers=[1, 2, 3]
result=sum_of_squares(numbers)
print(result)
    
numbers=[2, 4, 6]
print(result)



# Question 3

# Write a function that counts the number of vowels in a string.


def count_vowels(s):
    vowels = "aeiouAEIOU"  # Include both lowercase and uppercase vowels
    count = 0
    
    for char in s:
        if char in vowels:
            count += 1
    
    return count
s = "hello"
result = count_vowels(s)
print(result)

s = "aeiou"
print(result)

"""Returns the number of vowels in a string.
    >>> count_vowels("hello")
    2
    >>> count_vowels("aeiou")
    5
    """
 


# Question 4

# Write a function that counts the number of repeated characters in a string.


def count_repeats(s):
    """
    Finds the character with the highest number of repetitions in the input string
    and returns the count of its repetitions, or 0 if no character is repeated.

    Args:
        s (str): The input string.

    Returns:
        int: The highest number of repetitions for any character, or 0 if no repeats.
    """
    from collections import Counter

    # Count the occurrences of each character
    char_count = Counter(s)

    # Find the maximum count of any character that is repeated
    max_repeats = max((count for count in char_count.values() if count > 1), default=0)

    return max_repeats

# Examples
print(count_repeats("hello"))  # Output: 2
print(count_repeats("aeiou"))  # Output: 0




"""Returns the number of repeated characters in a string.
    >>> count_repeats("hello")
    2
    >>> count_repeats("aeiou")
    0
    """
 


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

