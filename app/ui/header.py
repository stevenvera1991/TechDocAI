"""
===========================================================
TechDocAI
Componente Header
===========================================================
"""

import customtkinter as ctk

from config import APP_NAME


class Header(ctk.CTkFrame):
    """
    Encabezado principal de la aplicación.
    """

    def __init__(self, master):

        super().__init__(
            master,
            height=80,
            corner_radius=0
        )

        self.grid_columnconfigure(0, weight=1)

        self._crear_componentes()

    def _crear_componentes(self):

        # -----------------------------
        # Contenedor izquierdo
        # -----------------------------

        frame_texto = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        frame_texto.grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=10
        )

        titulo = ctk.CTkLabel(
            frame_texto,
            text=APP_NAME,
            font=("Segoe UI", 26, "bold")
        )

        titulo.pack(anchor="w")

        subtitulo = ctk.CTkLabel(
            frame_texto,
            text="Intelligent Technical Document Analyzer",
            font=("Segoe UI", 13)
        )

        subtitulo.pack(anchor="w")