'''
International Morse Code defines a standard encoding where each letter 
is mapped to a series of dots and dashes, as follows: "a" maps to ".-", 
"b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet 
is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..",
"--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.
--","--.."]
Now, given a list of words, each word can be written as a concatenation of 
the Morse code of each letter. For example, "cba" can be written as 
"-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). 
We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
'''

def unique_morse_code(words):
    morse = set()

    mappings = [".-","-...","-.-.","-..",".","..-.","--.","....",
    "..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
    "...","-","..-","...-",".--","-..-","-.--","--.."]

    alphabet = ord('a')
    mappings_start = 0
    morse_map = dict()
    
    for word in mappings:
        morse_map[alphabet] = mappings[mappings_start]
        mappings_start += 1
        alphabet += 1

    for word in words:
        morse_word = []
        for char in word:
            morse_word.append(morse_map[ord(char)])
        morse.add(''.join(morse_word))

    return len(morse)

