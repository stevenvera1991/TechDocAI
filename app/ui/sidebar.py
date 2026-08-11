"""
===========================================================
TechDocAI
Barra lateral principal
===========================================================
"""

import customtkinter as ctk


class Sidebar(ctk.CTkFrame):
    """
    Barra lateral principal de TechDocAI.

    Contiene las acciones principales de la aplicación:
    - Cargar PDF
    - Analizar documento
    - Generar resumen
    - Exportar Markdown
    - Exportar PDF
    - Exportar DOCX
    """

    def __init__(
        self,
        master,
        abrir_pdf_callback,
        analizar_callback=None,
        resumen_callback=None,
        markdown_callback=None,
        pdf_callback=None,
        docx_callback=None,
    ):

        self.abrir_pdf_callback = abrir_pdf_callback
        self.analizar_callback = analizar_callback
        self.resumen_callback = resumen_callback
        self.markdown_callback = markdown_callback
        self.pdf_callback = pdf_callback
        self.docx_callback = docx_callback

        super().__init__(
            master,
            width=240,
            corner_radius=0
        )

        self.grid_propagate(False)

        self._crear_componentes()

    def _crear_componentes(self):

        # ==================================================
        # TÍTULO
        # ==================================================

        titulo = ctk.CTkLabel(
            self,
            text="MENÚ",
            font=("Segoe UI", 18, "bold")
        )

        titulo.pack(
            pady=(20, 25)
        )

        # ==================================================
        # ABRIR PDF
        # ==================================================

        self.btn_pdf = ctk.CTkButton(
            self,
            text="Abrir PDF",
            height=40,
            command=self.abrir_pdf_callback
        )

        self.btn_pdf.pack(
            fill="x",
            padx=15,
            pady=6
        )

        # ==================================================
        # ANALIZAR DOCUMENTO
        # ==================================================

        self.btn_ia = ctk.CTkButton(
            self,
            text="Analizar Documento",
            height=40,
            command=self.analizar_callback
        )

        self.btn_ia.pack(
            fill="x",
            padx=15,
            pady=6
        )

        # ==================================================
        # GENERAR RESUMEN
        # ==================================================

        self.btn_resumen = ctk.CTkButton(
            self,
            text="Generar Resumen",
            height=40,
            command=self.resumen_callback
        )

        self.btn_resumen.pack(
            fill="x",
            padx=15,
            pady=6
        )

        # ==================================================
        # EXPORTAR MARKDOWN
        # ==================================================

        self.btn_markdown = ctk.CTkButton(
            self,
            text="Exportar Markdown",
            height=40,
            command=self.markdown_callback
        )

        self.btn_markdown.pack(
            fill="x",
            padx=15,
            pady=6
        )

        # ==================================================
        # EXPORTAR PDF
        # ==================================================

        self.btn_exportar = ctk.CTkButton(
            self,
            text="Exportar PDF",
            height=40,
            command=self.pdf_callback
        )

        self.btn_exportar.pack(
            fill="x",
            padx=15,
            pady=6
        )

        # ==================================================
        # EXPORTAR DOCX
        # ==================================================

        self.btn_docx = ctk.CTkButton(
            self,
            text="Exportar DOCX",
            height=40,
            command=self.docx_callback
        )

        self.btn_docx.pack(
            fill="x",
            padx=15,
            pady=6
        )

        # ==================================================
        # ESPACIO FLEXIBLE
        # ==================================================

        espacio = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        espacio.pack(
            expand=True,
            fill="both"
        )