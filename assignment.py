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


def count_repeated_characters(s):
    # Dictionary to store the frequency of each character
    freq = {}
    
    # Count the frequency of each character in the string
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    # Count the number of characters that appear more than once
    repeated_count = sum(1 for count in freq.values() if count > 1)
    
    return repeated_count

# Example usage:
s = "hello"
result = count_repeated_characters(s)
print(result)  
s = "aeiou"
print(result)  

"""Returns the number of repeated characters in a string.
    >>> count_repeats("hello")
    2
    >>> count_repeats("aeiou")
    0
    """
 


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
