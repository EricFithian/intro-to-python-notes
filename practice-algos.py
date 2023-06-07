'''
*******************************************************************************
Write a function even_range(start, end) that returns an list containing all even
numbers between 'start' and 'end' in sequential order.
Examples:
even_range(13, 20) => [ 14, 16, 18, 20 ]
even_range(4, 11) => [ 4, 6, 8, 10 ]
even_range(8, 5) => []
*******************************************************************************/
'''

def even_range(start, end):
    # # I want to iterate through from the start to the end, inclusive of both, and add to an array (or list) that I create (I'll call it even_numbers) and then return that array
    # even_numbers = []
    # while start <= end:
    #     if start % 2 == 0:
    #         # This will run if start is even. 
    #         even_numbers.append(start)
    #     # Increment start by 1 but inside of the while loop not the if condition
    #     start += 1
    # return even_numbers
    # for num in range(start, end + 1):
    #     if num % 2 == 0:
    #         even_numbers.append(num)
    # return even_numbers
    return [num for num in range(start, end + 1) if num % 2 == 0]


print(even_range(13, 20))
print(even_range(4, 11))
print(even_range(8, 5))

'''
*******************************************************************************
Write a function phrase_finder(words, phrase), that takes in an list of words and a
string representing a phrase. The function should return True if the phrase can be
formed by a pair of words from the list. The function should return False if the
phrase cannot be formed by any pair of words.

Examples:

phrase_finder(['world', 'prep', 'hello', 'bootcamp'], 'bootcamp prep') => True
phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'bootcamp prep') => True
phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello world') => True
phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello prep') => True
phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello goodbye') => False
*******************************************************************************/
'''

def phrase_finder(words, phrase):
    # phrase_words = phrase.split(' ')
    # print(phrase_words)
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if words[i] + ' ' + words[j] == phrase or words[j] + ' ' + words[i] == phrase:
                return True
    return False

print(phrase_finder(['world', 'prep', 'hello', 'bootcamp'], 'bootcamp prep'))
print(phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'bootcamp prep'))
print(phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello world')) 
print(phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello prep'))
print(phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello goodbye'))

'''
-----------------------------------------------------------------
Prompt:

In information theory, the hamming distance refers to the count of the differences between two strings of equal length.  It is used in computer science for such things as implementing 'fuzzy search'  capability.

- Write a function named hammingDistance that accepts two arguments which are both strings of equal length.
- The function should return the count of the symbols (characters, numbers, etc.) at the same position within each string that are different.
- If the strings are not of the same length, the function should return float('nan'). Note: There is no native not a number type, but it can be cast through float() or imported from the python math library. 

Examples:

hamming_distance('abc', 'abc'); //=> 0
hamming_distance('a1c', 'a2c'); //=> 1
hamming_distance('!!!!', '****'); //=> 4
hamming_distance('abc', 'ab'); //=> NaN

-----------------------------------------------------------------*/

'''

def hamming_distance(word1, word2):
    differences = 0
    if len(word1) != len(word2):
        return 'NaN'
    # for idx in range(len(word1)):
    #     if word1[idx] != word2[idx]:
    #         differences += 1
    # print(enumerate(word1))
    for idx, letter in enumerate(word1):
        if letter != word2[idx]:
            differences += 1
    return differences

print(hamming_distance('abc', 'abc'))
print(hamming_distance('a1c', 'a2c'))
print(hamming_distance('!!!!', '****'))
print(hamming_distance('abc', 'ab'))