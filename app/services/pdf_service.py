from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError

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
    
    @staticmethod
    def leer_pdf(ruta):
        """
        Lee un documento PDF y devuelve información estructurada.
        """

        try:

            reader = PdfReader(ruta)

            texto = ""

            for pagina in reader.pages:

                contenido = pagina.extract_text()

                if contenido:
                    texto += contenido + "\n"

            if texto.strip() == "":

                raise ValueError(
                    "El documento no contiene texto extraíble."
                )

            return {
                "ruta": ruta,
                "nombre": ruta.name,
                "paginas": len(reader.pages),
                "tamano_mb": round(
                    ruta.stat().st_size / (1024 * 1024),
                    2
                ),
                "caracteres": len(texto),
                "texto": texto,
            }

        except PdfReadError:

            raise Exception(
                "El archivo PDF está dañado o protegido."
            )

        except Exception as e:

            raise Exception(str(e))