def is_palindrome(word: str) -> bool:
    word = word.replace(" ", "").lower()
    return word == word[::-1]
print(is_palindrome("kajak"))
print(is_palindrome("anna"))
print(is_palindrome("pies"))
print(is_palindrome("kobyła ma mały bok"))