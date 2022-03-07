'''

Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?

1. Is ASCCI or UNICODE string?

A) One solution is to create an array of boolean values, where the flag at index i indicates whether character
    i in the alphabet is contained in the string. The second time you see this character you can immediately
    return false.
    We can also immediately return false if the string length exceeds the number of unique characters in the
    alphabet. After all, you can't form a string of 280 unique characters out of a 128-character alphabet.
    
    >> I It's also okay to assume 256 characters. This would be the case in extended ASCII. You should
        clarify your assumptions with your interviewer.

Time Complexicity: O(n) -> n -> length of the string
Space Complexicity: O(1) -> foor loop will never iterate through more than 128 characters.
'''


def isUniqueChars(str):  
    char_set = [False] *128  
    if len(str) > 128:
        return False
    for i in str:
        index = ord(i) # ASCCI value for  the char              
        if char_set[index]: #already found this char in string
            return False
        char_set[index] = True   
    return True;

print(isUniqueChars('ANE'))