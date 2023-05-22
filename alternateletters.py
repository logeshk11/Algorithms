def mergeAlternately(word1, word2): # Takes 2 words as input and returns a single word which has alternate letters of
                                    #the two words
    n = len(word1)
    m = len(word2)
    s = ""
    i = 0
    j = 0
    while (i < n and j < m):
        s=s+word1[i]
        s=s+word2[j]
        i+=1
        j+=1
    if n==m :
        pass
    elif n<m:
        s=s+word2[i:]
    else:
        s=s+word1[i:]
    return s

print(mergeAlternately("logeshwiinnwe", "ku"))