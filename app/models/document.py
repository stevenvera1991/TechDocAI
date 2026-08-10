"""
===========================================================
TechDocAI
Modelo de Documento
===========================================================
"""

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class Document:
    """
    Representa un documento completamente procesado.
    """

    ruta: Path

    nombre: str

    paginas: int

    tamano_mb: float

    caracteres: int

    palabras: int

    lineas: int

    chunks: int

    texto: str

    lista_chunks: list[str] = field(
        default_factory=list
    )

    analisis: str = ""

    @property
    def resumen_estadistico(self) -> str:

        return (
            f"{self.paginas} páginas | "
            f"{self.palabras:,} palabras | "
            f"{self.chunks} chunks"
        )