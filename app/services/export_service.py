"""
===========================================================
TechDocAI
Servicio de exportación de informes
===========================================================
"""

from pathlib import Path
from datetime import datetime

from app.controllers.document_controller import DocumentController


class ExportService:
    """
    Servicio encargado de exportar informes generados
    por TechDocAI.
    """

    @staticmethod
    def exportar_markdown():

        documento = DocumentController.documento_actual

        if documento is None:

            raise Exception(
                "No existe un documento cargado."
            )

        if not documento.analisis:

            raise Exception(
                "Debe analizar el documento antes de exportarlo."
            )

        carpeta = Path("exports")

        carpeta.mkdir(exist_ok=True)

        nombre_archivo = documento.ruta.stem + "_Informe.md"

        ruta_archivo = carpeta / nombre_archivo

        contenido = f"""# INFORME TÉCNICO - TECHDOCAI

Fecha de generación:
{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}

---

## Información del documento

- Nombre: {documento.nombre}
- Páginas: {documento.paginas}
- Tamaño: {documento.tamano_mb:.2f} MB
- Caracteres: {documento.caracteres}
- Palabras: {documento.palabras}
- Líneas: {documento.lineas}
- Chunks procesados: {documento.chunks}

---

# ANÁLISIS GENERADO POR IA

{documento.analisis}

---

Informe generado automáticamente por TechDocAI.
"""

        ruta_archivo.write_text(
            contenido,
            encoding="utf-8"
        )

        return ruta_archivo