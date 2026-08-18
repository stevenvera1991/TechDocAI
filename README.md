# TechDocAI

**Intelligent Technical Document Analyzer**

TechDocAI es una aplicación de escritorio desarrollada en Python para el análisis inteligente de documentos técnicos en formato PDF mediante inteligencia artificial.

El sistema permite cargar documentos PDF, extraer y procesar su contenido, dividir documentos extensos en fragmentos (*chunks*), enviarlos a un modelo de inteligencia artificial mediante la API de Groq, generar un informe técnico consolidado y producir un resumen ejecutivo. Además, permite exportar los resultados en formatos Markdown, PDF y DOCX.

---

## Versión actual

**v0.7.0**

Esta versión incorpora la actualización del modelo de inteligencia artificial utilizado por TechDocAI a `openai/gpt-oss-120b`, junto con la actualización de la documentación técnica y arquitectónica del proyecto para reflejar el estado actual de entrega.

### Estado

- Análisis de documentos PDF: operativo
- Procesamiento por chunks: operativo
- Integración con Groq: operativa
- Generación de informe consolidado: operativa
- Generación de resumen ejecutivo: operativa
- Exportación Markdown: operativa
- Exportación PDF: operativa
- Exportación DOCX: operativa
- Reproducción desde un clon limpio: validada

---

## Características principales

TechDocAI incorpora las siguientes funcionalidades:

- Selección y carga de documentos PDF.
- Extracción del contenido textual del documento.
- Obtención de información básica del documento:
  - nombre;
  - número de páginas;
  - tamaño;
  - caracteres;
  - palabras;
  - líneas;
  - número de chunks.
- División del contenido en chunks para su procesamiento mediante IA.
- Análisis individual de los chunks mediante Groq.
- Consolidación de los resultados obtenidos.
- Generación de un informe técnico consolidado.
- Generación de un resumen ejecutivo técnico.
- Exportación del análisis en:
  - Markdown (`.md`);
  - PDF (`.pdf`);
  - Microsoft Word (`.docx`).
- Interfaz gráfica de escritorio desarrollada con CustomTkinter.
- Registro de eventos mediante sistema de logging.
- Gestión del historial de análisis.
- Configuración de credenciales mediante variables de entorno.
- Separación entre código fuente y archivos generados.
- Estructura modular orientada a servicios.

---

## Arquitectura general

TechDocAI utiliza una arquitectura modular en la que la interfaz gráfica, los controladores, los modelos, los servicios y las utilidades se encuentran separados.

El flujo general de procesamiento es:

```text
                    USUARIO
                       │
                       ▼
              INTERFAZ GRÁFICA
                 CustomTkinter
                       │
                       ▼
                CONTROLADOR
                       │
                       ▼
              PROCESAMIENTO PDF
                       │
                       ▼
             EXTRACCIÓN DE TEXTO
                       │
                       ▼
                 DIVISIÓN EN
                   CHUNKS
                       │
                       ▼
                SERVICIO GROQ
                       │
                       ▼
             ANÁLISIS DE CADA
                    CHUNK
                       │
                       ▼
               CONSOLIDACIÓN
                  DEL ANÁLISIS
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
      INFORME TÉCNICO      RESUMEN EJECUTIVO
             │                   │
             └─────────┬─────────┘
                       ▼
                 EXPORTACIÓN
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Markdown        PDF         DOCX
```

---

## Requisitos

Para ejecutar TechDocAI se requiere:

- Windows u otro sistema compatible con Python.
- Python 3.
- Git.
- Acceso a Internet para utilizar la API de Groq.
- Una API key válida de Groq.

Las dependencias directas del proyecto están especificadas en:

```text
requirements.txt
```

---

## Instalación

### 1. Clonar el repositorio

Para reproducir la versión actualmente validada:

```powershell
git clone --branch v0.6.1 https://github.com/stevenvera1991/TechDocAI.git
cd TechDocAI
```

También puede clonarse la rama de desarrollo:

```powershell
git clone https://github.com/stevenvera1991/TechDocAI.git
cd TechDocAI
```

