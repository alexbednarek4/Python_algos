"""
iven an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

 

Note:

    A word is defined as a sequence of non-space characters.
    Input string may contain leading or trailing spaces. 
    However, your reversed string should not contain leading or trailing spaces.
    You need to reduce multiple spaces between two words to a single space in the reversed string.


"""

def reverseWords(str):
    # Need pointers for first 
    result = ''
    i = 0
    n = len(str)

    # Iterate through entire string with i
    while i < n:
        # if str[i] is a " ", iterate until we find a character
        while i < n and str[i] == " ":
            i+=1
        if i >= n:
            break
        # now that we've reached a char, create j pointer
        j = i+1
        while j < n and str[j] != " ":
            j+=1
        # Slice word at i and j exclusive
        word = str[i:j]

        # if result string is empty
        if len(result) == 0:
            result = word
        else:
            # Append in reverse order
            result = word + " " + result
        
        # And continue iterating to find other words in string
        i = j+1
    return result

print(reverseWords("  hello world!  "))