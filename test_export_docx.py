"""
===========================================================
TechDocAI
Prueba independiente de exportación DOCX
===========================================================
"""

from pathlib import Path

from app.models.document import Document
from app.controllers.document_controller import DocumentController
from app.services.export_service import ExportService


def main():

    print("=" * 60)
    print("PRUEBA DE EXPORTACIÓN DOCX")
    print("=" * 60)

    documento = Document(
        ruta=Path(
            "documento_prueba.docx"
        ),
        nombre="Documento técnico de prueba",
        paginas=5,
        tamano_mb=1.25,
        caracteres=12500,
        palabras=2100,
        lineas=350,
        chunks=1,
        texto="Texto de prueba para TechDocAI.",
        lista_chunks=[
            (
                "Texto de prueba para validar "
                "la generación del informe DOCX."
            )
        ]
    )

    documento.analisis = """
# Análisis técnico de prueba

## 1. Objetivo

Este documento se utiliza para comprobar
la generación automática de informes DOCX
mediante TechDocAI.

## 2. Resultados

- El documento fue procesado correctamente.
- La información estadística fue registrada.
- El informe DOCX puede ser generado.
- La prueba no utiliza la API de Groq.

## 3. Conclusión

La exportación DOCX funciona correctamente
cuando existe un documento analizado.
"""

    DocumentController.documento_actual = documento

    print()
    print("Documento de prueba creado.")

    print(
        f"Nombre: {documento.nombre}"
    )

    print()
    print("Generando DOCX...")

    ruta = ExportService.exportar_docx()

    print()
    print("DOCX GENERADO CORRECTAMENTE")
    print("=" * 60)

    print(
        f"Ruta: {ruta}"
    )

    print(
        f"Existe: {ruta.exists()}"
    )

    if ruta.exists():

        print(
            f"Tamaño: {ruta.stat().st_size:,} bytes"
        )

    print("=" * 60)


if __name__ == "__main__":
    main()