from app.services.groq_service import GroqService

print("=" * 60)

print("PROBANDO CONEXIÓN CON GROQ")

print("=" * 60)

respuesta = GroqService.prueba_conexion()

print()

print("RESPUESTA:")

print()

print(respuesta)

print()

print("=" * 60)