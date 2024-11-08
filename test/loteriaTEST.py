import unittest
from src.modulo import generar_numeros_aleatorios, comparar_resultados

class TestLoteria(unittest.TestCase):

    def test_generar_numeros_aleatorios(self):
        # Comprobar que la lista tiene 5 números únicos entre 1 y 50
        numeros = generar_numeros_aleatorios()
        self.assertEqual(len(numeros), 5)
        self.assertTrue(all(1 <= num <= 50 for num in numeros))
        self.assertEqual(len(set(numeros)), 5)  # Verificar que no haya números repetidos

    def test_comparar_resultados(self):
        # Caso donde hay 3 números acertados
        numeros_usuario = [5, 12, 18, 23, 30]
        numeros_sorteo = [2, 12, 18, 45, 30]
        acertados, numeros_acertados = comparar_resultados(numeros_usuario, numeros_sorteo)
        self.assertEqual(acertados, 3)
        self.assertEqual(numeros_acertados, {12, 18, 30})

        # Caso donde no hay números acertados
        numeros_usuario = [1, 2, 3, 4, 5]
        numeros_sorteo = [6, 7, 8, 9, 10]
        acertados, numeros_acertados = comparar_resultados(numeros_usuario, numeros_sorteo)
        self.assertEqual(acertados, 0)
        self.assertEqual(numeros_acertados, set())

        # Caso donde el usuario acierta todos los números
        numeros_usuario = [1, 2, 3, 4, 5]
        numeros_sorteo = [1, 2, 3, 4, 5]
        acertados, numeros_acertados = comparar_resultados(numeros_usuario, numeros_sorteo)
        self.assertEqual(acertados, 5)
        self.assertEqual(numeros_acertados, {1, 2, 3, 4, 5})

if __name__ == '__main__':
    unittest.main()
