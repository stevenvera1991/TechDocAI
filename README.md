# TechDocAI

**Intelligent Technical Document Analyzer**

TechDocAI es una aplicaciÃ³n de escritorio desarrollada en Python para el anÃ¡lisis inteligente de documentos tÃ©cnicos en formato PDF mediante inteligencia artificial.

El sistema permite cargar documentos PDF, extraer y procesar su contenido, dividir documentos extensos en fragmentos (*chunks*), enviarlos a un modelo de inteligencia artificial mediante la API de Groq, generar un informe tÃ©cnico consolidado y producir un resumen ejecutivo. AdemÃ¡s, permite exportar los resultados en formatos Markdown, PDF y DOCX.

---

## VersiÃ³n actual

**v0.6.1**

Esta versiÃ³n corresponde a la etapa de normalizaciÃ³n de configuraciÃ³n y dependencias del proyecto y ha sido validada mediante una instalaciÃ³n reproducida desde GitHub en un entorno virtual limpio.

### Estado

- AnÃ¡lisis de documentos PDF: operativo
- Procesamiento por chunks: operativo
- IntegraciÃ³n con Groq: operativa
- GeneraciÃ³n de informe consolidado: operativa
- GeneraciÃ³n de resumen ejecutivo: operativa
- ExportaciÃ³n Markdown: operativa
- ExportaciÃ³n PDF: operativa
- ExportaciÃ³n DOCX: operativa
- ReproducciÃ³n desde un clon limpio: validada

---

## CaracterÃ­sticas principales

TechDocAI incorpora las siguientes funcionalidades:

- SelecciÃ³n y carga de documentos PDF.
- ExtracciÃ³n del contenido textual del documento.
- ObtenciÃ³n de informaciÃ³n bÃ¡sica del documento:
  - nombre;
  - nÃºmero de pÃ¡ginas;
  - tamaÃ±o;
  - caracteres;
  - palabras;
  - lÃ­neas;
  - nÃºmero de chunks.
- DivisiÃ³n del contenido en chunks para su procesamiento mediante IA.
- AnÃ¡lisis individual de los chunks mediante Groq.
- ConsolidaciÃ³n de los resultados obtenidos.
- GeneraciÃ³n de un informe tÃ©cnico consolidado.
- GeneraciÃ³n de un resumen ejecutivo tÃ©cnico.
- ExportaciÃ³n del anÃ¡lisis en:
  - Markdown (`.md`);
  - PDF (`.pdf`);
  - Microsoft Word (`.docx`).
- Interfaz grÃ¡fica de escritorio desarrollada con CustomTkinter.
- Registro de eventos mediante sistema de logging.
- GestiÃ³n del historial de anÃ¡lisis.
- ConfiguraciÃ³n de credenciales mediante variables de entorno.
- SeparaciÃ³n entre cÃ³digo fuente y archivos generados.
- Estructura modular orientada a servicios.

---

## Arquitectura general

TechDocAI utiliza una arquitectura modular en la que la interfaz grÃ¡fica, los controladores, los modelos, los servicios y las utilidades se encuentran separados.

El flujo general de procesamiento es:

```text
                    USUARIO
                       â”‚
                       â–¼
              INTERFAZ GRÃFICA
                 CustomTkinter
                       â”‚
                       â–¼
                CONTROLADOR
                       â”‚
                       â–¼
              PROCESAMIENTO PDF
                       â”‚
                       â–¼
             EXTRACCIÃ“N DE TEXTO
                       â”‚
                       â–¼
                 DIVISIÃ“N EN
                   CHUNKS
                       â”‚
                       â–¼
                SERVICIO GROQ
                       â”‚
                       â–¼
             ANÃLISIS DE CADA
                    CHUNK
                       â”‚
                       â–¼
               CONSOLIDACIÃ“N
                  DEL ANÃLISIS
                       â”‚
             â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
             â–¼                   â–¼
      INFORME TÃ‰CNICO      RESUMEN EJECUTIVO
             â”‚                   â”‚
             â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                       â–¼
                 EXPORTACIÃ“N
                       â”‚
          â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
          â–¼            â–¼            â–¼
       Markdown        PDF         DOCX
```

---

## Requisitos

Para ejecutar TechDocAI se requiere:

- Windows u otro sistema compatible con Python.
- Python 3.
- Git.
- Acceso a Internet para utilizar la API de Groq.
- Una API key vÃ¡lida de Groq.

Las dependencias directas del proyecto estÃ¡n especificadas en:

```text
requirements.txt
```

---

## InstalaciÃ³n

### 1. Clonar el repositorio

Para reproducir la versiÃ³n actualmente validada:

```powershell
git clone --branch v0.6.1 https://github.com/stevenvera1991/TechDocAI.git
cd TechDocAI
```

TambiÃ©n puede clonarse la rama de desarrollo:

```powershell
git clone https://github.com/stevenvera1991/TechDocAI.git
cd TechDocAI
```

### 2. Crear el entorno virtual

Desde la carpeta raÃ­z del proyecto:

```powershell
python -m venv venv
```

### 3. Activar el entorno virtual

En Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Si la activaciÃ³n fue correcta, el terminal mostrarÃ¡ el entorno virtual activo:

```text
(venv)
```

### 4. Instalar las dependencias

Con el entorno virtual activo:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Verificar las dependencias

Comprobar que no existan conflictos entre las dependencias instaladas:

