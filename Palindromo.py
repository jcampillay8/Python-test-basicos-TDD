# isPalindrome : escribe una función que verifique si la palabra dada es palíndrome (una palabra que se lee igual en ambos sentidos).
# Ejemplo: isPalindrome ("racecar") debería devolver True
# Prueba de ejemplo: afirmarEqual (isPalindrome ("racecar"), True) o afirmarTrue (isPalindrome ("racecar"))
# Prueba de ejemplo: afirmarFalse (isPalindrome ("rabcr")).
# Agregue al menos otros 5 casos de prueba

import unittest

def palindrome(s):
    if len(s) == 0: return False # empty string is False
    if len(s) < 2: return True
    
    L = 0
    R = len(s) - 1

    while(L < R):
        if s[L] != s[R]: return False
        L += 1
        R -= 1
    return True

def isPalindrome(s):
    '''Recursive palindrome'''
    print(s)
    if len(s) == 0: return False # empty string is False
    elif len(s) < 2: return True # 1 char left
    elif len(s) == 2 and s[0] == s[-1]: return True
    if s[0] != s[-1]: return False
    return isPalindrome(s[1:-1])



class TestPalindromes(unittest.TestCase):
    def test_racecar(self):
        self.assertTrue(palindrome("racecar"))
        self.assertTrue(isPalindrome("racecar"))
        
    def test_deed(self):
        self.assertTrue(palindrome("deed"))
        self.assertTrue(isPalindrome("deed"))
        
    def test_fair(self):
        self.assertFalse(palindrome("fair"))
        self.assertFalse(isPalindrome("fair"))
        
    def test_jakiro(self):
        self.assertFalse(palindrome("jakiro"))
        self.assertFalse(isPalindrome("jakiro"))

    def test_emptystring(self):
        self.assertFalse(palindrome(""))
        self.assertFalse(isPalindrome(""))
        
    def test_number(self):
        with self.assertRaises(TypeError):
            palindrome(1)
        with self.assertRaises(TypeError):
            isPalindrome(1)


if __name__ == '__main__':
    unittest.main()