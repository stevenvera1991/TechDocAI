"""
===========================================================
TechDocAI
Punto de entrada de la aplicación
===========================================================
"""

from config import (
    APP_NAME,
    APP_VERSION,
    AUTHOR,
    AI_PROVIDER,
)


def mostrar_banner() -> None:
    """Muestra la información básica del sistema."""

    print("=" * 55)
    print(f"{APP_NAME} v{APP_VERSION}")
    print("=" * 55)
    print(f"Autor      : {AUTHOR}")
    print(f"Proveedor IA: {AI_PROVIDER}")
    print("=" * 55)


def inicializar() -> None:
    """Inicializa la aplicación."""

    print("Inicializando aplicación...")
    print("Configuración cargada correctamente.")
    print("Sistema listo para iniciar.")


def main() -> None:
    """Función principal."""

    mostrar_banner()
    inicializar()


if __name__ == "__main__":
    main()