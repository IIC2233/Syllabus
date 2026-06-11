import random
from unittest import TestCase
from busqueda import buscar_dfs, buscar_bfs
from laberinto import Laberinto
from unittest.mock import patch
from estadisticas import Experimento, correr_experimento, normalizar_datos
import pandas as pd

class VerificarDFS(TestCase):

    def setUp(self):
        """
        Se ejecuta antes de cada test
        """
        random.seed(10)
        self.laberinto = Laberinto(50, 50)
        self.inicio = self.laberinto.obtener_celda(49, 0)
        self.fin = self.laberinto.obtener_celda(0, 49)

    def test_dfs_encuentra_camino(self):
        """
        Encuentra la solucion
        """
        camino, _ = buscar_dfs(self.inicio, self.fin)

        # Largo es mayor o igual a 9
        self.assertGreaterEqual(len(camino), 9)

        # Comienza con inicio y termina con fin
        self.assertEqual(self.inicio, camino[0])
        self.assertEqual(self.fin, camino[-1])

        # Las celdas del camino estan conectadas
        for i in range(len(camino) - 1):
            self.assertIn(camino[i + 1], camino[i].conexiones)

        # Las celdas no se repiten en la ruta
        self.assertEqual(len(camino), len(set(camino)))

    def test_ordenar_conexiones(self):
        """
        Testea que se llame a ordenar conexiones cuando se busca
        con ordenar_conexiones = True y que no se llame cuando
        es false
        """
        with patch.object(
            self.inicio,
            "conexiones_ordenadas",
            wraps=self.inicio.conexiones_ordenadas,
        ) as mock_sort:
            buscar_dfs(
                self.inicio,
                self.fin,
                ordernar_conexiones=True,
            )
            mock_sort.assert_called()

        with patch.object(
            self.inicio,
            "conexiones_ordenadas",
            wraps=self.inicio.conexiones_ordenadas,
        ) as mock_sort:
            buscar_dfs(
                self.inicio,
                self.fin,
                ordernar_conexiones=False,
            )
            mock_sort.assert_not_called()


class VerificarBFS(TestCase):

    def setUp(self):
        """
        Se ejecuta antes de cada test
        """
        random.seed(20)
        self.laberinto = Laberinto(10, 10)
        self.inicio = self.laberinto.grilla[9][0]
        self.fin = self.laberinto.grilla[0][9]

    def test_bfs_encuentra_camino_mas_corto_o_igual_que_dfs(self):
        """
        Encuentra la solucion optima
        """
        camino_dfs, _ = buscar_dfs(self.inicio, self.fin)
        camino_bfs, _ = buscar_bfs(self.inicio, self.fin)

        # Entre 9 y el largo de dfs
        self.assertGreaterEqual(len(camino_dfs), len(camino_bfs))
        self.assertGreaterEqual(len(camino_bfs), 9)

        # Comienza con inicio y termina con fin
        self.assertEqual(self.inicio, camino_bfs[0])
        self.assertEqual(self.fin, camino_bfs[-1])

        # Las celdas del camino estan conectadas
        for i in range(len(camino_bfs) - 1):
            self.assertIn(camino_bfs[i + 1], camino_bfs[i].conexiones)

        # Las celdas no se repiten en la ruta
        self.assertEqual(len(camino_bfs), len(set(camino_bfs)))


class VerificarEstadisticas(TestCase):
    """
    Testea las funciones correr_experimento y normalizar datos
    """

    def setUp(self):
        self.alto = 20
        self.ancho = 20
        self.redundancia = 0
        self.redundancias = [0, 0.1, 0.3, 0.6]
        self.repeticiones = 5

    def test_correr_experimento(self):
        """
        Verifica que el método llama a las funciones correspondientes
        y retorne los resultados esperados
        """
        experimento = Experimento(
            self.alto,
            self.ancho,
            self.redundancia,
            self.repeticiones
        )

        with patch(
            "estadisticas.buscar_dfs",
            wraps=buscar_dfs,
        ) as mock_dfs, patch(
            "estadisticas.buscar_bfs",
            wraps=buscar_bfs,
        ) as mock_bfs:
            
            df = correr_experimento(experimento)
            
            self.assertEqual(
                mock_dfs.call_count,
                2 * experimento.repeticiones,
            )
            self.assertEqual(
                mock_bfs.call_count,
                experimento.repeticiones,
            )

            self.assertEqual(len(df), experimento.repeticiones)

    def test_normalizar_datos(self):
        datos = pd.DataFrame({
            "visitados_ordenado": [20, 15],
            "visitados_sin_ordenar": [30, 18],
            "visitados_bfs": [10, 6],
            "largo_ordenado": [8, 9],
            "largo_sin_ordenar": [12, 12],
            "largo_bfs": [4, 3],
        })

        normalizar_datos(datos)

        esperado = pd.DataFrame({
            "norm_visitados_ordenado": [2.0, 2.5],
            "norm_visitados_sin_ordenar": [3.0, 3.0],
            "norm_largo_ordenado": [2.0, 3.0],
            "norm_largo_sin_ordenar": [3.0, 4.0],
        })

        pd.testing.assert_frame_equal(
            datos[esperado.columns],
            esperado,
        )
    