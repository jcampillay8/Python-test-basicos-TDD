# monedas : escribe una función que determine cuántas monedas de 25 centavos, de 10 centavos, de 5 centavos y de 1 centavo le dará a un cliente para un cambio en el que minimice la cantidad de monedas que entrega.
# Ejemplo: dado 87 centavos, el resultado debe ser 3 cuartos, 1 centavo, 0 níquel y 2 centavos
# Prueba de ejemplo: afirmar Igual (moneda (87), [3,1,0,2])
# Agregue al menos otros 5 casos de prueba

import unittest

def change(x: int, coins: list):
    lista=[]
    resto= x
    for i in range(len(coins)):
        a = resto // coins[i]
        lista.append(a)
        resto = resto % coins[i]
    
    return lista

class TestChange(unittest.TestCase):

    # Tests for change function (no dynamic programming):
    def test_change_1(self):
        coins = [25,10,5,1]
        self.assertEqual(change(87,coins), [3,1,0,2]) 

    def test_change_2(self):
        coins = [25,10,5,1]
        self.assertEqual(change(100,coins), [4,0,0,0])
    
    def test_change_3(self):
        coins = [25,10,5,1]
        self.assertEqual(change(68,coins), [2,1,1,3])    


if __name__ == '__main__':
    unittest.main()
