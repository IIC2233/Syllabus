import os

from clases.fabrica import Caja, CajaRechazadaError, Registro
from clases.lista_ligada import ListaLigada
from clases.maquinas import MaquinaInspeccion
from consultas import generar_reporte, registros_por_resultado
from utils import cargar_cajas


PESO_MAXIMO = 50.0  # PUEDES MODIFICAR ESTA VARIABLE
RUTA_DATOS = os.path.join("datos", "cajas.csv")


if __name__ == "__main__":

    # -------------------------------------------------------------------
    # PARTE 1: agregar y retirar_primera
    # -------------------------------------------------------------------
    print("=== PARTE 1: agregar ===")
    cinta_prueba = ListaLigada()
    cinta_prueba.agregar(Caja("CJA-1042", "Cereal integral", "4.2"))
    cinta_prueba.agregar(Caja("CJA-6412", "Fideos largos", "2.5"))
    cinta_prueba.agregar(Caja("CJA-1188", "Te en bolsitas", "0.4"))
    print(f"cabeza: {cinta_prueba.cabeza}")
    print(f"cola: {cinta_prueba.cola}")
    print(f"largo: {len(cinta_prueba)}")

    print("\n=== PARTE 1: retirar_primera ===")
    print(f"sale de la cinta: {cinta_prueba.retirar_primera()}")
    print(f"sale de la cinta: {cinta_prueba.retirar_primera()}")
    print(f"sale la última que queda: {cinta_prueba.retirar_primera()}")
    print(f"cabeza: {cinta_prueba.cabeza}, cola: {cinta_prueba.cola}, "
          f"largo: {len(cinta_prueba)}")

    try:
        cinta_prueba.retirar_primera()
        print("No se levantó IndexError")
    except IndexError as error:
        print(f"IndexError: {error}")

    # -------------------------------------------------------------------
    # PARTE 2: iterable e iterador
    # -------------------------------------------------------------------
    print("\n=== PARTE 2: recorrer la cinta ===")
    cinta_llena = ListaLigada()
    cinta_llena.agregar(Caja("CJA-7520", "Arroz grano largo", "18.0"))
    cinta_llena.agregar(Caja("CJA-2296", "Galletas surtidas", "7.3"))
    cinta_llena.agregar(Caja("CJA-5566", "Papel absorbente", "3.8"))

    for caja in cinta_llena:
        print(caja)

    print(f"la cinta no se consume, sigue con largo {len(cinta_llena)}")

    print("\n=== PARTE 2: iteradores independientes ===")
    primero = iter(cinta_llena)
    segundo = iter(cinta_llena)
    print(f"primero avanza a: {next(primero).codigo}")
    print(f"primero avanza a: {next(primero).codigo}")
    print(f"segundo parte de nuevo en: {next(segundo).codigo}")

    # -------------------------------------------------------------------
    # PARTE 3: la máquina
    #
    # Se arma la cinta con las cajas del archivo y se procesan una a una,
    # siempre desde la cabeza. Cada resultado queda en la bitácora.
    # -------------------------------------------------------------------
    print("\n=== PARTE 3: la máquina ===")
    maquina = MaquinaInspeccion(PESO_MAXIMO)
    cinta = ListaLigada()
    for caja in cargar_cajas(RUTA_DATOS):
        cinta.agregar(caja)

    print(f"cajas en la cinta: {len(cinta)}")

    bitacora = ListaLigada()
    while len(cinta) > 0:
        caja = cinta.retirar_primera()
        try:
            maquina.inspeccionar(caja)
        except CajaRechazadaError as error:
            print(f"{caja.codigo}: {error}")
            bitacora.agregar(
                Registro(caja.codigo, "Rechazada", error.motivo))
        else:
            print(f"{caja.codigo}: aprobada")
            bitacora.agregar(Registro(caja.codigo, "Aprobada"))

    print(f"la cinta quedó vacía: {len(cinta) == 0}")

    # -------------------------------------------------------------------
    # PARTE 4: consultas sobre la bitácora de la Parte 3
    # -------------------------------------------------------------------
    print("\n=== PARTE 4: consultas ===")
    aprobados = registros_por_resultado(bitacora, "Aprobada")
    print(f"registros_por_resultado entrega un {type(aprobados).__name__}")
    for registro in aprobados:
        print(registro)

    reporte = generar_reporte(bitacora, "Rechazada")
    print(f"\ngenerar_reporte entrega un {type(reporte).__name__}")
    for linea in reporte:
        print(linea)
