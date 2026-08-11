"""
===========================================================
TechDocAI
Ventana principal
===========================================================
"""

import customtkinter as ctk

from tkinter import messagebox

from config import (
    WINDOW_TITLE,
    APP_VERSION,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    THEME_MODE,
    COLOR_THEME,
    WINDOW_RESIZABLE,
)

from app.ui.header import Header
from app.ui.sidebar import Sidebar
from app.ui.workspace import Workspace
from app.ui.statusbar import StatusBar

from app.services.pdf_service import PDFService
from app.services.export_service import ExportService

from app.controllers.document_controller import DocumentController


class TechDocAIApp(ctk.CTk):
    """
    Ventana principal de TechDocAI.
    """

    def __init__(self):

        super().__init__()

        self._configurar_apariencia()

        self._configurar_ventana()

        self._crear_layout()

    # ======================================================
    # APARIENCIA
    # ======================================================

    def _configurar_apariencia(self):

        ctk.set_appearance_mode(
            THEME_MODE
        )

        ctk.set_default_color_theme(
            COLOR_THEME
        )

    # ======================================================
    # CONFIGURACIÓN DE VENTANA
    # ======================================================

    def _configurar_ventana(self):

        self.title(
            f"{WINDOW_TITLE} v{APP_VERSION}"
        )

        self.geometry(
            f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
        )

        self.resizable(
            WINDOW_RESIZABLE,
            WINDOW_RESIZABLE
        )

        self.grid_rowconfigure(
            1,
            weight=1
        )

        self.grid_columnconfigure(
            1,
            weight=1
        )

        self._centrar()

    # ======================================================
    # CENTRAR VENTANA
    # ======================================================

    def _centrar(self):

        self.update_idletasks()

        ancho = WINDOW_WIDTH
        alto = WINDOW_HEIGHT

        pantalla_ancho = (
            self.winfo_screenwidth()
        )

        pantalla_alto = (
            self.winfo_screenheight()
        )

        x = int(
            (pantalla_ancho - ancho) / 2
        )

        y = int(
            (pantalla_alto - alto) / 2
        )

        self.geometry(
            f"{ancho}x{alto}+{x}+{y}"
        )

    # ======================================================
    # CREAR LAYOUT
    # ======================================================

    def _crear_layout(self):

        # --------------------------------------------------
        # HEADER
        # --------------------------------------------------

        self.header = Header(
            self
        )

        self.header.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="nsew"
        )

        # --------------------------------------------------
        # SIDEBAR
        # --------------------------------------------------

        self.sidebar = Sidebar(
            self,
            self.abrir_pdf,
            self.analizar_documento,
            self.generar_resumen,
            self.exportar_markdown,
            self.exportar_pdf,
            self.exportar_docx,
        )

        self.sidebar.grid(
            row=1,
            column=0,
            sticky="nsew"
        )

        # --------------------------------------------------
        # WORKSPACE
        # --------------------------------------------------

        self.workspace = Workspace(
            self
        )

        self.workspace.grid(
            row=1,
            column=1,
            sticky="nsew"
        )

        # --------------------------------------------------
        # STATUS BAR
        # --------------------------------------------------

        self.statusbar = StatusBar(
            self
        )

        self.statusbar.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="ew"
        )

    # ======================================================
    # ABRIR PDF
    # ======================================================

    def abrir_pdf(self):

        ruta = PDFService.seleccionar_pdf()

        if ruta is None:

            return

        try:

            self.statusbar.actualizar_estado(
                "Leyendo documento..."
            )

            documento = (
                DocumentController.cargar_documento(
                    ruta
                )
            )

            self.workspace.mostrar_pdf(
                documento
            )

            self.statusbar.actualizar_estado(
                "Documento listo"
            )

        except Exception as error:

            self.statusbar.actualizar_estado(
                "Error"
            )

            messagebox.showerror(
                "TechDocAI",
                str(error)
            )

    # ======================================================
    # ANALIZAR DOCUMENTO
    # ======================================================

    def analizar_documento(self):

        try:

            self.statusbar.actualizar_estado(
                "Consultando Groq..."
            )

            respuesta = (
                DocumentController
                .analizar_documento()
            )

            self.workspace.mostrar_respuesta_ia(
                respuesta
            )

            self.statusbar.actualizar_estado(
                "Análisis finalizado"
            )

        except Exception as error:

            messagebox.showerror(
                "TechDocAI",
                str(error)
            )

            self.statusbar.actualizar_estado(
                "Error"
            )

    # ======================================================
    # GENERAR RESUMEN
    # ======================================================

    def generar_resumen(self):

        try:

            self.statusbar.actualizar_estado(
                "Generando resumen ejecutivo..."
            )

            respuesta = (
                DocumentController
                .generar_resumen()
            )

            self.workspace.mostrar_respuesta_ia(
                respuesta
            )

            self.statusbar.actualizar_estado(
                "Resumen generado correctamente"
            )

        except Exception as error:

            messagebox.showerror(
                "TechDocAI",
                str(error)
            )

            self.statusbar.actualizar_estado(
                "Error"
            )

    # ======================================================
    # EXPORTAR MARKDOWN
    # ======================================================

    def exportar_markdown(self):

        try:

            ruta = (
                ExportService
                .exportar_markdown()
            )

            messagebox.showinfo(
                "TechDocAI",
                (
                    "Informe Markdown "
                    "exportado correctamente.\n\n"
                    f"Archivo:\n{ruta}"
                )
            )

            self.statusbar.actualizar_estado(
                "Markdown exportado"
            )

        except Exception as error:

            messagebox.showerror(
                "TechDocAI",
                str(error)
            )

            self.statusbar.actualizar_estado(
                "Error"
            )

    # ======================================================
    # EXPORTAR PDF
    # ======================================================

    def exportar_pdf(self):

        try:

            ruta = (
                ExportService
                .exportar_pdf()
            )

            messagebox.showinfo(
                "TechDocAI",
                (
                    "Informe PDF "
                    "exportado correctamente.\n\n"
                    f"Archivo:\n{ruta}"
                )
            )

            self.statusbar.actualizar_estado(
                "PDF exportado"
            )

        except Exception as error:

            messagebox.showerror(
                "TechDocAI",
                str(error)
            )

            self.statusbar.actualizar_estado(
                "Error"
            )

    # ======================================================
    # EXPORTAR DOCX
    # ======================================================

    def exportar_docx(self):

        try:

            ruta = (
                ExportService
                .exportar_docx()
            )

            messagebox.showinfo(
                "TechDocAI",
                (
                    "Informe DOCX "
                    "exportado correctamente.\n\n"
                    f"Archivo:\n{ruta}"
                )
            )

            self.statusbar.actualizar_estado(
                "DOCX exportado"
            )

        except Exception as error:

            messagebox.showerror(
                "TechDocAI",
                str(error)
            )

            self.statusbar.actualizar_estado(
                "Error"
            )