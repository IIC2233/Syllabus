import os
from tests_privados.test_tools import IICTest, timeout
from backend.consultas import cadena_creacion, cargar_juguete_recurso, cargar_recurso_recurso

N_SECOND = 5.0
PATH_S = os.path.join("tests_privados", "data", "S")
PATH_M = os.path.join("tests_privados", "data", "M")
PATH_L = os.path.join("tests_privados", "data", "L")
PATH_XL = os.path.join("tests_privados", "data", "XL")


class TestCadenaCreacionCargaDatosPrivado(IICTest):
    """
    Verifica cadena_creacion cargando juguete_recurso y recurso_recurso desde datasets
    privados S, M, L y XL. Comprueba cadenas de distinta profundidad, recursos sin
    productores directos y recursos compartidos entre ramas.
    """

    @timeout(N_SECOND)
    def test_S_0(self):
        """
        Dataset S, recurso=1: recurso hoja sin receta; solo tiene juguetes productores
        (11, 29, 44) y el diccionario de recursos queda vacio.
        """
        gen_jr = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        gen_rr = cargar_recurso_recurso(os.path.join(PATH_S, "recurso_recurso.csv"))
        esperado = {1: {"recursos": {}, "juguetes": (11, 29, 44)}}
        self.assertEqual(cadena_creacion(gen_jr, gen_rr, 1), esperado)

    @timeout(N_SECOND)
    def test_S_1(self):
        """
        Dataset S, recurso=2: cadena de un nivel (R2 ← R1); R2 tiene dos productores
        directos (J5, J31) y R1 es hoja con tres productores.
        """
        gen_jr = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        gen_rr = cargar_recurso_recurso(os.path.join(PATH_S, "recurso_recurso.csv"))
        esperado = {
            2: {
                "recursos": {
                    1: {"recursos": {}, "juguetes": (11, 29, 44)},
                },
                "juguetes": (5, 31),
            }
        }
        self.assertEqual(cadena_creacion(gen_jr, gen_rr, 2), esperado)

    @timeout(N_SECOND)
    def test_S_2(self):
        """
        Dataset S, recurso=20: cadena lineal de 3 niveles (R20 ← R18 ← R4 ← R1);
        cada nivel tiene productores directos excepto R20 que solo tiene J33.
        """
        gen_jr = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        gen_rr = cargar_recurso_recurso(os.path.join(PATH_S, "recurso_recurso.csv"))
        esperado = {
            20: {
                "recursos": {
                    18: {
                        "recursos": {
                            4: {
                                "recursos": {
                                    1: {"recursos": {}, "juguetes": (11, 29, 44)},
                                },
                                "juguetes": (9,),
                            },
                        },
                        "juguetes": (17, 34, 36),
                    },
                },
                "juguetes": (33,),
            }
        }
        self.assertEqual(cadena_creacion(gen_jr, gen_rr, 20), esperado)

    @timeout(N_SECOND)
    def test_M_0(self):
        """
        Dataset M, recurso=20: cadena lineal de 3 niveles (R20 ← R10 ← R4 ← R1);
        R20 no tiene productores directos (juguetes vacio).
        """
        gen_jr = cargar_juguete_recurso(os.path.join(PATH_M, "juguete_recurso.csv"))
        gen_rr = cargar_recurso_recurso(os.path.join(PATH_M, "recurso_recurso.csv"))
        esperado = {
            20: {
                "recursos": {
                    10: {
                        "recursos": {
                            4: {
                                "recursos": {
                                    1: {"recursos": {}, "juguetes": (11,)},
                                },
                                "juguetes": (9, 100),
                            },
                        },
                        "juguetes": (4, 33, 112, 123, 146),
                    },
                },
                "juguetes": (),
            }
        }
        self.assertEqual(cadena_creacion(gen_jr, gen_rr, 20), esperado)

    @timeout(N_SECOND)
    def test_L_0(self):
        """
        Dataset L, recurso=20: cadena de un nivel (R20 ← R1); R20 tiene un productor
        directo (J322) y R1 es hoja con cuatro productores.
        """
        gen_jr = cargar_juguete_recurso(os.path.join(PATH_L, "juguete_recurso.csv"))
        gen_rr = cargar_recurso_recurso(os.path.join(PATH_L, "recurso_recurso.csv"))
        esperado = {
            20: {
                "recursos": {
                    1: {"recursos": {}, "juguetes": (11, 62, 101, 232)},
                },
                "juguetes": (322,),
            }
        }
        self.assertEqual(cadena_creacion(gen_jr, gen_rr, 20), esperado)

    @timeout(N_SECOND)
    def test_XL_recurso_repetido_en_dos_lugares(self):
        """
        XL privado: en la cadena de R8, R6 aparece como requisito directo e indirecto.
        La expansion de R6 debe repetirse correctamente en ambas posiciones.
        """
        gen_jr = cargar_juguete_recurso(os.path.join(PATH_XL, "juguete_recurso.csv"))
        gen_rr = cargar_recurso_recurso(os.path.join(PATH_XL, "recurso_recurso.csv"))
        cadena_R6 = {
            6: {
                "recursos": {
                    2: {
                        "recursos": {
                            1: {"recursos": {}, "juguetes": (11,)},
                        },
                        "juguetes": (5, 691),
                    },
                },
                "juguetes": (3, 66, 73, 383),
            }
        }
        esperado = {
            8: {
                "recursos": {
                    7: {
                        "recursos": cadena_R6,
                        "juguetes": (1,),
                    },
                    6: cadena_R6[6],
                },
                "juguetes": (6, 272),
            }
        }
        self.assertEqual(cadena_creacion(gen_jr, gen_rr, 8), esperado)

    @timeout(N_SECOND)
    def test_XL_ramas_independientes_de_distinta_profundidad(self):
        """
        XL privado: R14 tiene dos ramas independientes con distinta profundidad.
        Debe expandir ambas subcadenas sin mezclar sus niveles.
        """
        gen_jr = cargar_juguete_recurso(os.path.join(PATH_XL, "juguete_recurso.csv"))
        gen_rr = cargar_recurso_recurso(os.path.join(PATH_XL, "recurso_recurso.csv"))
        esperado = {
            14: {
                "recursos": {
                    13: {
                        "recursos": {
                            7: {
                                "recursos": {
                                    6: {
                                        "recursos": {
                                            2: {
                                                "recursos": {
                                                    1: {"recursos": {}, "juguetes": (11,)},
                                                },
                                                "juguetes": (5, 691),
                                            },
                                        },
                                        "juguetes": (3, 66, 73, 383),
                                    },
                                },
                                "juguetes": (1,),
                            },
                        },
                        "juguetes": (),
                    },
                    10: {
                        "recursos": {
                            4: {
                                "recursos": {
                                    1: {"recursos": {}, "juguetes": (11,)},
                                },
                                "juguetes": (9, 202),
                            },
                        },
                        "juguetes": (4,),
                    },
                },
                "juguetes": (),
            }
        }
        self.assertEqual(cadena_creacion(gen_jr, gen_rr, 14), esperado)
