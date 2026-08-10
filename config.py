"""
===========================================================
TechDocAI
Configuración general de la aplicación
===========================================================
"""

from pathlib import Path
import os

from dotenv import load_dotenv


# ==========================================================
# INFORMACIÓN DEL PROYECTO
# ==========================================================

APP_NAME = "TechDocAI"

APP_VERSION = "0.4.0"

AUTHOR = "Steven Vera"

COURSE = "Python + IA"

INSTITUTION = "Institute Technology Bertoni"


# ==========================================================
# PROVEEDOR IA
# ==========================================================

AI_PROVIDER = "groq"

MODEL_NAME = "llama-3.3-70b-versatile"

TEMPERATURE = 0.3

MAX_TOKENS = 2048


# ==========================================================
# VENTANA
# ==========================================================

WINDOW_TITLE = "TechDocAI"

WINDOW_WIDTH = 1200

WINDOW_HEIGHT = 750

WINDOW_RESIZABLE = True


# ==========================================================
# APARIENCIA
# ==========================================================

THEME_MODE = "dark"

COLOR_THEME = "blue"


# ==========================================================
# RUTAS DEL PROYECTO
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

ASSETS_DIR = BASE_DIR / "assets"

DATA_DIR = BASE_DIR / "data"

PDF_DIR = DATA_DIR / "pdf"

RESULTS_DIR = DATA_DIR / "resultados"

PROMPTS_DIR = BASE_DIR / "prompts"

LOGS_DIR = BASE_DIR / "logs"

TESTS_DIR = BASE_DIR / "tests"


# ==========================================================
# LOGS
# ==========================================================

LOG_FILE = LOGS_DIR / "app.log"


# ==========================================================
# GROQ
# ==========================================================

load_dotenv(
    BASE_DIR / ".env"
)

GROQ_API_KEY = os.getenv(
    "GROQ_API_KEY"
)

GROQ_MODEL = "llama-3.3-70b-versatile"

GROQ_TEMPERATURE = 0.2

GROQ_MAX_TOKENS = 4096