```powershell
python -m pip check
```

El resultado esperado es:

```text
No broken requirements found.
```

---

## ConfiguraciÃ³n de la API de Groq

TechDocAI utiliza Groq como proveedor de inteligencia artificial para realizar el anÃ¡lisis de los documentos.

### 1. Crear el archivo `.env`

El archivo `.env` debe ubicarse en la carpeta raÃ­z del proyecto:

```text
TechDocAI/
â”œâ”€â”€ .env
â”œâ”€â”€ config.py
â”œâ”€â”€ main.py
â”œâ”€â”€ requirements.txt
â””â”€â”€ ...
```

### 2. Configurar la API key

Dentro del archivo `.env`, agregar la variable:

```text
GROQ_API_KEY=tu_clave_de_groq
```

Reemplazar `tu_clave_de_groq` por una API key vÃ¡lida de Groq.

### 3. Seguridad de la API key

La API key no debe escribirse directamente en el cÃ³digo fuente.

El archivo `.env` se encuentra incluido en `.gitignore`, por lo que no debe formar parte del repositorio Git.

No se debe publicar la API key en:

- GitHub.
- Capturas de pantalla.
- DocumentaciÃ³n pÃºblica.
- Archivos fuente.
- Mensajes de commit.

Si una API key se expone accidentalmente, debe revocarse y sustituirse por una nueva.

### 4. VerificaciÃ³n de la configuraciÃ³n

Una vez creada la variable `GROQ_API_KEY`, ejecutar TechDocAI con el entorno virtual activo:

```powershell
python main.py
```

Si la configuraciÃ³n es correcta, la aplicaciÃ³n podrÃ¡ comunicarse con el servicio de Groq durante el anÃ¡lisis de los documentos.

### Proveedor y modelo

La configuraciÃ³n actual utiliza:

```text
Proveedor: Groq
Modelo: llama-3.3-70b-versatile
```

Los parÃ¡metros de configuraciÃ³n del proveedor se encuentran centralizados en `config.py`.

---

## EjecuciÃ³n

Con el entorno virtual activo y la API key de Groq configurada, iniciar la aplicaciÃ³n desde la carpeta raÃ­z del proyecto:

```powershell
python main.py
```

La aplicaciÃ³n abrirÃ¡ la interfaz grÃ¡fica de TechDocAI.

### Inicio de la aplicaciÃ³n

El punto de entrada principal del sistema es:

```text
main.py
```

Este archivo inicia la aplicaciÃ³n y carga la interfaz grÃ¡fica principal.

### Registro de ejecuciÃ³n

TechDocAI utiliza un sistema de logging para registrar eventos relevantes durante la ejecuciÃ³n.

Los registros permiten realizar seguimiento de:

- carga de documentos;
- procesamiento de informaciÃ³n;
- operaciones realizadas por los servicios;
- generaciÃ³n de resultados;
- errores o eventos relevantes.

Los archivos de log se almacenan localmente y estÃ¡n excluidos del control de versiones mediante `.gitignore`.

### DetenciÃ³n de la aplicaciÃ³n

Para finalizar la ejecuciÃ³n, cerrar la ventana principal de TechDocAI de forma normal.

---

## Flujo de uso

El uso de TechDocAI se realiza mediante la interfaz grÃ¡fica siguiendo una secuencia de operaciones.

### 1. Seleccionar un documento

Utilizar la opciÃ³n de apertura de archivos para seleccionar el documento PDF que se desea analizar.

### 2. Cargar el documento

TechDocAI carga el archivo seleccionado y presenta informaciÃ³n bÃ¡sica del documento, incluyendo:

- nombre del archivo;
- nÃºmero de pÃ¡ginas;
- tamaÃ±o;
- informaciÃ³n del contenido;
- nÃºmero de chunks generados.

### 3. Analizar el documento

Seleccionar:

**Analizar Documento**

El sistema procesa el contenido del PDF mediante el flujo de anÃ¡lisis implementado y utiliza Groq para generar los resultados correspondientes.

### 4. Generar el resumen ejecutivo

Una vez disponible el anÃ¡lisis consolidado, seleccionar:

**Generar Resumen**

TechDocAI genera un resumen ejecutivo tÃ©cnico basado en la informaciÃ³n obtenida durante el anÃ¡lisis.

### 5. Revisar los resultados

El usuario puede revisar el informe y el resumen generados desde la interfaz antes de realizar la exportaciÃ³n.

### 6. Exportar los resultados

El usuario puede seleccionar el formato de salida requerido:

- **Exportar Markdown**
- **Exportar PDF**
- **Exportar DOCX**

Los archivos generados se almacenan en:

```text
exports/
```

### Flujo general

```text
Seleccionar documento PDF
          â†“
      Cargar PDF
          â†“
   Analizar documento
          â†“
 Generar resultados
          â†“
Generar resumen ejecutivo
          â†“
   Revisar resultados
          â†“
       Exportar
          â†“
 Markdown / PDF / DOCX
```

---

## ExportaciÃ³n de resultados

TechDocAI permite exportar los resultados del anÃ¡lisis en diferentes formatos para facilitar su consulta, almacenamiento y utilizaciÃ³n posterior.

### Exportar en Markdown

La opciÃ³n **Exportar Markdown** genera un archivo de texto estructurado en formato Markdown (`.md`).

