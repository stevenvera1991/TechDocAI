"""
===========================================================
TechDocAI
Sidebar
===========================================================
"""

import customtkinter as ctk


class Sidebar(ctk.CTkFrame):
    """
    Barra lateral principal.
    """

    def __init__(self, master, abrir_pdf_callback):

        self.abrir_pdf_callback = abrir_pdf_callback

        super().__init__(
            master,
            width=240,
            corner_radius=0
        )

        self.grid_propagate(False)

        self._crear_componentes()

    def _crear_componentes(self):

        # -----------------------------
        # Título
        # -----------------------------

        titulo = ctk.CTkLabel(
            self,
            text="MENÚ",
            font=("Segoe UI", 18, "bold")
        )

        titulo.pack(pady=(20, 25))

        # -----------------------------
        # Botones
        # -----------------------------

        self.btn_pdf = ctk.CTkButton(
            self,
            text="Abrir PDF",
            height=40,
            command=self.abrir_pdf_callback
        )

        self.btn_pdf.pack(
            fill="x",
            padx=15,
            pady=8
        )

        self.btn_ia = ctk.CTkButton(
            self,
            text="Analizar Documento",
            height=40
        )

        self.btn_ia.pack(
            fill="x",
            padx=15,
            pady=8
        )

        self.btn_resumen = ctk.CTkButton(
            self,
            text="Generar Resumen",
            height=40
        )

        self.btn_resumen.pack(
            fill="x",
            padx=15,
            pady=8
        )

        self.btn_exportar = ctk.CTkButton(
            self,
            text="Exportar Informe",
            height=40
        )

        self.btn_exportar.pack(
            fill="x",
            padx=15,
            pady=8
        )

        # -----------------------------
        # Espacio flexible
        # -----------------------------

        espacio = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        espacio.pack(
            expand=True,
            fill="both"
        )