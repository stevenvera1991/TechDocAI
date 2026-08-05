"""
===========================================================
TechDocAI
Status Bar
===========================================================
"""

import customtkinter as ctk

from config import APP_VERSION, AI_PROVIDER


class StatusBar(ctk.CTkFrame):
    """
    Barra de estado inferior.
    """

    def __init__(self, master):

        super().__init__(
            master,
            height=30,
            corner_radius=0
        )

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)

        self._crear_componentes()

    def _crear_componentes(self):

        self.estado_label = ctk.CTkLabel(
            self,
            text="Estado: Listo",
            anchor="w",
            font=("Segoe UI", 12)
        )

        self.estado_label.grid(
            row=0,
            column=0,
            padx=(10, 0),
            sticky="w"
        )

        self.ia_label = ctk.CTkLabel(
            self,
            text=f"IA: {AI_PROVIDER.capitalize()}",
            font=("Segoe UI", 12)
        )

        self.ia_label.grid(
            row=0,
            column=1,
            padx=20
        )

        self.version_label = ctk.CTkLabel(
            self,
            text=f"Versión {APP_VERSION}",
            font=("Segoe UI", 12)
        )

        self.version_label.grid(
            row=0,
            column=2,
            padx=(0, 10),
            sticky="e"
        )

    def actualizar_estado(self, mensaje: str):
        """
        Actualiza el texto del estado.
        """

        self.estado_label.configure(
            text=f"Estado: {mensaje}"
        )