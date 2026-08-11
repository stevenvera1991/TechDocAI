"""
===========================================================
TechDocAI
Servicio Groq
===========================================================
"""

from pathlib import Path

from groq import Groq

from config import (
    GROQ_API_KEY,
    GROQ_MODEL,
    GROQ_TEMPERATURE,
    GROQ_MAX_TOKENS,
)

from app.utils.logger import logger


class GroqService:
    """
    Servicio de comunicación con Groq.
    """

    _client = None

    @classmethod
    def cliente(cls):

        if cls._client is None:

            cls._client = Groq(
                api_key=GROQ_API_KEY
            )

        return cls._client

    @classmethod
    def prueba_conexion(cls):

        try:

            respuesta = cls.cliente().chat.completions.create(

                model=GROQ_MODEL,

                temperature=GROQ_TEMPERATURE,

                max_tokens=50,

                messages=[
                    {
                        "role": "user",
                        "content": "Responde únicamente: Conexión exitosa."
                    }
                ]
            )

            texto = respuesta.choices[0].message.content

            logger.info("Conexión con Groq establecida.")

            return texto

        except Exception as error:

            logger.error(str(error))

            raise

    @classmethod
    def analizar_chunk(cls, texto):

        respuesta = cls.cliente().chat.completions.create(

            model=GROQ_MODEL,

            temperature=GROQ_TEMPERATURE,

            max_tokens=600,

            messages=[
                {
                    "role": "system",
                    "content":
                    (
                        "Eres un ingeniero experto en análisis de "
                        "documentación técnica."
                    )
                },
                {
                    "role": "user",
                    "content":
                    (
                        "Analiza el siguiente documento técnico.\n\n"
                        f"{texto}"
                    )
                }
            ]
        )

        return respuesta.choices[0].message.content

    @classmethod
    def resumir_chunk(cls, texto):

        respuesta = cls.cliente().chat.completions.create(

            model=GROQ_MODEL,

            temperature=0.2,

            max_tokens=220,

            messages=[

               {
                    "role": "system",
                    "content":
                    (
                        "Eres un ingeniero experto en documentación técnica."
                    )
                },

                {
                    "role": "user",
                    "content":
                    (
                        "Resume este fragmento técnico en máximo 120 palabras.\n\n"

                        "Incluye únicamente:\n"

                        "- Tema principal\n"

                        "- Conceptos importantes\n"

                        "- Datos relevantes\n\n"

                        f"{texto}"
                    )
                }

            ]

        )

        return respuesta.choices[0].message.content

    @classmethod
    def generar_informe(cls, resumenes):

        texto = "\n\n".join(resumenes)

        respuesta = cls.cliente().chat.completions.create(

            model=GROQ_MODEL,

            temperature=0.2,

            max_tokens=900,

            messages=[

                {
                    "role":"system",

                    "content":

                    (
                        "Eres un ingeniero especializado en análisis documental."
                    )
                },

                {
                    "role":"user",

                    "content":

                    (
                        "A partir de los siguientes resúmenes genera un único "

                        "informe técnico profesional.\n\n"

                        "Incluye:\n"

                        "- Resumen ejecutivo\n"

                        "- Objetivo\n"

                        "- Temas principales\n"

                        "- Hallazgos\n"

                        "- Conclusiones\n"

                        "- Recomendaciones\n\n"

                        f"{texto}"
                    )
                }

            ]

        )

        return respuesta.choices[0].message.content

    @classmethod
    def generar_resumen(cls, informe):

        """
        Genera un resumen ejecutivo a partir
        del informe técnico consolidado.
        """

        if not informe or not str(informe).strip():
            raise ValueError(
                "No existe un informe disponible "
                "para generar el resumen."
            )

        ruta_prompt = (
            Path(__file__).resolve().parents[2]
            / "prompts"
            / "resumen.txt"
        )

        if not ruta_prompt.exists():
            raise FileNotFoundError(
                f"No se encontró el prompt de resumen: "
                f"{ruta_prompt}"
            )

        prompt = ruta_prompt.read_text(
            encoding="utf-8"
        ).strip()

        if not prompt:
            raise ValueError(
                "El archivo prompts/resumen.txt "
                "está vacío."
            )

        respuesta = cls.cliente().chat.completions.create(

            model=GROQ_MODEL,

            temperature=0.2,

            max_tokens=500,

            messages=[

                {
                    "role": "system",

                    "content": prompt
                },

                {
                    "role": "user",

                    "content": (
                        "Genera el resumen ejecutivo "
                        "del siguiente informe técnico.\n\n"
                        f"{informe}"
                    )
                }

            ]

        )

        resumen = (
            respuesta
            .choices[0]
            .message
            .content
        )

        if not resumen or not resumen.strip():
            raise ValueError(
                "Groq no devolvió contenido "
                "para el resumen."
            )

        return resumen.strip()

    @classmethod
    def prueba(cls):
        return "OK"