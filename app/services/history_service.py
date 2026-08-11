"""
===========================================================
TechDocAI
Servicio de historial de exportaciones
Entrega 4.5
===========================================================
"""

import json
from datetime import datetime
from pathlib import Path

from config import (
    APP_VERSION,
    AI_PROVIDER,
    MODEL_NAME,
)


class HistoryService:
    """
    Gestiona el historial de informes exportados
    por TechDocAI.
    """

    # ======================================================
    # DIRECTORIO BASE DEL PROYECTO
    # ======================================================

    BASE_DIR = Path(__file__).resolve().parents[2]

    # ======================================================
    # DIRECTORIO E HISTORIAL
    # ======================================================

    HISTORY_DIR = BASE_DIR / "historial"

    HISTORY_FILE = HISTORY_DIR / "historial.json"

    # ======================================================
    # INICIALIZAR HISTORIAL
    # ======================================================

    @classmethod
    def _inicializar(cls):

        cls.HISTORY_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        if not cls.HISTORY_FILE.exists():

            cls.HISTORY_FILE.write_text(
                "[]",
                encoding="utf-8"
            )

    # ======================================================
    # NORMALIZAR RUTA
    # ======================================================

    @classmethod
    def _normalizar_ruta(cls, ruta):

        ruta = Path(ruta)

        # Si la ruta es relativa,
        # se interpreta desde la raíz del proyecto.
        if not ruta.is_absolute():

            ruta = cls.BASE_DIR / ruta

        return ruta.resolve()

    # ======================================================
    # LEER HISTORIAL
    # ======================================================

    @classmethod
    def obtener_historial(cls):

        cls._inicializar()

        try:

            contenido = cls.HISTORY_FILE.read_text(
                encoding="utf-8"
            )

            historial = json.loads(
                contenido
            )

            if isinstance(historial, list):

                return historial

            return []

        except (
            json.JSONDecodeError,
            OSError
        ):

            return []

    # ======================================================
    # REGISTRAR EXPORTACIÓN
    # ======================================================

    @classmethod
    def registrar_exportacion(
        cls,
        documento,
        ruta,
        formato
    ):

        cls._inicializar()

        historial = cls.obtener_historial()

        ruta_absoluta = cls._normalizar_ruta(
            ruta
        )

        try:

            ruta_relativa = ruta_absoluta.relative_to(
                cls.BASE_DIR
            )

        except ValueError:

            ruta_relativa = ruta_absoluta

        registro = {

            "documento": documento.nombre,

            "fecha": datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            ),

            "formato": formato.upper(),

            "archivo": ruta_absoluta.name,

            "ruta": ruta_relativa.as_posix(),

            "version": APP_VERSION,

            "proveedor_ia": AI_PROVIDER,

            "modelo": MODEL_NAME,
        }

        historial.append(
            registro
        )

        cls.HISTORY_FILE.write_text(
            json.dumps(
                historial,
                ensure_ascii=False,
                indent=4
            ),
            encoding="utf-8"
        )

        return registro

    # ======================================================
    # ÚLTIMAS EXPORTACIONES
    # ======================================================

    @classmethod
    def ultimas_exportaciones(
        cls,
        cantidad=10
    ):

        historial = cls.obtener_historial()

        return historial[-cantidad:]

    # ======================================================
    # LIMPIAR HISTORIAL
    # ======================================================

    @classmethod
    def limpiar_historial(cls):

        cls._inicializar()

        cls.HISTORY_FILE.write_text(
            "[]",
            encoding="utf-8"
        )