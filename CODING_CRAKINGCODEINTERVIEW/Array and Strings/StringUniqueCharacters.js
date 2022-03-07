/*
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

*/
function isUniqueChars(str) {
    var char_set = [];
    for (var i = 0; i < str.length; i++) {
      var char = str.charAt(i);      
      if (char_set[char]) {
        return false;
      }    
      char_set[char] = true;
    }
    return true;
  }
  
  var string = "ANA";
  console.log(isUniqueChars(string));
  