Este formato permite conservar la estructura del informe y facilita su lectura, ediciÃ³n y reutilizaciÃ³n en diferentes herramientas compatibles con Markdown.

### Exportar en PDF

La opciÃ³n **Exportar PDF** genera un documento en formato PDF mediante ReportLab.

Este formato estÃ¡ orientado a la presentaciÃ³n y distribuciÃ³n del informe tÃ©cnico en un documento de salida independiente.

### Exportar en DOCX

La opciÃ³n **Exportar DOCX** genera un documento compatible con Microsoft Word (`.docx`).

Este formato permite editar posteriormente el contenido del informe mediante aplicaciones compatibles con documentos de Word.

### UbicaciÃ³n de los archivos

Los archivos generados por TechDocAI se almacenan en la carpeta:

```text
exports/
```

La carpeta `exports/` estÃ¡ excluida del control de versiones mediante `.gitignore`, por lo que los documentos generados localmente no se incorporan al repositorio Git.

### Formatos disponibles

| Formato | ExtensiÃ³n | Uso principal |
|---|---|---|
| Markdown | `.md` | Lectura, ediciÃ³n y reutilizaciÃ³n del informe |
| PDF | `.pdf` | PresentaciÃ³n y distribuciÃ³n |
| Microsoft Word | `.docx` | EdiciÃ³n posterior del documento |

---

## Procesamiento por chunks

Para procesar documentos de mayor extensiÃ³n, TechDocAI divide el contenido textual extraÃ­do del PDF en fragmentos denominados *chunks*.

### Flujo de procesamiento

El procesamiento sigue la siguiente secuencia:

```text
Documento PDF
      â†“
ExtracciÃ³n de texto
      â†“
DivisiÃ³n del contenido
      â†“
GeneraciÃ³n de chunks
      â†“
AnÃ¡lisis individual de cada chunk
      â†“
ConsolidaciÃ³n de resultados
      â†“
Informe tÃ©cnico
```

Cada chunk es procesado de manera individual mediante el servicio de inteligencia artificial configurado en TechDocAI.

### Procesamiento individual

El sistema procesa los fragmentos de forma secuencial:

```text
Chunk 1 â†’ Groq
Chunk 2 â†’ Groq
Chunk 3 â†’ Groq
   ...
Chunk N â†’ Groq
```

Los resultados obtenidos de los diferentes chunks se utilizan posteriormente para generar un anÃ¡lisis consolidado del documento.

### Ventajas del procesamiento por chunks

Esta estrategia permite:

- trabajar con documentos de mayor extensiÃ³n;
- dividir el contenido en unidades de procesamiento controlables;
- procesar cada fragmento de manera individual;
- consolidar posteriormente los resultados obtenidos.

El nÃºmero de chunks depende del contenido y de la configuraciÃ³n utilizada por el procesador de texto de TechDocAI.

---

## Arquitectura del proyecto

TechDocAI estÃ¡ organizado mediante una estructura modular que separa la interfaz grÃ¡fica, la lÃ³gica de procesamiento, los modelos de datos, los servicios y las utilidades.

La estructura principal del proyecto es:

```text
TechDocAI/
â”‚
â”œâ”€â”€ app/
â”‚   â”œâ”€â”€ config/
â”‚   â”‚   â””â”€â”€ __init__.py
â”‚   â”‚
â”‚   â”œâ”€â”€ controllers/
â”‚   â”‚   â”œâ”€â”€ __init__.py
â”‚   â”‚   â””â”€â”€ document_controller.py
â”‚   â”‚
â”‚   â”œâ”€â”€ core/
â”‚   â”‚   â”œâ”€â”€ __init__.py
â”‚   â”‚   â””â”€â”€ text_processor.py
â”‚   â”‚
â”‚   â”œâ”€â”€ models/
â”‚   â”‚   â”œâ”€â”€ __init__.py
â”‚   â”‚   â””â”€â”€ document.py
â”‚   â”‚
â”‚   â”œâ”€â”€ services/
â”‚   â”‚   â”œâ”€â”€ __init__.py
â”‚   â”‚   â”œâ”€â”€ export_service.py
â”‚   â”‚   â”œâ”€â”€ groq_service.py
â”‚   â”‚   â”œâ”€â”€ history_service.py
â”‚   â”‚   â””â”€â”€ pdf_service.py
â”‚   â”‚
â”‚   â”œâ”€â”€ ui/
â”‚   â”‚   â”œâ”€â”€ __init__.py
â”‚   â”‚   â”œâ”€â”€ header.py
â”‚   â”‚   â”œâ”€â”€ main_window.py
â”‚   â”‚   â”œâ”€â”€ sidebar.py
â”‚   â”‚   â”œâ”€â”€ statusbar.py
â”‚   â”‚   â””â”€â”€ workspace.py
â”‚   â”‚
â”‚   â””â”€â”€ utils/
â”‚       â”œâ”€â”€ __init__.py
â”‚       â””â”€â”€ logger.py
â”‚
â”œâ”€â”€ docs/
â”‚   â””â”€â”€ arquitectura/
â”‚       â””â”€â”€ README.md
â”‚
â”œâ”€â”€ prompts/
â”‚   â””â”€â”€ resumen.txt
â”‚
â”œâ”€â”€ tests/
â”‚   â””â”€â”€ test_history.py
â”‚
â”œâ”€â”€ config.py
â”œâ”€â”€ main.py
â”œâ”€â”€ VERSION
â”œâ”€â”€ requirements.txt
â”œâ”€â”€ CHANGELOG.md
â”œâ”€â”€ CONTRIBUTING.md
â”œâ”€â”€ LICENSE
â”œâ”€â”€ README.md
â”œâ”€â”€ .gitignore
â”‚
â”œâ”€â”€ test_controller_resumen.py
â”œâ”€â”€ test_export_docx.py
â”œâ”€â”€ test_export_pdf.py
â”œâ”€â”€ test_generar_resumen.py
â””â”€â”€ test_groq.py
```

