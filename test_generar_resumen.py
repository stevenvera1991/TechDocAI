"""
===========================================================
TechDocAI
Prueba de generación de resumen
Entrega 5.1
===========================================================
"""

from app.services.groq_service import GroqService


print("=" * 60)
print("PRUEBA DE GENERACIÓN DE RESUMEN")
print("=" * 60)

informe_prueba = """
INFORME TÉCNICO DE PRUEBA

Objetivo:
Evaluar el funcionamiento del sistema TechDocAI para
analizar documentos técnicos mediante inteligencia artificial.

Hallazgos:
El sistema permite extraer texto de documentos PDF,
procesarlo mediante fragmentos y utilizar un modelo de IA
para generar un informe consolidado.

Conclusiones:
El flujo de análisis documental funciona correctamente
y permite obtener información técnica estructurada.

Recomendaciones:
Continuar mejorando la generación automática de resúmenes
y la presentación de los resultados.
"""

print()
print("Enviando informe de prueba a Groq...")
print()

try:

    resumen = GroqService.generar_resumen(
        informe_prueba
    )

    print("=" * 60)
    print("RESUMEN GENERADO CORRECTAMENTE")
    print("=" * 60)
    print()
    print(resumen)
    print()
    print("=" * 60)

except Exception as error:

    print()
    print("=" * 60)
    print("ERROR EN LA GENERACIÓN DEL RESUMEN")
    print("=" * 60)
    print()
    print(type(error).__name__)
    print(str(error))