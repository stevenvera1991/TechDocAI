# Arquitectura de TechDocAI

## Introducción

TechDocAI utiliza una arquitectura modular desarrollada en Python. El proyecto separa las responsabilidades de la interfaz gráfica, los controladores, los modelos de datos, los servicios de procesamiento y las utilidades auxiliares.

Esta separación permite mantener el código organizado, facilitar el mantenimiento y permitir la evolución progresiva de las diferentes funcionalidades de la aplicación.

La arquitectura documentada corresponde al estado funcional de la versión `v0.7.0`.

---

## Arquitectura general

El flujo general de TechDocAI puede representarse de la siguiente manera:

```text
                         USUARIO
                            │
                            ▼
                 ┌─────────────────────┐
                 │   INTERFAZ GRÁFICA  │
                 │     CustomTkinter   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    CONTROLADORES    │
                 │    Controllers      │
                 └──────────┬──────────┘
                            │
              ┌─────────────┼─────────────┐
              │             │             │
              ▼             ▼             ▼
        ┌──────────┐  ┌──────────┐  ┌──────────┐
        │  CORE    │  │  MODELOS │  │ SERVICIOS│
        │Procesam. │  │Document  │  │          │
        └────┬─────┘  └──────────┘  └────┬─────┘
             │                            │
             │                  ┌─────────┼─────────┐
             │                  │         │         │
             │                  ▼         ▼         ▼
             │               PDF       Groq      Exportación
             │               Service   Service    Services
             │
             ▼
       Procesamiento
       de texto y chunks
                            │
                            ▼
                    ┌───────────────┐
                    │   RESULTADO   │
                    │    ANÁLISIS   │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │   EXPORTACIÓN │
                    │ Markdown/PDF/  │
                    │     DOCX      │
                    └───────────────┘
```

La arquitectura se organiza alrededor de un flujo en el que la interfaz recibe las acciones del usuario, los controladores coordinan las operaciones y los servicios ejecutan las tareas especializadas.

---

## Estructura de directorios

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
├── prompts/
│
├── tests/
│
├── exports/
├── logs/
├── historial/
│
├── .env
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── VERSION
├── config.py
├── main.py
└── requirements.txt
```

Los directorios `exports/`, `logs/` e `historial/` corresponden a información generada durante la ejecución y se gestionan de acuerdo con las reglas establecidas en `.gitignore`.

---

## Capas de la arquitectura

La aplicación puede dividirse conceptualmente en las siguientes capas:

```text
┌──────────────────────────────────────────────┐
│              INTERFAZ DE USUARIO             │
│                    app/ui                     │
├──────────────────────────────────────────────┤
│                 CONTROLADORES                 │
│                app/controllers                │
├──────────────────────────────────────────────┤
│            LÓGICA DE PROCESAMIENTO            │
│                   app/core                    │
├──────────────────────────────────────────────┤
│                 MODELOS                       │
│                 app/models                    │
├──────────────────────────────────────────────┤
│                  SERVICIOS                    │
│                app/services                   │
├──────────────────────────────────────────────┤
│              UTILIDADES Y CONFIG.             │
│          app/utils / config.py                │
└──────────────────────────────────────────────┘
```

Cada capa tiene una responsabilidad específica y evita concentrar toda la lógica de la aplicación en un único módulo.

---

## Interfaz gráfica

La interfaz gráfica se encuentra principalmente dentro de:

```text
app/ui/
```

Los módulos principales son:

```text
header.py
main_window.py
sidebar.py
statusbar.py
workspace.py
```

### `main_window.py`

Actúa como componente principal de la ventana de TechDocAI y coordina los elementos visuales principales de la aplicación.

Entre las operaciones accesibles desde la interfaz se encuentran:

- carga de documentos PDF;
- análisis del documento;
- generación del resumen ejecutivo;
- exportación a Markdown;
- exportación a PDF;
- exportación a DOCX.

### `sidebar.py`

Contiene los controles principales de navegación y las acciones disponibles para el usuario.

### `header.py`

Gestiona los elementos visuales correspondientes a la cabecera de la aplicación.

### `workspace.py`

Gestiona el área principal de trabajo donde se presenta la información relacionada con el documento y los resultados del procesamiento.

### `statusbar.py`

Presenta información relacionada con el estado actual de las operaciones de la aplicación.

---

## Controladores

Los controladores se encuentran en:

```text
app/controllers/
```

El componente principal es:

```text
document_controller.py
```

El controlador de documentos actúa como punto de coordinación entre la interfaz gráfica y las operaciones necesarias para cargar, procesar y analizar los documentos.

Su responsabilidad principal es evitar que la interfaz tenga que implementar directamente toda la lógica de procesamiento.

---

## Modelo de datos

El modelo principal se encuentra en:

```text
app/models/document.py
```

El modelo `Document` representa la información asociada con el documento que está siendo procesado.

La utilización de un modelo separado permite mantener los datos del documento diferenciados de la lógica de interfaz y de los servicios de procesamiento.

---

## Procesamiento de texto

La lógica principal relacionada con el procesamiento del contenido textual se encuentra en:

```text
app/core/text_processor.py
```

Este componente participa en la preparación del contenido extraído del documento para su procesamiento posterior.

Una de las funciones fundamentales del sistema es dividir documentos extensos en fragmentos o *chunks*.

El flujo conceptual es:

```text
Documento PDF
      │
      ▼