### Componentes principales

#### `app/controllers/`

Contiene los controladores responsables de coordinar las acciones realizadas sobre los documentos y conectar la interfaz con la lÃ³gica de procesamiento.

#### `app/core/`

Contiene la lÃ³gica central relacionada con el procesamiento y transformaciÃ³n del texto extraÃ­do de los documentos.

#### `app/models/`

Contiene los modelos utilizados para representar la informaciÃ³n de los documentos procesados.

#### `app/services/`

Contiene los servicios principales de la aplicaciÃ³n:

- `pdf_service.py`: procesamiento y extracciÃ³n de informaciÃ³n de documentos PDF.
- `groq_service.py`: comunicaciÃ³n con el servicio de inteligencia artificial de Groq.
- `export_service.py`: generaciÃ³n y exportaciÃ³n de los resultados.
- `history_service.py`: gestiÃ³n del historial de anÃ¡lisis.

#### `app/ui/`

Contiene los componentes de la interfaz grÃ¡fica de TechDocAI:

- encabezado;
- ventana principal;
- barra lateral;
- barra de estado;
- Ã¡rea de trabajo.

La interfaz estÃ¡ desarrollada utilizando CustomTkinter.

#### `app/utils/`

Contiene utilidades generales utilizadas por diferentes componentes de la aplicaciÃ³n, incluyendo el sistema de logging.

#### `prompts/`

Contiene los archivos de instrucciones utilizados para orientar la generaciÃ³n de determinados resultados mediante inteligencia artificial.

#### `tests/`

Contiene pruebas asociadas a funcionalidades especÃ­ficas del proyecto.

#### `docs/`

Contiene documentaciÃ³n tÃ©cnica complementaria del proyecto, incluyendo la documentaciÃ³n detallada de arquitectura.

#### Archivos principales

- `main.py`: punto de entrada de la aplicaciÃ³n.
- `config.py`: configuraciÃ³n general del proyecto y del proveedor de IA.
- `VERSION`: versiÃ³n actual de TechDocAI.
- `requirements.txt`: dependencias directas del proyecto.
- `.gitignore`: archivos y directorios excluidos del control de versiones.
- `README.md`: documentaciÃ³n general del proyecto.
- `CHANGELOG.md`: historial de cambios entre versiones.
- `CONTRIBUTING.md`: directrices de contribuciÃ³n.
- `LICENSE`: archivo destinado a documentar la licencia del proyecto.

---

## Dependencias principales

TechDocAI utiliza un conjunto de dependencias directas necesarias para la interfaz grÃ¡fica, el procesamiento de documentos, la integraciÃ³n con inteligencia artificial y la generaciÃ³n de archivos de salida.

Las dependencias principales y sus versiones utilizadas en la versiÃ³n `v0.6.1` son:

```text
customtkinter==6.0.0
groq==1.6.0
PyPDF2==3.0.1
python-dotenv==1.2.2
Pillow==12.3.0
reportlab==5.0.0
python-docx==1.2.0
```

### FunciÃ³n de las principales dependencias

| Dependencia | FunciÃ³n |
|---|---|
| `customtkinter` | Desarrollo de la interfaz grÃ¡fica de escritorio. |
| `groq` | ComunicaciÃ³n con la API de Groq para el procesamiento mediante inteligencia artificial. |
| `PyPDF2` | Lectura y extracciÃ³n de contenido de documentos PDF. |
| `python-dotenv` | Carga de variables de entorno desde el archivo `.env`. |
| `Pillow` | Procesamiento y gestiÃ³n de imÃ¡genes utilizadas por la aplicaciÃ³n. |
| `reportlab` | GeneraciÃ³n de documentos PDF. |
| `python-docx` | GeneraciÃ³n de documentos Microsoft Word (`.docx`). |

### GestiÃ³n de dependencias

Las dependencias directas del proyecto se encuentran declaradas en:

```text
requirements.txt
```

El archivo mantiene las versiones utilizadas para facilitar la reproducciÃ³n del entorno de ejecuciÃ³n.

Las dependencias transitivas son instaladas automÃ¡ticamente por `pip` cuando son requeridas por las bibliotecas principales y no necesitan ser declaradas individualmente en `requirements.txt` cuando no son utilizadas directamente por el cÃ³digo de TechDocAI.

### VerificaciÃ³n del entorno

Para comprobar que las dependencias instaladas no presentan conflictos se puede ejecutar:

```powershell
python -m pip check
```

El resultado esperado es:

```text
No broken requirements found.
```

TambiÃ©n puede verificarse la instalaciÃ³n de las dependencias mediante:

```powershell
python -m pip freeze
```

La versiÃ³n `v0.6.1` fue validada mediante la instalaciÃ³n de las dependencias desde `requirements.txt` en un entorno virtual independiente.

---

