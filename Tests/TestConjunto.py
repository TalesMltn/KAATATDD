import unittest
from src.Logica.Conjunto import Conjunto
class TestConjunto( unittest.TestCase):
    def test_conjunto_vacio_reptornaNone(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.promedio())
    def test_conjunto_vacio_reptornaNone(self):
        conjunto = Conjunto ([5])
        self.asserEqual
def test_conjunto_dosElementos_retornaPromedioElementos( self ):
conjunto=Conjunto([5,7])
self.assertEqual(6,conjunto.promedio())
def test_conjunto_dosElementos_retornaPromedioElementos( self ):
conjunto=Conjunto([5,7])
self.assertEqual(6,conjunto.promedio())