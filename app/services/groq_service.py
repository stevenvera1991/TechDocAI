"""
===========================================================
TechDocAI
Servicio Groq
===========================================================
"""

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
    def prueba(cls):
        return "OK"