Extracción de texto
      │
      ▼
Procesamiento del texto
      │
      ▼
División en chunks
      │
      ▼
Procesamiento mediante IA
```

La división en *chunks* permite procesar documentos cuyo contenido completo no resulta conveniente enviar como una única entrada al modelo.

---

## Servicios

Los servicios especializados se encuentran en:

```text
app/services/
```

La arquitectura actual contiene los siguientes servicios principales:

```text
export_service.py
groq_service.py
history_service.py
pdf_service.py
```

### `pdf_service.py`

Se encarga de las operaciones relacionadas con la lectura y procesamiento de documentos PDF.

El flujo comienza cuando el usuario selecciona un documento y TechDocAI obtiene información básica como:

- nombre del documento;
- número de páginas;
- tamaño;
- caracteres;
- palabras;
- líneas;
- cantidad de chunks generados.

### `groq_service.py`

Gestiona la comunicación con la API de Groq.

El servicio recibe el contenido preparado para el análisis y realiza las solicitudes al modelo configurado.

En la versión `v0.7.0` se utiliza:

```text
Proveedor: Groq
Modelo: openai/gpt-oss-120b
```

El flujo de comunicación es:

```text
Contenido procesado
        │
        ▼
    Groq Service
        │
        ▼
     API Groq
        │
        ▼
Respuesta del modelo
```

El servicio también participa en la generación del informe consolidado y del resumen ejecutivo.

### `export_service.py`

Gestiona la generación de archivos de salida a partir de los resultados obtenidos durante el análisis.

Los formatos utilizados por TechDocAI incluyen:

```text
Markdown
PDF
DOCX
```

El flujo de exportación es:

```text
Resultado del análisis
          │
          ▼
   Export Service
          │
    ┌─────┼─────┐
    ▼     ▼     ▼
 Markdown PDF   DOCX
```

### `history_service.py`

Gestiona las operaciones relacionadas con el historial de análisis realizados por la aplicación.

---

## Configuración

La configuración general del proyecto se encuentra principalmente en:

```text
config.py
```

Este archivo centraliza parámetros generales como:

- nombre de la aplicación;
- versión;
- autor;
- proveedor de IA;
- modelo utilizado;
- configuración de la interfaz;
- rutas utilizadas por el proyecto.

La versión actual es:

```text
0.7.0
```

La versión también se mantiene registrada en:

```text
VERSION
```

---

## Variables de entorno

Las credenciales sensibles no se almacenan directamente en el código fuente.

TechDocAI utiliza un archivo:

```text
.env
```

para almacenar variables de entorno.

La variable principal utilizada para la integración con Groq es:

```text
GROQ_API_KEY=tu_clave_de_groq
```

El archivo `.env` se encuentra excluido del control de versiones mediante `.gitignore`.

---

## Flujo completo de procesamiento

El flujo principal de TechDocAI puede representarse mediante las siguientes etapas:

```text
┌──────────────────────┐
│     Usuario          │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│      Abrir PDF       │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    PDF Service       │
│ Extracción de texto  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Text Processor     │
│  Preparación/chunks  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│     Groq Service     │
│  Análisis por chunks │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Informe consolidado  │
└──────────┬───────────┘
           │
           ├───────────────────┐
           │                   │
           ▼                   ▼
┌──────────────────┐  ┌──────────────────┐
│ Resumen ejecutivo│  │    Historial     │
└────────┬─────────┘  └──────────────────┘
         │
         ▼
┌──────────────────────┐
│   Export Service     │
└──────────┬───────────┘
           │
      ┌────┼────┐
      ▼    ▼    ▼
     MD   PDF  DOCX
```

---

## Procesamiento por chunks

El procesamiento por *chunks* constituye una etapa importante de la arquitectura.

Cuando un documento es cargado, su contenido es extraído y posteriormente dividido en fragmentos.

Cada fragmento puede ser procesado individualmente mediante el servicio de Groq.

El flujo es:

```text
Documento
    │
    ▼
Texto extraído
    │
    ▼
┌───────────────┐
│ Chunk 1       │
├───────────────┤
│ Chunk 2       │
├───────────────┤
│ Chunk 3       │
├───────────────┤
│ ...           │
├───────────────┤
│ Chunk N       │
└───────┬───────┘
        │
        ▼