### 2. Crear el entorno virtual

Desde la carpeta raíz del proyecto:

```powershell
python -m venv venv
```

### 3. Activar el entorno virtual

En Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Si la activación fue correcta, el terminal mostrará el entorno virtual activo:

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

## Configuración de la API de Groq

TechDocAI utiliza Groq como proveedor de inteligencia artificial para realizar el análisis de los documentos.

### 1. Crear el archivo `.env`

El archivo `.env` debe ubicarse en la carpeta raíz del proyecto:

```text
TechDocAI/
├── .env
├── config.py
├── main.py
├── requirements.txt
└── ...
```

### 2. Configurar la API key

Dentro del archivo `.env`, agregar la variable:

```text
GROQ_API_KEY=tu_clave_de_groq
```

Reemplazar `tu_clave_de_groq` por una API key válida de Groq.

### 3. Seguridad de la API key

La API key no debe escribirse directamente en el código fuente.

El archivo `.env` se encuentra incluido en `.gitignore`, por lo que no debe formar parte del repositorio Git.

No se debe publicar la API key en:

- GitHub.
- Capturas de pantalla.
- Documentación pública.
- Archivos fuente.
- Mensajes de commit.

Si una API key se expone accidentalmente, debe revocarse y sustituirse por una nueva.

### 4. Verificación de la configuración

Una vez creada la variable `GROQ_API_KEY`, ejecutar TechDocAI con el entorno virtual activo:

```powershell
python main.py
```

Si la configuración es correcta, la aplicación podrá comunicarse con el servicio de Groq durante el análisis de los documentos.

### Proveedor y modelo

La configuración actual utiliza:

```text
Proveedor: Groq
Modelo: openai/gpt-oss-120b
```

Los parámetros de configuración del proveedor se encuentran centralizados en `config.py`.

---

## Ejecución

Con el entorno virtual activo y la API key de Groq configurada, iniciar la aplicación desde la carpeta raíz del proyecto:

```powershell
python main.py
```

La aplicación abrirá la interfaz gráfica de TechDocAI.

### Inicio de la aplicación

El punto de entrada principal del sistema es:

```text
main.py
```

Este archivo inicia la aplicación y carga la interfaz gráfica principal.

### Registro de ejecución

TechDocAI utiliza un sistema de logging para registrar eventos relevantes durante la ejecución.

Los registros permiten realizar seguimiento de:

- carga de documentos;
- procesamiento de información;
- operaciones realizadas por los servicios;
- generación de resultados;
- errores o eventos relevantes.

Los archivos de log se almacenan localmente y están excluidos del control de versiones mediante `.gitignore`.

### Detención de la aplicación

Para finalizar la ejecución, cerrar la ventana principal de TechDocAI de forma normal.

---

## Flujo de uso

El uso de TechDocAI se realiza mediante la interfaz gráfica siguiendo una secuencia de operaciones.

### 1. Seleccionar un documento

Utilizar la opción de apertura de archivos para seleccionar el documento PDF que se desea analizar.

### 2. Cargar el documento

TechDocAI carga el archivo seleccionado y presenta información básica del documento, incluyendo:

- nombre del archivo;
- número de páginas;
- tamaño;
- información del contenido;
- número de chunks generados.

### 3. Analizar el documento

Seleccionar:

**Analizar Documento**

El sistema procesa el contenido del PDF mediante el flujo de análisis implementado y utiliza Groq para generar los resultados correspondientes.

### 4. Generar el resumen ejecutivo

Una vez disponible el análisis consolidado, seleccionar:

**Generar Resumen**

TechDocAI genera un resumen ejecutivo técnico basado en la información obtenida durante el análisis.

### 5. Revisar los resultados

El usuario puede revisar el informe y el resumen generados desde la interfaz antes de realizar la exportación.

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
          ↓
      Cargar PDF
          ↓
   Analizar documento
          ↓
 Generar resultados
          ↓
Generar resumen ejecutivo
          ↓
   Revisar resultados
          ↓
       Exportar
          ↓
 Markdown / PDF / DOCX
