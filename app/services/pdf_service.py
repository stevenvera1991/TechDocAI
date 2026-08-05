"""
===========================================================
TechDocAI
Servicio para selección de archivos PDF
===========================================================
"""

from tkinter import filedialog
from pathlib import Path


class PDFService:
    """
    Servicio encargado de seleccionar archivos PDF.
    """

    @staticmethod
    def seleccionar_pdf():

        ruta = filedialog.askopenfilename(
            title="Seleccione un documento PDF",
            filetypes=[
                ("Documentos PDF", "*.pdf")
            ]
        )

        if not ruta:
            return None

        return Path(ruta)