Procesamiento individual
        │
        ▼
Resultados parciales
        │
        ▼
Consolidación
```

La aplicación registra durante la ejecución información relacionada con el número de chunks y el progreso del procesamiento.

Por ejemplo:

```text
Procesando 8 chunks...
Resumiendo chunk 1/8
Resumiendo chunk 2/8
...
Resumiendo chunk 8/8
Generando informe consolidado...
```

---

## Consolidación del análisis

Después de procesar los diferentes *chunks*, los resultados individuales son enviados al proceso de consolidación.

El objetivo es generar un único informe técnico coherente a partir de los resultados parciales.

El flujo es:

```text
Chunk 1 ──┐
Chunk 2 ──┤
Chunk 3 ──┤
   ...    ├──► Consolidación ──► Informe técnico
Chunk N ──┘
```

Una vez generado el informe consolidado, TechDocAI puede utilizarlo como base para generar el resumen ejecutivo.

---

## Generación del resumen ejecutivo

La generación del resumen ejecutivo constituye una etapa independiente dentro del flujo.

El sistema utiliza el análisis consolidado como entrada para generar un resumen técnico.

```text
Informe consolidado
        │
        ▼
Prompt de resumen
        │
        ▼
Groq Service
        │
        ▼
Resumen ejecutivo
```

El resumen está orientado a presentar de manera concisa los aspectos esenciales identificados durante el análisis.

---

## Exportación de resultados

Una vez disponibles los resultados, el usuario puede exportarlos desde la interfaz gráfica.

Los formatos disponibles son:

```text
Markdown
PDF
DOCX
```

La arquitectura separa la generación de estos formatos mediante el servicio de exportación.

Esto permite mantener la lógica de generación de documentos independiente de la interfaz gráfica.

---

## Registro de eventos

TechDocAI utiliza un sistema de registro mediante:

```text
app/utils/logger.py
```

Los registros permiten realizar seguimiento de operaciones importantes durante la ejecución.

Entre los eventos registrados se encuentran:

```text
Documento cargado
Procesamiento de chunks
Solicitudes a Groq
Generación del informe consolidado
Generación del resumen ejecutivo
Exportación de resultados
```

Los registros facilitan la identificación de errores y la comprobación del flujo de ejecución.

---

## Punto de entrada

El punto de entrada de la aplicación es:

```text
main.py
```

La ejecución normal de TechDocAI se realiza mediante:

```powershell
python main.py
```

El punto de entrada inicia la aplicación y permite acceder a la interfaz gráfica principal.

---

## Dependencias entre componentes

La relación conceptual entre los principales componentes puede resumirse de la siguiente manera:

```text
main.py
   │
   ▼
Interfaz gráfica
   │
   ▼
Controller
   │
   ├──────────────► PDF Service
   │
   ├──────────────► Text Processor
   │
   ├──────────────► Groq Service
   │
   ├──────────────► History Service
   │
   └──────────────► Export Service
```

La interfaz no necesita implementar directamente las operaciones internas de cada servicio. El controlador y los servicios especializados permiten distribuir las responsabilidades.

---

## Principios de diseño utilizados

La organización actual del proyecto busca mantener los siguientes principios:

### Separación de responsabilidades

Cada módulo tiene una responsabilidad específica.

Por ejemplo:

```text
UI             → interacción con el usuario
Controller     → coordinación
Core           → procesamiento
Models         → representación de datos
Services       → operaciones especializadas
Utils          → funciones auxiliares
```

### Modularidad

Las funcionalidades están distribuidas en módulos independientes para facilitar su mantenimiento y evolución.

### Reutilización

Los servicios pueden ser utilizados por diferentes componentes sin necesidad de duplicar la lógica correspondiente.

### Mantenibilidad

La separación de responsabilidades permite localizar con mayor facilidad los componentes que deben modificarse cuando se incorpora una nueva funcionalidad.

---

## Estado arquitectónico en v0.7.0

La arquitectura documentada corresponde al estado funcional de `v0.7.0`.

En esta versión se encuentran implementados los principales componentes necesarios para:

```text
Carga de documentos
        ↓
Extracción de contenido
        ↓
Procesamiento de texto
        ↓
División en chunks
        ↓
Análisis mediante Groq
        ↓
Consolidación
        ↓
Resumen ejecutivo
        ↓
Exportación
```

La arquitectura puede continuar evolucionando en versiones posteriores, especialmente en aspectos relacionados con empaquetamiento, pruebas automatizadas, optimización del procesamiento y ampliación de funcionalidades.

Esta documentación debe actualizarse cuando una nueva versión modifique de manera significativa la estructura o las responsabilidades de los componentes.