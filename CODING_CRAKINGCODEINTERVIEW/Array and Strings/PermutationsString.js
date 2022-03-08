/*
Check Permutation: Given two strings,write a method to decide if one is a permutation of the
other.
Check Permutation. Given two string, write a method to decide if one is a permutation of the other.
Sort the Strings
*/

function sorted(str) {     
    return  str.split('').sort().join('') 
}
function permutation(s, t) {
    if( s.length != t.length)
        return false;      
    return sorted(s) === sorted(t)
}

console.log(permutation('doA','Sod'))

/*
Check if the two strings have identical character counts.
We can also use the definition of a permutation-two words with the same character counts-to implement
this algorithm. We simply iterate through this code, counting how many times each character appears.
Then, afterwards, we compare the two arrays.
*/

function permutation2(s, t){
    if( s.length != t.length)
        return false        

    let letters = [0];   
    let s_array = s.split('')     
    console.log('s_array:'+s_array)
    for(let i =0; i<s_array.length; i++){
        letters[i]++;
    }
    console.log('letters:'+letters)

    for(let i =0; i<t.length; i++){
        let c = t.charAt(i)        
        console.log('letters:'+letters)
        letters[c] = letters[c] - 1
        if(letters[c] < 0){
            return false
        }
    }
    return true


}
console.log(permutation2('doA','Sod'))