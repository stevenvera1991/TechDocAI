"""
===========================================================
TechDocAI
Configuración general del sistema
===========================================================
"""

from pathlib import Path

# ==========================================================
# INFORMACIÓN DEL PROYECTO
# ==========================================================

APP_NAME = "TechDocAI"

APP_VERSION = "0.2.0"

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

# ==========================================================
# APARIENCIA
# ==========================================================

THEME_MODE = "dark"

COLOR_THEME = "blue"

WINDOW_RESIZABLE = True

# ==========================================================
# RUTAS
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