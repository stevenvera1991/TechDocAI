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

        self.titulo = ctk.CTkLabel(
            contenedor,
            text="Bienvenido a TechDocAI",
            font=("Segoe UI", 28, "bold")
        )

        self.titulo.pack(pady=(20, 10))

        self.descripcion = ctk.CTkLabel(
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

        self.descripcion.pack(pady=10)

        self.instrucciones = ctk.CTkLabel(
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

        self.instrucciones.pack(pady=(20, 0))

    def mostrar_pdf(self, documento):

        self.titulo.configure(
            text="Documento cargado correctamente"
        )

        self.descripcion.configure(
            text=f"📄 {documento.nombre}"
        )

        self.instrucciones.configure(
            text=(
                f"Páginas: {documento.paginas}\n"
                f"Tamaño: {documento.tamano_mb} MB\n"
                f"Caracteres: {documento.caracteres}\n"
                f"Palabras: {documento.palabras}\n"
                f"Líneas: {documento.lineas}\n\n"
                f"Chunks IA: {documento.chunks}\n"
                "Estado:\n"
                "✔ Documento cargado correctamente\n\n"
                "Listo para enviar a Groq."
            )
        )
    def limpiar(self):
        """
        Restablece el Workspace al estado inicial.
        """

        self.titulo.configure(
            text="Bienvenido a TechDocAI"
        )

        self.descripcion.configure(
            text="Seleccione un documento PDF para comenzar."
        )

        self.instrucciones.configure(
            text=""
        )

    def mostrar_respuesta_ia(self, respuesta):

        self.titulo.configure(
            text="Análisis generado por IA"
        )

        self.descripcion.configure(
            text="Respuesta del modelo Groq"
        )

        texto = respuesta

        if len(texto) > 3000:
            texto = texto[:3000] + "\n\n[...]"

        self.instrucciones.configure(
            text=texto
        )