## ConfiguraciÃ³n del proyecto

Los principales parÃ¡metros de configuraciÃ³n de TechDocAI se encuentran centralizados en el archivo:

```text
config.py
```

Este archivo contiene la configuraciÃ³n general de la aplicaciÃ³n y de los servicios utilizados por el sistema.

### InformaciÃ³n de la aplicaciÃ³n

La configuraciÃ³n incluye:

- nombre de la aplicaciÃ³n;
- versiÃ³n actual;
- autor;
- curso;
- instituciÃ³n.

La versiÃ³n definida actualmente es:

```text
0.6.1
```

y se mantiene sincronizada con el archivo:

```text
VERSION
```

### ConfiguraciÃ³n del proveedor de IA

TechDocAI utiliza Groq como proveedor de inteligencia artificial.

La configuraciÃ³n incluye:

```text
Proveedor: Groq
Modelo: llama-3.3-70b-versatile
```

Los parÃ¡metros especÃ­ficos de Groq se encuentran definidos en `config.py`.

La API key no se almacena directamente en este archivo. Se obtiene mediante la variable de entorno:

```text
GROQ_API_KEY
```

### ConfiguraciÃ³n de la interfaz

El archivo `config.py` tambiÃ©n contiene parÃ¡metros relacionados con la interfaz grÃ¡fica, incluyendo:

- tÃ­tulo de la ventana;
- ancho;
- alto;
- posibilidad de redimensionamiento;
- modo de apariencia;
- tema de color.

### Rutas del proyecto

La configuraciÃ³n establece las rutas utilizadas por los diferentes componentes de TechDocAI.

Entre ellas se encuentran las rutas correspondientes a:

- directorio base;
- documentos PDF;
- resultados;
- prompts;
- registros de ejecuciÃ³n;
- pruebas.

La centralizaciÃ³n de estas configuraciones permite que los diferentes mÃ³dulos de la aplicaciÃ³n utilicen una referencia comÃºn para los recursos del proyecto.

---

## Seguridad y archivos excluidos

TechDocAI utiliza un archivo `.gitignore` para evitar que informaciÃ³n sensible, archivos temporales, entornos locales y resultados generados sean incorporados al repositorio.

### Archivos y directorios excluidos

Entre los principales elementos excluidos se encuentran:

```text
venv/
.env
__pycache__/
*.py[cod]
*$py.class
logs/*.log
.vscode/
*.tmp
*.bak
*.swp
Thumbs.db
.DS_Store
exports/
historial/
```

### Variables de entorno

El archivo `.env` contiene las variables de entorno utilizadas por la aplicaciÃ³n, incluyendo la API key de Groq.

Por seguridad, `.env` no debe incorporarse al repositorio.

La configuraciÃ³n se realiza mediante:

```text
GROQ_API_KEY=tu_clave_de_groq
```

### Entorno virtual

El directorio `venv/` contiene el entorno virtual local utilizado para ejecutar TechDocAI.

Este directorio no se versiona porque el entorno puede reconstruirse mediante:

```powershell
python -m venv venv
python -m pip install -r requirements.txt
```

### Archivos generados

Los directorios `exports/` e `historial/` contienen informaciÃ³n generada durante la utilizaciÃ³n de la aplicaciÃ³n.

Estos archivos son especÃ­ficos de cada entorno de ejecuciÃ³n y no forman parte del cÃ³digo fuente versionado.

### Registros

Los archivos de registro generados durante la ejecuciÃ³n se almacenan localmente y se excluyen del repositorio mediante:

```text
logs/*.log
```

### ProtecciÃ³n de credenciales

Las credenciales y claves de acceso no deben almacenarse directamente en los archivos fuente ni incluirse en commits.

Antes de realizar un commit, se debe comprobar que no existan archivos sensibles o credenciales dentro de los cambios pendientes.

---

## Reproducibilidad

La versiÃ³n `v0.6.1` de TechDocAI fue validada mediante la reproducciÃ³n del proyecto desde un clon limpio del repositorio.

El objetivo de esta validaciÃ³n es comprobar que otra instalaciÃ³n puede reconstruir el entorno de ejecuciÃ³n utilizando Ãºnicamente el repositorio, las dependencias declaradas y la configuraciÃ³n de la API.

### Procedimiento de reproducciÃ³n

El proceso utilizado fue:

```text
Repositorio GitHub
       â†“
Clon de la versiÃ³n v0.6.1
       â†“
CreaciÃ³n de un nuevo entorno virtual
       â†“
InstalaciÃ³n de requirements.txt
       â†“
ConfiguraciÃ³n de la API de Groq
       â†“
VerificaciÃ³n de dependencias
       â†“
VerificaciÃ³n de compilaciÃ³n
       â†“
EjecuciÃ³n de TechDocAI
       â†“
Prueba funcional
```

### Clon de la versiÃ³n validada

La versiÃ³n especÃ­fica puede obtenerse mediante:

```powershell
git clone --branch v0.6.1 https://github.com/stevenvera1991/TechDocAI.git TechDocAI-REPRO
cd TechDocAI-REPRO
```

### CreaciÃ³n del entorno

Desde la carpeta del proyecto:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### InstalaciÃ³n de dependencias

Con el entorno virtual activo:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### VerificaciÃ³n de dependencias

Comprobar que no existan conflictos:

```powershell
python -m pip check
```

Resultado esperado:

```text
No broken requirements found.
```

