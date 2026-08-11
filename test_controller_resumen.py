"""
===========================================================
TechDocAI
Prueba de integración DocumentController + resumen
Entrega 5.2
===========================================================
"""

from app.controllers.document_controller import DocumentController


print("=" * 60)
print("PRUEBA DE INTEGRACIÓN DEL RESUMEN")
print("=" * 60)

print()
print("Configurando documento de prueba...")

documento = DocumentController.documento_actual

print()
print("Estado inicial del controlador:")
print(documento)

print()
print("=" * 60)
print("PRUEBA 1 — Sin documento cargado")
print("=" * 60)

try:

    DocumentController.generar_resumen()

except Exception as error:

    print()
    print("Error controlado:")
    print(str(error))


print()
print("=" * 60)
print("PRUEBA 2 — Documento con análisis")
print("=" * 60)

# Crear un objeto de prueba mínimo utilizando el modelo real
from pathlib import Path
from app.models.document import Document


documento_prueba = Document(
    ruta=Path("documento_prueba.pdf"),
    nombre="Documento de prueba",
    paginas=1,
    tamano_mb=0.1,
    caracteres=500,
    palabras=80,
    lineas=20,
    chunks=1,
    texto="Contenido técnico de prueba",
    lista_chunks=["Contenido técnico de prueba"]
)

documento_prueba.analisis = """
INFORME TÉCNICO DE PRUEBA

El sistema TechDocAI permite analizar documentos técnicos
mediante inteligencia artificial.

El análisis identifica los principales conceptos técnicos,
hallazgos y conclusiones del documento.

Se recomienda continuar mejorando el procesamiento y
la generación automática de informes.
"""

DocumentController.documento_actual = documento_prueba

print()
print("Análisis de prueba asignado correctamente.")

print()
print("Generando resumen mediante DocumentController...")

try:

    resumen = DocumentController.generar_resumen()

    print()
    print("=" * 60)
    print("RESUMEN GENERADO CORRECTAMENTE")
    print("=" * 60)
    print()
    print(resumen)
    print()
    print("=" * 60)

except Exception as error:

    print()
    print("=" * 60)
    print("ERROR")
    print("=" * 60)
    print()
    print(type(error).__name__)
    print(str(error))