'''
Check Permutation: Given two strings,write a method to decide if one is a permutation of the
other.
Check Permutation. Given two string, write a method to decide if one is a permutation of the other.
Sort the Strings
 '''

def sort(str):
    content = str
    content.sort()
    return ''.join(content)

def permutation(s, t ):
    if len(s) != len(t):
        return False;   
    return sorted(s) == sorted(t)
print(permutation('doS','Sod'))
#-----------------------------------------

def permutation2(s1, s2):
    if len(s1) != len(s2): 
        return False
    return ' '.join(sorted(s1)) == ' '.join(sorted(s2))
print(permutation2('doS','Sod'))
