def palindrome (word):
    for i in range (0,len(word)-1):
        if word [i]!= word[len(word)-1-i]:
            return False 
    return True
print(palindrome("kajak"))
print(palindrome("anna"))
print(palindrome("rower"))
