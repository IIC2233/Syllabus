"""
Herramientas de consola para la simulación.

NO MODIFICAR.

Cuando varios threads usan print() al mismo tiempo, los mensajes salen
mezclados o cortados. Por eso log() protege la impresión con un Lock: así
solo un thread escribe en la consola a la vez.
"""
import time
from threading import Lock

ANCHO = 62


class Consola:
    """Imprime mensajes de forma segura entre threads, con un cronómetro."""

    def __init__(self) -> None:
        self._lock = Lock()
        self._inicio = None

    def iniciar_cronometro(self) -> None:
        """Fija el instante 0 del cronómetro que muestran los mensajes."""
        with self._lock:
            self._inicio = time.time()

    def log(self, emisor: str, mensaje: str) -> None:
        """
        Imprime un mensaje de forma segura entre threads, indicando el tiempo
        transcurrido y quién lo emite.

        Ejemplo de salida:
            [  4.07s] [Yoshi   ] emplata Pedido #3 (Hamburguesa doble)
        """
        with self._lock:
            if self._inicio is None:
                self._inicio = time.time()
            transcurrido = time.time() - self._inicio
            print(f"[{transcurrido:6.2f}s] [{emisor:<8}] {mensaje}", flush=True)


# Instancia única compartida por todo el programa. Se exponen sus métodos
_consola = Consola()
iniciar_cronometro = _consola.iniciar_cronometro
log = _consola.log


def imprimir_reporte(pedidos: list, tiempos: dict,
                     no_entregados: list) -> None:
    """Imprime el reporte final del servicio."""
    print()
    print("=" * ANCHO)
    print(" REPORTE FINAL DEL SERVICIO ".center(ANCHO))
    print("=" * ANCHO)
    _imprimir_entregados(pedidos, tiempos)
    _imprimir_no_entregados(pedidos, no_entregados)
    _imprimir_veredicto(pedidos, tiempos, no_entregados)


def _imprimir_entregados(pedidos: list, tiempos: dict) -> None:
    print(f"\n PEDIDOS ENTREGADOS ({len(tiempos)}/{len(pedidos)})")
    print(" " + "-" * (ANCHO - 2))

    if not tiempos:
        print(" No se entregó ningún pedido.")
        return

    platos = {pedido.id_pedido: pedido.plato for pedido in pedidos}
    print(f" {'Pedido':<8}{'Plato':<22}{'Tiempo de preparación':>20}")
    for id_pedido, tiempo in sorted(tiempos.items(), key=lambda par: par[1]):
        segundos = f"{tiempo.total_seconds():.2f} s"
        print(f" #{id_pedido:<7}{platos[id_pedido]:<22}{segundos:>20}")

    promedio = sum(t.total_seconds() for t in tiempos.values()) / len(tiempos)
    id_lento, tiempo_lento = max(tiempos.items(), key=lambda par: par[1])
    print(" " + "-" * (ANCHO - 2))
    print(f" Tiempo promedio de preparación: {promedio:.2f} s")
    print(f" Pedido más lento: #{id_lento} "
          f"({tiempo_lento.total_seconds():.2f} s)")


def _imprimir_no_entregados(pedidos: list, no_entregados: list) -> None:
    print(f"\n PEDIDOS NO ENTREGADOS ({len(no_entregados)}/{len(pedidos)})")
    print(" " + "-" * (ANCHO - 2))

    if not no_entregados:
        print(" ¡Ninguno! Se alcanzó a entregar todo el servicio.")
        return

    for pedido in no_entregados:
        print(f" #{pedido.id_pedido:<7}{pedido.plato:<22}"
              f"{'la cocina cerró antes':>20}")


def _imprimir_veredicto(pedidos: list, tiempos: dict,
                        no_entregados: list) -> None:
    print("\n" + "=" * ANCHO)
    reportados = len(tiempos) + len(no_entregados)
    if reportados != len(pedidos):
        print(f" ADVERTENCIA: hay {len(pedidos)} pedidos en total, pero el "
              f"reporte solo da cuenta de {reportados}.")
    elif not no_entregados:
        print(" SERVICIO PERFECTO: todos los pedidos salieron a tiempo.")
    else:
        print(f" SERVICIO INCOMPLETO: {len(no_entregados)} pedido(s) "
              f"quedaron sin entregar.")
    print("=" * ANCHO)
