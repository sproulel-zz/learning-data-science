anagramList = ['dog','god','cat']



     
anagramDict = {}


for word in anagramList:
    string = ''.join(sorted(word)) #sorts the string
    if string not in anagramDict: #checks to see if the string is in the dictionary
        anagramDict[string] = []
        anagramDict[string].append(word)
        
    else:
        anagramDict[string].append(word)  #appends the word into the dictionary 



for anagram in anagramDict.values(): 
    if len(anagram) >= 2:             #checks to see if there are multiple entries in the dictionary
        print (anagram)               #prints the words that are anagrams of each other



