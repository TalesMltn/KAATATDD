import unittest
from src.Logica.Conjunto import Conjunto
class TestConjunto( unittest.TestCase):
    def test_conjunto_vacio_reptornaNone(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.promedio())
    def test_conjunto_vacio_reptornaNone(self):
        conjunto = Conjunto ([5])
        self.asserEqual
