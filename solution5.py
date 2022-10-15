def is_palindrome(word):
    if (len(word) < 2):
        return True
    else:
        last_letter = len(word) - 1
        if ( word[0] != word[last_letter] ):
            return False
        else:
            return is_palindrome(word[1:last_letter])

print(is_palindrome("racecar"))