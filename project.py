#%% Project Option 1: Morse Code
#Question 1: How would you model the various parts of the process?
'''
The whole program consists of 2 main components that would need to be modelled 
or implemented:
    - Encryption by looking up the dictionary for Morse Code and translate it 
    accordingly as
    as well as return a set of untranslable characters
    - Decryption by looking uo the dictionary for Morse Code and translating it
    into English
Both function that conducts the encryption and decryption process will contains
loop functions in order to go through individual characters within the string 
in order to search up the characters within the dictionary. If that is not the
it can be assumed that the character that is not within the dictionary is a 
' ' or space which will also be added into the decrypted or encrypted message.
The loops for going through each individual letter can be viewed mathematically
as list or set where we are acessing the character in its given range.  
This process is applied by using a series of if-else statement based on boolean
condition which is either 'True' or 'False'. The condition can also be a 
combination of operators such as 'and', 'or' to access the condition.

The original message will be store in a separate variable which is different 
from the variable that store decrypted or encrypted message. By each
time going through each characters, the individual character will be added to 
the new variable that contains the decrypted or encrypted message.

The difficult problem of this program is that while returning an encoded 
message you will also have to return a set of untranslable characters.
Effectively, the solution that have been applied to solve this is first to 
convert the string into a list that each index place within the list contain a
single character or element of the string. Applying the technique of functional
decomposition within programming, we can implement encrypt() function by 
building other functions that can be used or call within encrypt()

The first function that need to be build is a function that will filter out 
untranslable characters from the original message during this process, the 
function will also need to turn the message into uppercase version. The message
within the function will be first converted into an array version via 
string_to_array() function which take the input of a string message and return
a list that contain individual string characters. Next the 
serach_for_untranslable() function contain a loop that will repeatedly cycle 
through each position within the list (using a 'for' loop). Then each elements
will be assess using a conditon statement which essentially will add using the 
append() function to add element that is true to the condition (either be
within the morse code dictionary or a space) to a new list that contain 
translable letters. At the end of the function, the list will then be turn into 
again using built-in ''.join() function. Meanwhile, if the element within the 
list does not satisfy the condition will then be added to a separate defined 
set that hold untranslable characters using the built-in add() function. The
search_for_untranslable() function take an unfiltered string that can be either 
in uppercase or lowercase and return a filtered all uppercase letters string 
and a set that contains untranslable characters or symbols. 
'''
'''
Explain and justify your choice of test cases in this documentation comment.
You may wish to define multiple lists of test cases for different components
of your (anticipated) solution.
All expected results are supplied with respect to the test cases

test cases for string_to_array() function:
    'hello': this is to test whether the function can convert a single string
    word that has a combination of capitalised letter and number. The function
    should be able to separate each individual character into different separate
    element is different position.
    '234 TH1RE & ': This is to see whehther the function can also convert ' ' 
    or space into an element of the list that holds individuals characters of 
    the string.
    '': this is to see whether the function can correct an empyty input into an
    empty list or not
    
test cases for search_for_untranslable():
    'h  i,, th123Aer%e!': the purpose of this test case is to see whether the 
    function can interpret double space '  ' or not. It also is to test whether
    the function can put items that does not belong to the dictionary into a set
    which is not allowing repetition of elements or not.
    
test cases for encrypt():
    'hiuDn': this is to see whether the function can simply translate a single 
    word with combination of non-capitalised and capitalised letter or not.
    '234  TH,1R,E & ': this is to see whether the function can process the ' '
    or space correctly or not, which it should be able to give space accordingly
    similar to the original text. it is also to see how it would response to 
    untranslable characters.
    '!!!': this is to see whether the function can return an empty string as 
    well as a set that has a single '!' or not
    
test cases for decrypt():
    '.... .. ..- -.. -. ': this is to see whether the function can properly 
    progress a morsecode with a space at the end or not. It should be abloe to 
    return a string with a space last.
    '..--- ...-- ....-   - .... .---- .-. .': This is to see whether the 
    function can work properly with double '' or not.

'''

#define some test cases here

#test case for string_to_array()
string_to_array_test = { 
    'hEl1o',
    '234 TH1RE & ',
    
}
'''
string_to_array_result = ['h', 'E', 'l', '1', 'o'],
                          ['2', '3', '4', ' ', 'T', 'H', '1', 'R', 'E', ' ', '&', ' '],
                          []
'''                      

search_for_untranslable_test = {'h  i,, th123Aer%e!'
    }
'''
search_for_untranslable_result = {('H  I TH123AERE', {'!', '%', ','}),
    }
'''
encrypt_test = { 
    'hiuDn',
    '234  TH,1R,E & ',
    '!!!'
}
'''
encrypt_test_result = {('.... .. ..- -.. -. ', set()),
                       ('..--- ...-- ....-   - .... .---- .-. .   ', {'&', ','}),
                       ('', {'!'})
    }
'''
decrypt_test = { 
    '.... .. ..- -.. -. ',
    '..--- ...-- ....-   - .... .---- .-. .'
}
decrypt_result ={
    'HIUDN ',
    '234 TH1RE'
    }
#dictionary of morse code translation 
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
#Function to turn the string message into an array
def string_to_array(message):
    arr = list(message)
    return arr
 
#Function to find the untranslable element within the array    
def search_for_untranslable(message):
    #turn the message into uppercase characters
    upper_message = message.upper()
    
    #create a list that contain the letters of the message as individual elements
    arr_message =string_to_array(upper_message)
    
    #length of the list
    length = len(arr_message)
    
    #create an empty list that will hold translable characters
    translable_array = []
    
    #create an empty set that will hold untranslable characters
    untranslable_set = set()
    
    #a translabe string of word that have been filtered
    translable_string = None
    
    #the for loop to go through 
    for i in range(length):
        if arr_message[i] in MORSE_CODE_DICT or arr_message[i]==' ':
            translable_string= translable_array.append(arr_message[i])
        else: 
            untranslable_set.add(arr_message[i])
    translable_string = ''.join(translable_array)
    return translable_string, untranslable_set

# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    cipher_text = ''
    upper_message, untranslable_set = search_for_untranslable(message)
    
    for letter in upper_message:
        if letter != ' ':
            cipher_text += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher_text += ' '
    return cipher_text, untranslable_set
 
# Function to decrypt the string
# from morse to english
def decrypt(encoded_message):
 
    # extra space added at the end to access the
    # last morse code
    encoded_message += ' '
 
    text_decipher = ''
    cit_text = ''
    for element in encoded_message:
        if (element != ' '):
            count = 0
            cit_text += element

        else:
            count += 1
            if count == 2 :
                text_decipher += ' '
            else:
                text_decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(cit_text)]
                cit_text = ''
 
    return text_decipher