### VerificaciÃ³n de compilaciÃ³n

Comprobar que los mÃ³dulos principales puedan compilarse correctamente:

```powershell
python -m compileall -f app config.py main.py
```

### ConfiguraciÃ³n de la API

Crear el archivo `.env` en la raÃ­z del proyecto y configurar una API key vÃ¡lida de Groq:

```text
GROQ_API_KEY=tu_clave_de_groq
```

La API key es especÃ­fica del entorno de ejecuciÃ³n y no forma parte del repositorio.

### ValidaciÃ³n funcional

Una vez configurado el entorno, ejecutar:

```powershell
python main.py
```

La versiÃ³n `v0.6.1` fue validada mediante:

- clon del repositorio;
- creaciÃ³n de un entorno virtual independiente;
- instalaciÃ³n desde `requirements.txt`;
- verificaciÃ³n de dependencias;
- verificaciÃ³n de compilaciÃ³n;
- configuraciÃ³n de la API de Groq;
- ejecuciÃ³n de la aplicaciÃ³n;
- carga de un documento PDF;
- anÃ¡lisis mediante Groq;
- generaciÃ³n del informe consolidado;
- generaciÃ³n del resumen ejecutivo;
- exportaciÃ³n de resultados.

Esta validaciÃ³n confirma la reproducibilidad funcional de `v0.6.1` bajo las condiciones utilizadas durante las pruebas.

---

## ValidaciÃ³n tÃ©cnica

La versiÃ³n `v0.6.1` fue sometida a diferentes comprobaciones tÃ©cnicas antes y durante la validaciÃ³n funcional.

### VerificaciÃ³n de dependencias

Se comprobÃ³ que las dependencias instaladas no presentaran conflictos mediante:

```powershell
python -m pip check
```

Resultado obtenido:

```text
No broken requirements found.
```

### VerificaciÃ³n de compilaciÃ³n

Se comprobÃ³ la compilaciÃ³n de los mÃ³dulos principales de Python mediante:

```powershell
python -m compileall -f app config.py main.py
```

La compilaciÃ³n se completÃ³ correctamente para los mÃ³dulos del proyecto.

### VerificaciÃ³n del cÃ³digo

TambiÃ©n se realizÃ³ una comprobaciÃ³n de formato de diferencias mediante:

```powershell
git diff --check
```

La comprobaciÃ³n no reportÃ³ errores de espacios en blanco ni problemas de formato en los cambios realizados.

### VerificaciÃ³n funcional

La aplicaciÃ³n fue ejecutada mediante:

```powershell
python main.py
```

Durante la prueba funcional se verificÃ³ el procesamiento de un documento PDF mediante el siguiente flujo:

```text
Carga del documento
        â†“
ExtracciÃ³n del contenido
        â†“
GeneraciÃ³n de chunks
        â†“
Procesamiento mediante Groq
        â†“
GeneraciÃ³n del informe consolidado
        â†“
GeneraciÃ³n del resumen ejecutivo
        â†“
ExportaciÃ³n de resultados
```

La integraciÃ³n con Groq respondiÃ³ correctamente durante las pruebas realizadas.

### Resultado de la validaciÃ³n

Las comprobaciones realizadas permitieron verificar:

- integridad de las dependencias;
- compilaciÃ³n correcta de los mÃ³dulos principales;
- ausencia de errores de formato en los cambios revisados;
- ejecuciÃ³n correcta de la aplicaciÃ³n;
- comunicaciÃ³n con la API de Groq;
- procesamiento de documentos PDF;
- generaciÃ³n del informe consolidado;
- generaciÃ³n del resumen ejecutivo;
- funcionamiento de las opciones de exportaciÃ³n.

Estas comprobaciones forman parte de la validaciÃ³n tÃ©cnica de la versiÃ³n `v0.6.1`.

---

## EvoluciÃ³n del proyecto

TechDocAI fue desarrollado de manera incremental mediante diferentes etapas de implementaciÃ³n, validaciÃ³n y limpieza del proyecto.

### v0.2.0

IntroducciÃ³n del modelo de dominio `Document` y consolidaciÃ³n de la arquitectura inicial de gestiÃ³n documental.

TambiÃ©n se incorporaron componentes relacionados con la configuraciÃ³n de la integraciÃ³n con Groq y el procesamiento de documentos mediante inteligencia artificial.

### v0.3.0

ConsolidaciÃ³n del flujo de anÃ¡lisis de documentos mediante inteligencia artificial y evoluciÃ³n de los componentes principales de procesamiento.

### v0.4.0

ImplementaciÃ³n de la exportaciÃ³n y gestiÃ³n de reportes, incorporando los mecanismos necesarios para generar documentos de salida.

### v0.5.0

ImplementaciÃ³n de la generaciÃ³n del resumen ejecutivo a partir del anÃ¡lisis consolidado.

### v0.6.0

Limpieza integral del proyecto y eliminaciÃ³n controlada de componentes obsoletos o que ya no formaban parte del flujo funcional.

### v0.6.1

CorrecciÃ³n y normalizaciÃ³n de la configuraciÃ³n del proyecto y de sus dependencias.

Esta versiÃ³n tambiÃ©n fue sometida a una validaciÃ³n de reproducibilidad mediante la creaciÃ³n de un entorno independiente a partir de un clon del repositorio.

### Estado de la evoluciÃ³n

