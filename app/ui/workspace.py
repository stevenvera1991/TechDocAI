"""
===========================================================
TechDocAI
Workspace
===========================================================
"""

import customtkinter as ctk


class Workspace(ctk.CTkFrame):
    """
    Área principal de trabajo.
    """

    def __init__(self, master):

        super().__init__(
            master,
            corner_radius=0
        )

        self._crear_componentes()

    def _crear_componentes(self):

        contenedor = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        contenedor.pack(
            expand=True
        )

        titulo = ctk.CTkLabel(
            contenedor,
            text="Bienvenido a TechDocAI",
            font=("Segoe UI", 28, "bold")
        )

        titulo.pack(pady=(20, 10))

        descripcion = ctk.CTkLabel(
            contenedor,
            text=(
                "Analice documentos técnicos utilizando Inteligencia Artificial.\n\n"
                "Este sistema permitirá:\n"
                "• Extraer texto de archivos PDF.\n"
                "• Analizar documentos mediante Groq.\n"
                "• Generar resúmenes técnicos.\n"
                "• Exportar informes automáticamente."
            ),
            justify="center",
            font=("Segoe UI", 14)
        )

        descripcion.pack(pady=10)

        instrucciones = ctk.CTkLabel(
            contenedor,
            text=(
                "Para comenzar:\n\n"
                "1. Presione 'Abrir PDF'.\n"
                "2. Seleccione un documento.\n"
                "3. Ejecute el análisis."
            ),
            justify="center",
            font=("Segoe UI", 13)
        )

        instrucciones.pack(pady=(20, 0))