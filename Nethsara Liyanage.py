from functools import reduce
from re import T
from numpy import *
import string
import numpy as np
import itertools

#alphabet dictionary
alpha=['a','b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' , 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#get the distance of two letters
def distance(letter1, letter2):
    
    return np.abs((alpha.index(letter2)+1)%26 - (alpha.index(letter1)+1)%26)

#function test
# print(distance('z', 'a'))


#get the total distance of two strings
def totalDistance(string1, string2):
    ans = 0
    for x in range(len(string1)):
        ans += distance(string1[x], string2[x])

    return ans

#function test
# print(totalDistance('bd', 'za'))


#get all the possible strings
def possibleStrings(str1, k):

    arr3 = []

    for j in range(k):
        arr1 = [alpha.index(str1[j]), alpha.index(str1[j])]
        arr2 = [str1[j]]
            
        for i in range(k):
            # arr1.append(alpha.index(st1[i]))
            arr2.append(alpha[arr1[i]-(i+1)])
            arr2.append(alpha[arr1[i]+(i+1)])

        arr3.append(arr2)

    # print(arr3[0])
    possibleOutputs =[]

    #get the possible output strings
    for x,y in itertools.product(arr3[0],arr3[1]):
        possibleOutputs.append(x+y)

    # print(possibleOutputs)
    return possibleOutputs


#check the totDistance value of strings is less than or evel to the given K value
def checkWithKVal(stringArr, str1,  k):
    stringArr2 = []
    for m in range(len(stringArr)):
        totDistance = totalDistance(str1, stringArr[m])

        if(totDistance <= k):
            stringArr2.append(stringArr[m])

    return stringArr2

# function test
# stringArr = ['xa', 'bd', 'ac','fe', 'dd', 'bf']
# print(checkWithKVal(stringArr, 'bd', 2))



#sort the string array to the Lexicographic order
def sortLexo(stringArr):

    stringArr.sort()
    
    return stringArr[0]

# function test
# stringArr = ['xa', 'bd', 'ac','fe']
# print(sortLexo(stringArr))


# main function - getSmallestString
def getSmallestString(str,k):
    # print('Function Called')

    lower = str.islower()

    if(lower):
        if (len(str) >= 1 and len(str) <= 1000000):

            if (k >= 0 and k <= 1000000000):
                stringArr = possibleStrings(str, k)

                stringsAccordingToK = checkWithKVal(stringArr, str, k)
                
                returnStr = sortLexo(stringsAccordingToK)

                return returnStr
                
            else: 
                # print("K value issue occured!")
                return "K value issue occured!"
        else: 
            # print("String length issue occured!")
            return "String length issue occured!"
    else: 
        # print("String length issue occured!")
        return "String is not in lower case!"



# #test 01
print('Test 01 - ', getSmallestString('bd', 2))
assert getSmallestString('bd', 2) == 'ac', "should be 'ac'"

# #test 02
# print('Test 02 - ', getSmallestString('bd', -1))
# assert getSmallestString('bd', -1) == 'K value issue occured!', "should be 'K value issue occured!'"

# #test 03
# print('Test 03 - ', getSmallestString('bd', 1000000001))
# assert getSmallestString('bd', 1000000001) == 'K value issue occured!', "should be 'K value issue occured!'"

# #test 04
# print('Test 04 - ', getSmallestString('BD', 2))
# assert getSmallestString('BD', 2) == 'String is not in lower case!', "should be 'String is not in lower case!'"