La evoluciÃ³n del proyecto ha permitido pasar progresivamente de una estructura inicial de anÃ¡lisis documental a un MVP funcional capaz de:

- cargar documentos PDF;
- procesar su contenido;
- utilizar inteligencia artificial mediante Groq;
- consolidar resultados;
- generar un resumen ejecutivo;
- exportar informes en diferentes formatos;
- mantener una estructura modular;
- reproducir el entorno de ejecuciÃ³n mediante dependencias declaradas.

---

## Control de versiones

TechDocAI utiliza Git para el control de versiones y GitHub como repositorio remoto del proyecto.

El desarrollo se ha organizado mediante commits y etiquetas (*tags*) para identificar versiones funcionales y facilitar la trazabilidad de los cambios.

### Rama de desarrollo

La rama utilizada para el desarrollo principal del proyecto es:

```text
develop
```

Los cambios se incorporan mediante commits descriptivos y se verifican antes de ser publicados en el repositorio remoto.

### Versiones etiquetadas

Las principales versiones identificadas durante la evoluciÃ³n del proyecto son:

```text
v0.2.0
v0.3.0
v0.4.0
v0.5.0
v0.6.0
v0.6.1
```

Cada etiqueta permite identificar un estado especÃ­fico del proyecto y facilita la reproducciÃ³n de una versiÃ³n determinada.

### VersiÃ³n actual

La versiÃ³n actualmente validada es:

```text
v0.6.1
```

Esta versiÃ³n se encuentra sincronizada entre:

```text
VERSION
```

y:

```python
APP_VERSION = "0.6.1"
```

El tag `v0.6.1` identifica el estado del cÃ³digo utilizado durante la validaciÃ³n de reproducibilidad.

### ReproducciÃ³n de una versiÃ³n especÃ­fica

Para obtener directamente la versiÃ³n `v0.6.1` desde GitHub:

```powershell
git clone --branch v0.6.1 https://github.com/stevenvera1991/TechDocAI.git
```

De esta manera se puede reconstruir el entorno correspondiente a una versiÃ³n concreta sin depender del estado posterior de la rama de desarrollo.

### PrÃ³xima versiÃ³n de entrega

La siguiente versiÃ³n se definirÃ¡ una vez completadas las etapas pendientes del proyecto, incluyendo:

- documentaciÃ³n final;
- empaquetamiento de la aplicaciÃ³n;
- validaciÃ³n final del paquete de entrega;
- preparaciÃ³n de los materiales de presentaciÃ³n.

La numeraciÃ³n de la prÃ³xima versiÃ³n se establecerÃ¡ de acuerdo con los cambios que finalmente se incorporen al proyecto.

---

## Desarrollo

El desarrollo de TechDocAI se organiza mediante una estructura modular y un flujo de trabajo basado en control de versiones.

### OrganizaciÃ³n del desarrollo

Las nuevas funcionalidades y modificaciones deben realizarse de manera controlada, procurando mantener separadas las diferentes responsabilidades del sistema.

Antes de incorporar cambios al proyecto se recomienda:

1. Implementar la modificaciÃ³n.
2. Ejecutar las pruebas correspondientes.
3. Verificar la compilaciÃ³n de los mÃ³dulos.
4. Comprobar las dependencias.
5. Revisar los cambios mediante Git.
6. Crear un commit descriptivo.
7. Publicar los cambios en el repositorio remoto cuando corresponda.

### Rama de desarrollo

La rama principal utilizada durante el desarrollo es:

```text
develop
```

Los cambios realizados durante la construcciÃ³n del proyecto se integran progresivamente en esta rama.

### Commits

Los commits deben utilizar mensajes descriptivos que permitan identificar claramente el cambio realizado.

Ejemplo:

```powershell
git add .
git commit -m "DescripciÃ³n del cambio"
```

### VerificaciÃ³n antes de un commit

Se recomienda comprobar el estado del repositorio mediante:

```powershell
git status
```

TambiÃ©n puede revisarse la diferencia de los archivos modificados mediante:

```powershell
git diff
```

Y comprobar posibles problemas de espacios en blanco mediante:

```powershell
git diff --check
```

### PublicaciÃ³n de cambios

Una vez verificados los cambios, pueden publicarse en el repositorio remoto mediante:

```powershell
git push origin develop
```

El flujo de desarrollo debe mantener el repositorio en un estado funcional y reproducible.

---

## Pruebas

TechDocAI incorpora diferentes archivos de prueba destinados a verificar funcionalidades especÃ­ficas de la aplicaciÃ³n.

### Pruebas disponibles

Entre los archivos de prueba incluidos en el proyecto se encuentran:

```text
test_controller_resumen.py
test_export_docx.py
test_export_pdf.py
test_generar_resumen.py
test_groq.py
tests/test_history.py
```

Estas pruebas cubren diferentes componentes relacionados con:

- generaciÃ³n del resumen;
- comunicaciÃ³n con Groq;
- exportaciÃ³n a PDF;
- exportaciÃ³n a DOCX;
- gestiÃ³n del historial.

### VerificaciÃ³n de compilaciÃ³n

AdemÃ¡s de las pruebas funcionales, se puede comprobar que los mÃ³dulos principales de Python puedan compilarse correctamente mediante:

```powershell
python -m compileall -f app config.py main.py
```

### VerificaciÃ³n de dependencias

La integridad de las dependencias instaladas puede comprobarse mediante:

