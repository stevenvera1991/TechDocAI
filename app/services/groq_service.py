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