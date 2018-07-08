# Python program to check if two strings are isomorphic
MAX_CHARS = 256

f = open('dictionary.lst', 'r')
data = f.read().lower()
#print(data)
f.close()
a = data.split()
count = {}
d = {}
# Isomorphic function
def areIsomorphic(string1, string2):
    m = len(string1)
    n = len(string2)
 
    # Length of both strings must be same for one to one
    # corresponance
    if m != n:
        return False
 
    # To mark visited characters in str2
    marked = [False] * MAX_CHARS
 
    # To store mapping of every character from str1 to
    # that of str2. Initialize all entries of map as -1
    map = [-1] * MAX_CHARS
 
    # Process all characters one by one
    for i in range(n):
 
        # if current character of str1 is seen first
        # time in it.
        if map[ord(string1[i])] == -1:
 
            # if current character of st2 is already
            # seen, one to one mapping not possible
            if marked[ord(string2[i])] == True:
                return False
 
            # Mark current character of str2 as visited
            marked[ord(string2[i])] = True
 
            # Store mapping of current characters
            map[ord(string1[i])] = string2[i]
 
        # If this is not first appearance of current
        # character in str1, then check if previous
        # appearance mapped to same character of str2
        elif map[ord(string1[i])] != string2[i]:
            return False
 
    return True

print("Please provide the message to be decrypted:")
w = input().split()
freqs = {}
for line in w:
    for char in line:
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1
#print(len(freqs))
b = " ".join(w) 
while(len(d)!=len(freqs)):
    for word in w:
        count[word]=0
        for wor in a:
            if areIsomorphic(word,wor):
                gue = 0
                for i in range(len(wor)):
                    if (word[i] in d and d[word[i]]!=wor[i]):
                        gue = 1
                if gue==0:
                    count[word]+=1
                    cor = wor
                
        if count[word] ==1:
            for i in range(len(word)):
                d[word[i]]=cor[i]
            w.remove(word)
            count.pop(word)
        #print(len(d))
d[' ']=' '
#print(len(d))
x = []
for i in range(len(b)):
    x.append(d[b[i]])
print("Decrypted result:"+"".join(x))