```

---

## Exportación de resultados

TechDocAI permite exportar los resultados del análisis en diferentes formatos para facilitar su consulta, almacenamiento y utilización posterior.

### Exportar en Markdown

La opción **Exportar Markdown** genera un archivo de texto estructurado en formato Markdown (`.md`).

Este formato permite conservar la estructura del informe y facilita su lectura, edición y reutilización en diferentes herramientas compatibles con Markdown.

### Exportar en PDF

La opción **Exportar PDF** genera un documento en formato PDF mediante ReportLab.

Este formato está orientado a la presentación y distribución del informe técnico en un documento de salida independiente.

### Exportar en DOCX

La opción **Exportar DOCX** genera un documento compatible con Microsoft Word (`.docx`).

Este formato permite editar posteriormente el contenido del informe mediante aplicaciones compatibles con documentos de Word.

### Ubicación de los archivos

Los archivos generados por TechDocAI se almacenan en la carpeta:

```text
exports/
```

La carpeta `exports/` está excluida del control de versiones mediante `.gitignore`, por lo que los documentos generados localmente no se incorporan al repositorio Git.

### Formatos disponibles

| Formato | Extensión | Uso principal |
|---|---|---|
| Markdown | `.md` | Lectura, edición y reutilización del informe |
| PDF | `.pdf` | Presentación y distribución |
| Microsoft Word | `.docx` | Edición posterior del documento |

---

## Procesamiento por chunks

Para procesar documentos de mayor extensión, TechDocAI divide el contenido textual extraído del PDF en fragmentos denominados *chunks*.

### Flujo de procesamiento

El procesamiento sigue la siguiente secuencia:

```text
Documento PDF
      ↓
Extracción de texto
      ↓
División del contenido
      ↓
Generación de chunks
      ↓
Análisis individual de cada chunk
      ↓
Consolidación de resultados
      ↓
Informe técnico
```

Cada chunk es procesado de manera individual mediante el servicio de inteligencia artificial configurado en TechDocAI.

### Procesamiento individual

El sistema procesa los fragmentos de forma secuencial:

```text
Chunk 1 → Groq
Chunk 2 → Groq
Chunk 3 → Groq
   ...
