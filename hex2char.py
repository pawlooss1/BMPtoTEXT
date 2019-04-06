
# coding: utf-8

# In[7]:


import numpy as np
import re
import sys, os
import reading_bmp_file as read


# In[9]:


#function to convert number to char
def num2char(numArray):
    [r1, r2, r3, r4, r5, r6, r7] = [np.array([range(0,37)]), np.array([range(37,74)]), np.array([range(74,111)]),
                            np.array([range(111,147)]), np.array([range(147,184)]), np.array([range(184,220)]),
                            np.array([range(220,256)])]
    charArray = [' ', ',', '-', ':', '+', '$', '#']
    fullArrayStrNeg = ""
    fullArrayStrPos = ""
    for i in numArray:
        for j in i:
            if j in r1:
                fullArrayStrNeg += charArray[0]
                fullArrayStrPos += charArray[6]
            elif j in r2:
                fullArrayStrNeg += charArray[1]
                fullArrayStrPos += charArray[5]
            elif j in r3:
                fullArrayStrNeg += charArray[2]
                fullArrayStrPos += charArray[4]
            elif j in r4:
                fullArrayStrNeg += charArray[3]
                fullArrayStrPos += charArray[3]
            elif j in r5:
                fullArrayStrNeg += charArray[4]
                fullArrayStrPos += charArray[2]
            elif j in r6:
                fullArrayStrNeg += charArray[5]
                fullArrayStrPos += charArray[1]
            else:
                fullArrayStrNeg += charArray[6]
                fullArrayStrPos += charArray[0]
        fullArrayStrNeg += '\n'
        fullArrayStrPos += '\n'
    return fullArrayStrNeg, fullArrayStrPos


# In[10]:


def write2file(charArrayNeg, charArrayPos):
    finalFileNeg = open("finalFileNeg.txt","w")
    finalFileNeg.write(charArrayNeg)
    finalFilePos = open("finalFilePos.txt","w")
    finalFilePos.write(charArrayPos)


# In[5]:


#getting argument (numpy array)
args = sys.argv
#print(args)
if len(args) == 2:
    if os.path.isfile(args[1]):
        hexArray = read.image_to_array(args[1])
        charArrNeg, charArrPos = num2char(hexArray)
        write2file(charArrNeg, charArrPos)
    else:
        print("Can't find this image, sorry.")
else:
    print("Wrong number of arguments")

