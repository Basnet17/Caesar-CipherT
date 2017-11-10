'''
This program decodes the secret massage, the famous massage using the correct shift, we decipher the text in this program
Pritam Basnet
Project7.py
10th November 2017
Here the secret message decoded is the letter written by Abraham Lincoln to Mrs. Bixby on 21 November, 1864
'''

def multiSplit (str1,str2):
    '''
    This function implements a multiple split functionality.  String str1 is
    split into multiple pieces.  The individual characters in string str2 are
    used as the split points.  Each character is used individually.
    Parameters:
        str1 - a string that is to be split
        str2 - a string containing characters used to split string1
    Return Value:
        a list of strings from the splitting
    '''
    ret = [str1]                                 #initialises the ret with the first string
    for c in str2:                               #takes one character from str2 at a time for splitting
        temp = []
        for s in ret:                            #takes each character from the ret
            lst = s.split(c)                     #splits the strings from ret using character from str2
            for word in lst:
                if word != '':
                    temp.append(word)            #appends the strings in temp
        ret = temp                               #ret is set as temp at the end of the loop

    return ret

def decode(text,key):
    '''
    This function decodes the string text file from the ciphertext obtained by opening the file in main function
    Parameters:
        text: The string text file under the text file opened inside the main function
    Return:
        plaintext: The decoded string text using various key
    '''
    plaintext=''                                 #the empty string is assigned as plaintext
    for c in text:
        if ord(c) >=65 and ord(c) <=90:          #only the character with ord ranging from 65 to 90 are processed with decoding mathematics
            val = ord(c)-65
            val = (val - key)%26
            cc = chr(val + 65)                   #the character converts integer with specific letter and stroes in cc
            plaintext = plaintext+ cc
        else:
            plaintext = plaintext+ c             #the characters except those with ord ranging from 65 to 90 are processed and are kept as they are
    return plaintext

def makeConcordance (filename1):
    '''
    This function reads a text file and returns a dictionary concordance
    from that file. Concordance value is a list of line numbers where
    that word appears.
    Parameters:  filename (string)
    Return Value: concordance (dictionary)
    '''
    concor = {}
    f = open(filename1,'r')                     #opens up the file and reads it
    count = 0
    for line in f:
        count = count + 1
        temp = multiSplit(line,'.,:;!? \t\n()-_"\'')   #each line is splitted into different words using the Multisplit function
        for word in temp:                       #each word from temp is taken at one time
            word = word.upper()                 #all the words are changed into upper case
            if word in concor:
                concor[word].append(count)       #the words are appended in dictionary with their values
            else:
                concor[word] = [count]
    return concor
    f.close()
    
    
def hitRate(lisit, dicis):
    '''
    This function counts the percentage of the total characters of the list present in the dictionary
    Parameters:
        lisit: The list of strings splitted using the Multisplit function
        dicis: The concordance built under the dictionary.txt
    Return
        count: The total number of words present in the lisit which are in the dicis
    '''
    count = 0                               #firstly the counter is set 0
    for character in lisit:                 #for each character in lisit, the same list got by splitting plaintext from decode function 
        if character in dicis:              #if the word in lisit, the list got by splitting plaintext are in dicis(the concordance dictionary) then count is increased 1 each time
            count = count + 1
    return count
        
def main():
    #the txt file ciphertext.txt is opened and is read and the string is stored in text
    filename = 'ciphertext.txt'             
    g = open(filename,'r')
    text = g.read()
    #the txt file dictionary.txt is passed to the makeConcordance function to open it and make a new concor with dictionary.txt in it
    filename1 = 'dictionary.txt'
    dicis= makeConcordance(filename1)       #now the parameter of hitRate function, dicis is set as the return value from the function makeConcordance so dicis is dictionary containing words from dictionary.txt
    maxCount = 0
    for key in range(26):                   #as there are 26 unique keys the loop is set for 26 ranges
        call1 = decode(text,key)            #call1 is used as variable to store plaintext returned from decode function
        lisit = multiSplit(call1, '.,:;!? \t\n()-_"\'')       #lisit now stores the splitted words from call1 which contains plaintext from decode function
        call2 = hitRate(lisit, dicis)       #call2 is used as variable to store the count returned from hitRate function
        if call2 > maxCount:
            maxCount = call2                #when certain value is larger than previous value the larger value is stored as maxCount
            setkey = key                    #the key with highest maxCount value is stored in setkey it's 7 in our case
            print('The correct key is:',setkey)   #the key and the text related to key are printed
            print(decode(text,setkey))
    g.close()
    
main()
    