Chunk N → Groq
```

Los resultados obtenidos de los diferentes chunks se utilizan posteriormente para generar un análisis consolidado del documento.

### Ventajas del procesamiento por chunks

Esta estrategia permite:

- trabajar con documentos de mayor extensión;
- dividir el contenido en unidades de procesamiento controlables;
- procesar cada fragmento de manera individual;
- consolidar posteriormente los resultados obtenidos.

El número de chunks depende del contenido y de la configuración utilizada por el procesador de texto de TechDocAI.

---

## Arquitectura del proyecto

TechDocAI está organizado mediante una estructura modular que separa la interfaz gráfica, la lógica de procesamiento, los modelos de datos, los servicios y las utilidades.

La estructura principal del proyecto es:

```text
TechDocAI/
│
├── app/
│   ├── config/
│   │   └── __init__.py
│   │
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── document_controller.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   └── text_processor.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── document.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── export_service.py
│   │   ├── groq_service.py
│   │   ├── history_service.py
│   │   └── pdf_service.py
│   │
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── header.py
│   │   ├── main_window.py
│   │   ├── sidebar.py
│   │   ├── statusbar.py
│   │   └── workspace.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── logger.py
│
├── docs/
│   └── arquitectura/
│       └── README.md
│
├── prompts/
│   └── resumen.txt
│
├── tests/
│   └── test_history.py
│
├── config.py
├── main.py
├── VERSION
├── requirements.txt
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── .gitignore
│
├── test_controller_resumen.py
├── test_export_docx.py
├── test_export_pdf.py
├── test_generar_resumen.py
└── test_groq.py
```

### Componentes principales

#### `app/controllers/`

Contiene los controladores responsables de coordinar las acciones realizadas sobre los documentos y conectar la interfaz con la lógica de procesamiento.

#### `app/core/`

Contiene la lógica central relacionada con el procesamiento y transformación del texto extraído de los documentos.

#### `app/models/`

Contiene los modelos utilizados para representar la información de los documentos procesados.

#### `app/services/`

Contiene los servicios principales de la aplicación:

- `pdf_service.py`: procesamiento y extracción de información de documentos PDF.
- `groq_service.py`: comunicación con el servicio de inteligencia artificial de Groq.
- `export_service.py`: generación y exportación de los resultados.
- `history_service.py`: gestión del historial de análisis.

#### `app/ui/`

Contiene los componentes de la interfaz gráfica de TechDocAI:

- encabezado;
- ventana principal;
- barra lateral;
- barra de estado;
- área de trabajo.

La interfaz está desarrollada utilizando CustomTkinter.

#### `app/utils/`

Contiene utilidades generales utilizadas por diferentes componentes de la aplicación, incluyendo el sistema de logging.

#### `prompts/`

Contiene los archivos de instrucciones utilizados para orientar la generación de determinados resultados mediante inteligencia artificial.

#### `tests/`

Contiene pruebas asociadas a funcionalidades específicas del proyecto.

#### `docs/`

Contiene documentación técnica complementaria del proyecto, incluyendo la documentación detallada de arquitectura.

#### Archivos principales

- `main.py`: punto de entrada de la aplicación.
- `config.py`: configuración general del proyecto y del proveedor de IA.
- `VERSION`: versión actual de TechDocAI.
- `requirements.txt`: dependencias directas del proyecto.
- `.gitignore`: archivos y directorios excluidos del control de versiones.
- `README.md`: documentación general del proyecto.
- `CHANGELOG.md`: historial de cambios entre versiones.
- `CONTRIBUTING.md`: directrices de contribución.
- `LICENSE`: archivo destinado a documentar la licencia del proyecto.

---

## Dependencias principales

TechDocAI utiliza un conjunto de dependencias directas necesarias para la interfaz gráfica, el procesamiento de documentos, la integración con inteligencia artificial y la generación de archivos de salida.

Las dependencias principales y sus versiones utilizadas en la versión `v0.6.1` son:

```text
customtkinter==6.0.0
groq==1.6.0
PyPDF2==3.0.1
python-dotenv==1.2.2
Pillow==12.3.0
reportlab==5.0.0
python-docx==1.2.0
```

### Función de las principales dependencias

| Dependencia | Función |
|---|---|
| `customtkinter` | Desarrollo de la interfaz gráfica de escritorio. |
| `groq` | Comunicación con la API de Groq para el procesamiento mediante inteligencia artificial. |
| `PyPDF2` | Lectura y extracción de contenido de documentos PDF. |
| `python-dotenv` | Carga de variables de entorno desde el archivo `.env`. |
| `Pillow` | Procesamiento y gestión de imágenes utilizadas por la aplicación. |
| `reportlab` | Generación de documentos PDF. |
| `python-docx` | Generación de documentos Microsoft Word (`.docx`). |

### Gestión de dependencias

Las dependencias directas del proyecto se encuentran declaradas en:

```text
requirements.txt
```

El archivo mantiene las versiones utilizadas para facilitar la reproducción del entorno de ejecución.

Las dependencias transitivas son instaladas automáticamente por `pip` cuando son requeridas por las bibliotecas principales y no necesitan ser declaradas individualmente en `requirements.txt` cuando no son utilizadas directamente por el código de TechDocAI.

### Verificación del entorno

Para comprobar que las dependencias instaladas no presentan conflictos se puede ejecutar:

```powershell
python -m pip check
```

El resultado esperado es:

```text
No broken requirements found.
```

También puede verificarse la instalación de las dependencias mediante:

```powershell
python -m pip freeze
```

La versión `v0.6.1` fue validada mediante la instalación de las dependencias desde `requirements.txt` en un entorno virtual independiente.

---

## Configuración del proyecto

Los principales parámetros de configuración de TechDocAI se encuentran centralizados en el archivo:

```text
config.py
```

Este archivo contiene la configuración general de la aplicación y de los servicios utilizados por el sistema.

### Información de la aplicación

La configuración incluye:

- nombre de la aplicación;
- versión actual;
- autor;
- curso;
- institución.

La versión definida actualmente es:

```text
0.7.0
```

y se mantiene sincronizada con el archivo:

```text
VERSION
```

### Configuración del proveedor de IA

TechDocAI utiliza Groq como proveedor de inteligencia artificial.

La configuración incluye:

```text
Proveedor: Groq
Modelo: openai/gpt-oss-120b
```

Los parámetros específicos de Groq se encuentran definidos en `config.py`.

La API key no se almacena directamente en este archivo. Se obtiene mediante la variable de entorno:

```text
GROQ_API_KEY
```

### Configuración de la interfaz

El archivo `config.py` también contiene parámetros relacionados con la interfaz gráfica, incluyendo:

- título de la ventana;
- ancho;
- alto;
- posibilidad de redimensionamiento;
- modo de apariencia;
- tema de color.

### Rutas del proyecto

La configuración establece las rutas utilizadas por los diferentes componentes de TechDocAI.

Entre ellas se encuentran las rutas correspondientes a:

- directorio base;
- documentos PDF;
- resultados;
- prompts;
- registros de ejecución;
- pruebas.

La centralización de estas configuraciones permite que los diferentes módulos de la aplicación utilicen una referencia común para los recursos del proyecto.

---

## Seguridad y archivos excluidos

TechDocAI utiliza un archivo `.gitignore` para evitar que información sensible, archivos temporales, entornos locales y resultados generados sean incorporados al repositorio.

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

El archivo `.env` contiene las variables de entorno utilizadas por la aplicación, incluyendo la API key de Groq.

Por seguridad, `.env` no debe incorporarse al repositorio.

La configuración se realiza mediante:

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

Los directorios `exports/` e `historial/` contienen información generada durante la utilización de la aplicación.

Estos archivos son específicos de cada entorno de ejecución y no forman parte del código fuente versionado.

### Registros

Los archivos de registro generados durante la ejecución se almacenan localmente y se excluyen del repositorio mediante:

```text
logs/*.log
```

### Protección de credenciales

Las credenciales y claves de acceso no deben almacenarse directamente en los archivos fuente ni incluirse en commits.

Antes de realizar un commit, se debe comprobar que no existan archivos sensibles o credenciales dentro de los cambios pendientes.

---

## Reproducibilidad

La versión `v0.6.1` de TechDocAI fue validada mediante la reproducción del proyecto desde un clon limpio del repositorio.

El objetivo de esta validación es comprobar que otra instalación puede reconstruir el entorno de ejecución utilizando únicamente el repositorio, las dependencias declaradas y la configuración de la API.

### Procedimiento de reproducción

El proceso utilizado fue:

```text
Repositorio GitHub
       ↓
Clon de la versión v0.6.1
       ↓
Creación de un nuevo entorno virtual
       ↓
Instalación de requirements.txt
       ↓
Configuración de la API de Groq
       ↓
Verificación de dependencias
       ↓
Verificación de compilación
       ↓
Ejecución de TechDocAI
       ↓
Prueba funcional
```

### Clon de la versión validada

La versión específica puede obtenerse mediante:

```powershell
git clone --branch v0.6.1 https://github.com/stevenvera1991/TechDocAI.git TechDocAI-REPRO
cd TechDocAI-REPRO
```

### Creación del entorno

Desde la carpeta del proyecto:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Instalación de dependencias

Con el entorno virtual activo:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Verificación de dependencias

Comprobar que no existan conflictos:

```powershell
python -m pip check
```

Resultado esperado:

```text
No broken requirements found.
```

### Verificación de compilación

Comprobar que los módulos principales puedan compilarse correctamente:

```powershell
python -m compileall -f app config.py main.py
```

### Configuración de la API

Crear el archivo `.env` en la raíz del proyecto y configurar una API key válida de Groq:

```text
GROQ_API_KEY=tu_clave_de_groq
```

La API key es específica del entorno de ejecución y no forma parte del repositorio.

### Validación funcional

Una vez configurado el entorno, ejecutar:

```powershell
python main.py
```

La versión `v0.6.1` fue validada mediante:

- clon del repositorio;
- creación de un entorno virtual independiente;
- instalación desde `requirements.txt`;
- verificación de dependencias;
- verificación de compilación;
- configuración de la API de Groq;
- ejecución de la aplicación;
- carga de un documento PDF;
- análisis mediante Groq;
- generación del informe consolidado;
- generación del resumen ejecutivo;
- exportación de resultados.

Esta validación confirma la reproducibilidad funcional de `v0.6.1` bajo las condiciones utilizadas durante las pruebas.

---

## Validación técnica

La versión `v0.6.1` fue sometida a diferentes comprobaciones técnicas antes y durante la validación funcional.

### Verificación de dependencias

Se comprobó que las dependencias instaladas no presentaran conflictos mediante:

```powershell
python -m pip check
```

Resultado obtenido:

```text
No broken requirements found.
```

### Verificación de compilación

Se comprobó la compilación de los módulos principales de Python mediante:

```powershell
python -m compileall -f app config.py main.py
```

La compilación se completó correctamente para los módulos del proyecto.

### Verificación del código

También se realizó una comprobación de formato de diferencias mediante:

```powershell
git diff --check
```

La comprobación no reportó errores de espacios en blanco ni problemas de formato en los cambios realizados.

### Verificación funcional

La aplicación fue ejecutada mediante:

```powershell
python main.py
```

Durante la prueba funcional se verificó el procesamiento de un documento PDF mediante el siguiente flujo:

```text
Carga del documento
        ↓
Extracción del contenido
        ↓
Generación de chunks
        ↓
Procesamiento mediante Groq
        ↓
Generación del informe consolidado
        ↓
Generación del resumen ejecutivo
        ↓
Exportación de resultados
```

La integración con Groq respondió correctamente durante las pruebas realizadas.

### Resultado de la validación

Las comprobaciones realizadas permitieron verificar:

- integridad de las dependencias;
- compilación correcta de los módulos principales;
- ausencia de errores de formato en los cambios revisados;
- ejecución correcta de la aplicación;
- comunicación con la API de Groq;
- procesamiento de documentos PDF;
- generación del informe consolidado;
- generación del resumen ejecutivo;
- funcionamiento de las opciones de exportación.

Estas comprobaciones forman parte de la validación técnica de la versión `v0.6.1`.

---

## Evolución del proyecto

TechDocAI fue desarrollado de manera incremental mediante diferentes etapas de implementación, validación y limpieza del proyecto.

### v0.2.0

Introducción del modelo de dominio `Document` y consolidación de la arquitectura inicial de gestión documental.

También se incorporaron componentes relacionados con la configuración de la integración con Groq y el procesamiento de documentos mediante inteligencia artificial.

### v0.3.0

Consolidación del flujo de análisis de documentos mediante inteligencia artificial y evolución de los componentes principales de procesamiento.

### v0.4.0

Implementación de la exportación y gestión de reportes, incorporando los mecanismos necesarios para generar documentos de salida.

### v0.5.0

Implementación de la generación del resumen ejecutivo a partir del análisis consolidado.

### v0.6.0

Limpieza integral del proyecto y eliminación controlada de componentes obsoletos o que ya no formaban parte del flujo funcional.

### v0.6.1

Corrección y normalización de la configuración del proyecto y de sus dependencias.

Esta versión también fue sometida a una validación de reproducibilidad mediante la creación de un entorno independiente a partir de un clon del repositorio.

### v0.7.0

Actualización del modelo de inteligencia artificial utilizado por el proyecto a `openai/gpt-oss-120b`, manteniendo a Groq como proveedor de inteligencia artificial.

Esta versión incorpora además la actualización de la documentación técnica y arquitectónica para reflejar el estado actual de entrega del proyecto y fue validada funcionalmente mediante la ejecución de la aplicación y el procesamiento de un documento PDF con el modelo actualizado.

### Estado de la evolución

La evolución del proyecto ha permitido pasar progresivamente de una estructura inicial de análisis documental a un MVP funcional capaz de:

- cargar documentos PDF;
- procesar su contenido;
- utilizar inteligencia artificial mediante Groq;
- consolidar resultados;
- generar un resumen ejecutivo;
- exportar informes en diferentes formatos;
- mantener una estructura modular;
- reproducir el entorno de ejecución mediante dependencias declaradas.

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

Las principales versiones identificadas durante la evolución del proyecto son:

```text
v0.2.0
v0.3.0
v0.4.0
v0.5.0
v0.6.0
v0.6.1
```

Cada etiqueta permite identificar un estado específico del proyecto y facilita la reproducción de una versión determinada.

### Versión actual

La versión actualmente validada es:

```text
v0.7.0
```

Esta versión se encuentra sincronizada entre:

```text
VERSION
```

y:

```python
APP_VERSION = "0.7.0"
```

El tag `v0.7.0` identifica el estado actual del código utilizado durante la validación funcional del proyecto.

### Reproducción de una versión específica

Para obtener directamente la versión `v0.6.1` desde GitHub:

```powershell
git clone --branch v0.6.1 https://github.com/stevenvera1991/TechDocAI.git
```

De esta manera se puede reconstruir el entorno correspondiente a una versión concreta sin depender del estado posterior de la rama de desarrollo.

### Próxima versión de entrega

La siguiente versión se definirá una vez completadas las etapas pendientes del proyecto, incluyendo:

- documentación final;
- empaquetamiento de la aplicación;
- validación final del paquete de entrega;
- preparación de los materiales de presentación.

La numeración de la próxima versión se establecerá de acuerdo con los cambios que finalmente se incorporen al proyecto.

---

## Desarrollo

El desarrollo de TechDocAI se organiza mediante una estructura modular y un flujo de trabajo basado en control de versiones.

### Organización del desarrollo

Las nuevas funcionalidades y modificaciones deben realizarse de manera controlada, procurando mantener separadas las diferentes responsabilidades del sistema.

Antes de incorporar cambios al proyecto se recomienda:

1. Implementar la modificación.
2. Ejecutar las pruebas correspondientes.
3. Verificar la compilación de los módulos.
4. Comprobar las dependencias.
5. Revisar los cambios mediante Git.
6. Crear un commit descriptivo.
7. Publicar los cambios en el repositorio remoto cuando corresponda.

### Rama de desarrollo

La rama principal utilizada durante el desarrollo es:

```text
develop
```

Los cambios realizados durante la construcción del proyecto se integran progresivamente en esta rama.

### Commits

Los commits deben utilizar mensajes descriptivos que permitan identificar claramente el cambio realizado.

Ejemplo:

```powershell
git add .
git commit -m "Descripción del cambio"
```

### Verificación antes de un commit

Se recomienda comprobar el estado del repositorio mediante:

```powershell
git status
```

También puede revisarse la diferencia de los archivos modificados mediante:

```powershell
git diff
```

Y comprobar posibles problemas de espacios en blanco mediante:

```powershell
git diff --check
```

### Publicación de cambios

Una vez verificados los cambios, pueden publicarse en el repositorio remoto mediante:

```powershell
git push origin develop
```

El flujo de desarrollo debe mantener el repositorio en un estado funcional y reproducible.

---

## Pruebas

TechDocAI incorpora diferentes archivos de prueba destinados a verificar funcionalidades específicas de la aplicación.

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

- generación del resumen;
- comunicación con Groq;
- exportación a PDF;
- exportación a DOCX;
- gestión del historial.

### Verificación de compilación

Además de las pruebas funcionales, se puede comprobar que los módulos principales de Python puedan compilarse correctamente mediante:

```powershell
python -m compileall -f app config.py main.py
```

### Verificación de dependencias

La integridad de las dependencias instaladas puede comprobarse mediante:

```powershell
python -m pip check
```

El resultado esperado es:

```text
No broken requirements found.
```

### Verificación del repositorio

Antes de publicar cambios se recomienda comprobar el estado del repositorio:

```powershell
git status
```

También puede verificarse la integridad de los cambios mediante:

```powershell
git diff --check
```

### Validación funcional

La validación funcional de `v0.7.0` incluyó la ejecución de TechDocAI y el procesamiento de un documento PDF mediante Groq utilizando el modelo `openai/gpt-oss-120b`.

Durante esta validación se comprobó el flujo principal de la aplicación:

```text
Carga del documento
        ↓
Procesamiento del PDF
        ↓
Análisis mediante Groq
        ↓
Generación del informe
        ↓
Generación del resumen ejecutivo
        ↓
Exportación de resultados
```

Estas comprobaciones complementan las pruebas específicas y permiten verificar el funcionamiento general del MVP.

---

## Limitaciones actuales

La versión `v0.7.0` constituye un MVP funcional y reproducible de TechDocAI. Sin embargo, existen aspectos que pueden continuar desarrollándose en versiones posteriores.

### Limitaciones de procesamiento

- El procesamiento de documentos extensos depende de la división del contenido en *chunks*.
- El tiempo de procesamiento puede aumentar según la cantidad de chunks generados.
- El procesamiento mediante la API de Groq está sujeto a los límites y condiciones del servicio utilizado.
- La calidad de los resultados depende del contenido y calidad del documento PDF analizado.

### Limitaciones de la versión actual

La versión `v0.7.0` no constituye todavía una versión final empaquetada como aplicación distribuible independiente.

Entre las funcionalidades que pueden desarrollarse posteriormente se encuentran:

- empaquetamiento de la aplicación para distribución;
- automatización del proceso de instalación;
- ampliación de las pruebas automatizadas;
- mejoras adicionales de la interfaz gráfica;
- optimización del procesamiento de documentos extensos;
- manejo más avanzado de límites y errores de la API;
- incorporación de nuevos proveedores o modelos de inteligencia artificial;
- ampliación de las capacidades de análisis técnico.

Estas funcionalidades forman parte de posibles etapas futuras y no deben considerarse como características garantizadas de `v0.7.0`.

### Alcance del MVP

El MVP actual se centra en proporcionar un flujo funcional para:

```text
Carga de PDF
      ↓
Procesamiento del documento
      ↓
Análisis mediante IA
      ↓
Consolidación de resultados
      ↓
Resumen ejecutivo
      ↓
Exportación
```

La ampliación de funcionalidades se realizará de manera progresiva en las siguientes versiones del proyecto.

---

## Autor

**Steven Vera**

TechDocAI fue desarrollado como proyecto del curso:

**Python + IA**

Institución:

**Institute Technology Bertoni**

---

## Licencia

La información correspondiente a la licencia del proyecto se encuentra en el archivo:

```text
LICENSE
```

La licencia aplicable a TechDocAI deberá consultarse directamente en dicho archivo.

---

## Estado final del proyecto

**TechDocAI v0.7.0 — MVP funcional y reproducible**

La versión `v0.7.0` representa el estado actualmente validado del proyecto.

El MVP permite:

- cargar documentos PDF;
- extraer y procesar su contenido;
- dividir documentos en *chunks*;
- analizar el contenido mediante Groq;
- generar un informe técnico consolidado;
- generar un resumen ejecutivo;
- exportar resultados en Markdown, PDF y DOCX;
- mantener un historial de análisis;
- utilizar una configuración mediante variables de entorno;
- reproducir el entorno de ejecución mediante las dependencias declaradas.

La versión `v0.7.0` fue validada mediante la ejecución del proyecto actualizado, configuración de la API de Groq, ejecución de la aplicación y procesamiento funcional de un documento PDF con el modelo `openai/gpt-oss-120b`.

### Estado de la versión

```text
Versión: v0.7.0
Estado: MVP funcional y reproducible
Proveedor de IA: Groq
Modelo: openai/gpt-oss-120b
```

### Siguiente etapa

Con la validación del MVP completada, el proyecto puede avanzar hacia las siguientes etapas de entrega:

- documentación técnica final;
- documentación de arquitectura;
- preparación del empaquetamiento;
- validación del paquete de distribución;
- preparación del material audiovisual;
- definición y publicación de la versión final de entrega.

---
