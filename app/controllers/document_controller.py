"""
===========================================================
TechDocAI
Controlador de documentos
===========================================================
"""

from app.models.document import Document
from app.services.pdf_service import PDFService
from app.services.groq_service import GroqService
from app.core.text_processor import TextProcessor
from app.utils.logger import logger

class DocumentController:
    """
    Controlador encargado del flujo completo de procesamiento
    de un documento PDF.
    """

    # Documento actualmente cargado
    documento_actual = None

    @staticmethod
    def cargar_documento(ruta):

        info_pdf = PDFService.leer_pdf(ruta)

        texto_limpio = TextProcessor.limpiar(
            info_pdf["texto"]
        )

        chunks = TextProcessor.dividir_chunks(
            texto_limpio
        )

        estadisticas = TextProcessor.estadisticas(
            texto_limpio
        )

        documento = Document(

            ruta=info_pdf["ruta"],

            nombre=info_pdf["nombre"],

            paginas=info_pdf["paginas"],

            tamano_mb=info_pdf["tamano_mb"],

            caracteres=info_pdf["caracteres"],

            palabras=estadisticas["palabras"],

            lineas=estadisticas["lineas"],

            chunks=len(chunks),

            texto=texto_limpio,

            lista_chunks=chunks
        )

        DocumentController.documento_actual = documento

        logger.info(
            f"Documento cargado: {documento.nombre}"
        )

        logger.info(
            f"Páginas: {documento.paginas}"
        )

        logger.info(
            f"Chunks: {documento.chunks}"
        )

        return documento

    @staticmethod
    def analizar_documento():

        if DocumentController.documento_actual is None:

            raise Exception(
                "No existe un documento cargado."
            )

        documento = DocumentController.documento_actual

        resumenes = []

        total = len(documento.lista_chunks)

        logger.info(
            f"Procesando {total} chunks..."
        )

        for indice, chunk in enumerate(documento.lista_chunks):

            logger.info(
                f"Resumiendo chunk {indice+1}/{total}"
            )

            resumen = GroqService.resumir_chunk(
                chunk
            )

            resumenes.append(
                resumen
            )

        logger.info(
            "Generando informe consolidado..."
        )

        informe = GroqService.generar_informe(
            resumenes
        )

        return informe