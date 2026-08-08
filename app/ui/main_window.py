from app.ui.header import Header
from app.ui.sidebar import Sidebar
from app.ui.workspace import Workspace
from app.ui.statusbar import StatusBar
from app.services.pdf_service import PDFService
from tkinter import messagebox
from app.core.text_processor import TextProcessor
from app.models.document import Document
from app.controllers.document_controller import DocumentController

"""
===========================================================
TechDocAI
Ventana principal
===========================================================
"""

import customtkinter as ctk

from config import (
    WINDOW_TITLE,
    APP_VERSION,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    THEME_MODE,
    COLOR_THEME,
    WINDOW_RESIZABLE,
)


class TechDocAIApp(ctk.CTk):
    """
    Ventana principal de TechDocAI.
    """

    def __init__(self):
        super().__init__()

        self._configurar_apariencia()
        self._configurar_ventana()
        self._crear_layout()

    def _configurar_apariencia(self):
        ctk.set_appearance_mode(THEME_MODE)
        ctk.set_default_color_theme(COLOR_THEME)

    def _configurar_ventana(self):

        self.title(f"{WINDOW_TITLE} v{APP_VERSION}")

        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.resizable(WINDOW_RESIZABLE, WINDOW_RESIZABLE)

        self.grid_rowconfigure(1, weight=1)

        self.grid_columnconfigure(1, weight=1)

        self._centrar()

    def _centrar(self):

        self.update_idletasks()

        ancho = WINDOW_WIDTH
        alto = WINDOW_HEIGHT

        pantalla_ancho = self.winfo_screenwidth()
        pantalla_alto = self.winfo_screenheight()

        x = int((pantalla_ancho - ancho) / 2)
        y = int((pantalla_alto - alto) / 2)

        self.geometry(f"{ancho}x{alto}+{x}+{y}")

    def _crear_layout(self):

        self.header = Header(self)

        self.header.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="nsew"
        )

        self.sidebar = Sidebar(
            self,
            self.abrir_pdf
        )

        self.sidebar.grid(
            row=1,
            column=0,
            sticky="nsew"
        )

        self.workspace = Workspace(self)

        self.workspace.grid(
            row=1,
            column=1,
            sticky="nsew"
        )

        self.statusbar = StatusBar(self)

        self.statusbar.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="ew"
        )

    def abrir_pdf(self):

        ruta = PDFService.seleccionar_pdf()

        if ruta is None:
            return

        try:

            self.statusbar.actualizar_estado(
                "Leyendo documento..."
            )

            documento = DocumentController.cargar_documento(
                ruta
            )

            self.workspace.mostrar_pdf(documento)

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