```powershell
python -m pip check
```

El resultado esperado es:

```text
No broken requirements found.
```

### VerificaciÃ³n del repositorio

Antes de publicar cambios se recomienda comprobar el estado del repositorio:

```powershell
git status
```

TambiÃ©n puede verificarse la integridad de los cambios mediante:

```powershell
git diff --check
```

### ValidaciÃ³n funcional

La validaciÃ³n funcional de `v0.6.1` incluyÃ³ la ejecuciÃ³n de TechDocAI y el procesamiento de un documento PDF mediante Groq.

Durante esta validaciÃ³n se comprobÃ³ el flujo principal de la aplicaciÃ³n:

```text
Carga del documento
        â†“
Procesamiento del PDF
        â†“
AnÃ¡lisis mediante Groq
        â†“
GeneraciÃ³n del informe
        â†“
GeneraciÃ³n del resumen ejecutivo
        â†“
ExportaciÃ³n de resultados
```

Estas comprobaciones complementan las pruebas especÃ­ficas y permiten verificar el funcionamiento general del MVP.

---

## Limitaciones actuales

La versiÃ³n `v0.6.1` constituye un MVP funcional y reproducible de TechDocAI. Sin embargo, existen aspectos que pueden continuar desarrollÃ¡ndose en versiones posteriores.

### Limitaciones de procesamiento

- El procesamiento de documentos extensos depende de la divisiÃ³n del contenido en *chunks*.
- El tiempo de procesamiento puede aumentar segÃºn la cantidad de chunks generados.
- El procesamiento mediante la API de Groq estÃ¡ sujeto a los lÃ­mites y condiciones del servicio utilizado.
- La calidad de los resultados depende del contenido y calidad del documento PDF analizado.

### Limitaciones de la versiÃ³n actual

La versiÃ³n `v0.6.1` no constituye todavÃ­a una versiÃ³n final empaquetada como aplicaciÃ³n distribuible independiente.

Entre las funcionalidades que pueden desarrollarse posteriormente se encuentran:

- empaquetamiento de la aplicaciÃ³n para distribuciÃ³n;
- automatizaciÃ³n del proceso de instalaciÃ³n;
- ampliaciÃ³n de las pruebas automatizadas;
- mejoras adicionales de la interfaz grÃ¡fica;
- optimizaciÃ³n del procesamiento de documentos extensos;
- manejo mÃ¡s avanzado de lÃ­mites y errores de la API;
- incorporaciÃ³n de nuevos proveedores o modelos de inteligencia artificial;
- ampliaciÃ³n de las capacidades de anÃ¡lisis tÃ©cnico.

Estas funcionalidades forman parte de posibles etapas futuras y no deben considerarse como caracterÃ­sticas garantizadas de `v0.6.1`.

### Alcance del MVP

El MVP actual se centra en proporcionar un flujo funcional para:

```text
Carga de PDF
      â†“
Procesamiento del documento
      â†“
AnÃ¡lisis mediante IA
      â†“
ConsolidaciÃ³n de resultados
      â†“
Resumen ejecutivo
      â†“
ExportaciÃ³n
```

La ampliaciÃ³n de funcionalidades se realizarÃ¡ de manera progresiva en las siguientes versiones del proyecto.

---

## Autor

**Steven Vera**

TechDocAI fue desarrollado como proyecto del curso:

**Python + IA**

InstituciÃ³n:

**Institute Technology Bertoni**

---

## Licencia

La informaciÃ³n correspondiente a la licencia del proyecto se encuentra en el archivo:

```text
LICENSE
```

La licencia aplicable a TechDocAI deberÃ¡ consultarse directamente en dicho archivo.

---

## Estado final del proyecto

**TechDocAI v0.6.1 â€” MVP funcional y reproducible**

La versiÃ³n `v0.6.1` representa el estado actualmente validado del proyecto.

El MVP permite:

- cargar documentos PDF;
- extraer y procesar su contenido;
- dividir documentos en *chunks*;
- analizar el contenido mediante Groq;
- generar un informe tÃ©cnico consolidado;
- generar un resumen ejecutivo;
- exportar resultados en Markdown, PDF y DOCX;
- mantener un historial de anÃ¡lisis;
- utilizar una configuraciÃ³n mediante variables de entorno;
- reproducir el entorno de ejecuciÃ³n mediante las dependencias declaradas.

La versiÃ³n `v0.6.1` fue validada mediante un clon independiente del repositorio, creaciÃ³n de un entorno virtual, instalaciÃ³n de las dependencias, configuraciÃ³n de la API de Groq, ejecuciÃ³n de la aplicaciÃ³n y procesamiento funcional de un documento PDF.

### Estado de la versiÃ³n

```text
VersiÃ³n: v0.6.1
Estado: MVP funcional y reproducible
Proveedor de IA: Groq
Modelo: llama-3.3-70b-versatile
```

### Siguiente etapa

Con la validaciÃ³n del MVP completada, el proyecto puede avanzar hacia las siguientes etapas de entrega:

- documentaciÃ³n tÃ©cnica final;
- documentaciÃ³n de arquitectura;
- preparaciÃ³n del empaquetamiento;
- validaciÃ³n del paquete de distribuciÃ³n;
- preparaciÃ³n del material audiovisual;
- definiciÃ³n y publicaciÃ³n de la versiÃ³n final de entrega.

---
