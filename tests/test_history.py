"""
Prueba del servicio de historial de TechDocAI.
"""

from pathlib import Path

from app.services.history_service import HistoryService


class DocumentoPrueba:

    nombre = "Documento técnico de prueba.pdf"


print("=" * 60)
print("PRUEBA DE HISTORIAL DE EXPORTACIONES")
print("=" * 60)

documento = DocumentoPrueba()

ruta_prueba = (
    Path("exports")
    / "documento_prueba_Informe.pdf"
)

print()
print("Registrando exportación...")

registro = HistoryService.registrar_exportacion(
    documento=documento,
    ruta=ruta_prueba,
    formato="PDF"
)

print()
print("REGISTRO CREADO CORRECTAMENTE")
print("=" * 60)

print(
    f"Documento: {registro['documento']}"
)

print(
    f"Fecha: {registro['fecha']}"
)

print(
    f"Formato: {registro['formato']}"
)

print(
    f"Archivo: {registro['archivo']}"
)

print(
    f"Ruta: {registro['ruta']}"
)

print(
    f"Versión: {registro['version']}"
)

print(
    f"Proveedor IA: {registro['proveedor_ia']}"
)

print(
    f"Modelo: {registro['modelo']}"
)

print("=" * 60)

print()
print("HISTORIAL ACTUAL:")

historial = HistoryService.obtener_historial()

for indice, elemento in enumerate(
    historial,
    start=1
):

    print(
        f"{indice}. "
        f"{elemento['fecha']} | "
        f"{elemento['formato']} | "
        f"{elemento['archivo']}"
    )