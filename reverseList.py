#1 reverseList : escribe una función que invierta los valores en la lista (sin crear una matriz temporal).
# Ejemplo: reverseList ([1,3,5]) debería devolver [5,3,1]
# Prueba de ejemplo: afirmarEqual (reverseList ([1,3,5]), [5,3,1])
# Agregue al menos otros 3 casos de prueba
import unittest

def reverseArray(list):
    # pass
    for i in range(int(len(list)/2)):
        list[i], list[len(list)-i-1] = list[len(list)-i-1], list[i]
    return list

class reverseArrayTests(unittest.TestCase):
    
    def testOne(self):
        self.assertEqual(reverseArray([1,3,5]),[5,3,1])

    def testtwo(self):
        self.assertEqual(reverseArray([5,3,1]),[1,3,5])
    
    def testhree(self):
        self.assertEqual(([5,3,1]),[5,3,1])

if __name__=='__main__':
    unittest.main() #esto ejecuta nuestras pruebas