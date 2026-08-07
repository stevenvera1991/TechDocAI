"""
===========================================================
TechDocAI
Procesador de texto
===========================================================
"""

import re


class TextProcessor:
    """
    Procesa y limpia el texto extraído de un PDF.
    """

    @staticmethod
    def limpiar(texto: str) -> str:
        """
        Limpia el texto antes de enviarlo a la IA.
        """

        # Eliminar espacios repetidos
        texto = re.sub(r"[ \t]+", " ", texto)

        # Eliminar líneas vacías múltiples
        texto = re.sub(r"\n\s*\n+", "\n\n", texto)

        # Eliminar espacios al inicio y final
        texto = texto.strip()

        return texto

    @staticmethod
    def estadisticas(texto: str):

        palabras = len(texto.split())

        lineas = len(texto.splitlines())

        caracteres = len(texto)

        return {
            "palabras": palabras,
            "lineas": lineas,
            "caracteres": caracteres
        }

    @staticmethod
    def dividir_chunks(
        texto: str,
        max_caracteres: int = 5000
    ):
        """
        Divide un texto largo en bloques para IA.
        """

        palabras = texto.split()

        chunks = []

        chunk_actual = ""

        for palabra in palabras:

            if len(chunk_actual) + len(palabra) + 1 <= max_caracteres:

                chunk_actual += palabra + " "

            else:

                chunks.append(chunk_actual.strip())

                chunk_actual = palabra + " "

        if chunk_actual:

            chunks.append(chunk_actual.strip())

        return chunks