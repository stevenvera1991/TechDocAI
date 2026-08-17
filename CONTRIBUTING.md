# Contribuyendo a TechDocAI

Gracias por tu interés en contribuir al desarrollo de TechDocAI.

Este documento establece las pautas básicas para modificar, probar y mantener el proyecto de forma organizada.

---

## Requisitos

Antes de realizar modificaciones en el proyecto se recomienda disponer de:

- Python compatible con la versión utilizada por el proyecto.
- Git.
- Visual Studio Code u otro editor compatible.
- Una cuenta de GitHub para contribuir mediante el repositorio remoto.
- Una API key de Groq para ejecutar las funcionalidades que requieren acceso al servicio de inteligencia artificial.

Las dependencias del proyecto se encuentran declaradas en:

```text
requirements.txt
```

---

## Configuración del entorno

Crear un entorno virtual desde la carpeta raíz del proyecto:

```powershell
python -m venv venv
```

Activar el entorno virtual en Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```powershell
python -m pip install -r requirements.txt
```

Configurar la variable de entorno necesaria para la integración con Groq mediante un archivo `.env`:

```text
GROQ_API_KEY=tu_clave_de_groq
```

El archivo `.env` no debe incorporarse al repositorio.

---

## Flujo de trabajo

Antes de comenzar una modificación, comprobar el estado actual del repositorio:

```powershell
git status
```

Se recomienda trabajar sobre una rama independiente para cada funcionalidad o modificación significativa.

El flujo general es:

```text
Actualizar el repositorio
        ↓
Crear una rama
        ↓
Realizar cambios
        ↓
Ejecutar pruebas
        ↓
Revisar diferencias
        ↓
Crear commit
        ↓
Publicar la rama
```

---

## Ramas

La rama utilizada para el desarrollo principal de TechDocAI es:

```text
develop
```

Para una nueva funcionalidad o modificación significativa se recomienda crear una rama independiente:

```powershell
git switch -c nombre-de-la-rama
```

Los nombres de las ramas deben ser descriptivos y estar relacionados con el cambio realizado.

Ejemplos:

```text
feature/exportacion
feature/mejora-interfaz
fix/error-pdf
docs/actualizacion-documentacion
```

---

## Cambios y commits

Los cambios deben mantenerse enfocados en una funcionalidad, corrección o tarea concreta.

Antes de realizar un commit se recomienda comprobar:

```powershell
git status
```

Revisar las diferencias:

```powershell
git diff
```

Y comprobar posibles problemas de espacios en blanco:

```powershell
git diff --check
```

Los mensajes de commit deben ser descriptivos.

Ejemplo:

```powershell
git add .
git commit -m "Descripción del cambio"
```

Evitar mensajes genéricos como:

```text
cambios
prueba
actualización
cosas nuevas
```

---

## Pruebas

Antes de publicar cambios se deben ejecutar las comprobaciones correspondientes a la modificación realizada.

### Comprobación de dependencias

```powershell
python -m pip check
```

El resultado esperado es:

```text
No broken requirements found.
```

### Comprobación de compilación

```powershell
python -m compileall -f app config.py main.py
```

### Ejecución de la aplicación

```powershell
python main.py
```

Las modificaciones que afecten al flujo principal deben comprobarse mediante una ejecución funcional de TechDocAI.

---

## Pull requests

Cuando el proyecto se gestione mediante ramas de desarrollo y revisión, los cambios pueden integrarse mediante un Pull Request.

Un Pull Request debe incluir:

- descripción clara del cambio;
- motivo de la modificación;
- funcionalidades afectadas;
- pruebas realizadas;
- posibles limitaciones conocidas.

Los cambios deben revisarse antes de integrarse en la rama de desarrollo.

---

## Documentación

Las modificaciones que cambien el comportamiento, estructura o funcionamiento del proyecto deben reflejarse en la documentación correspondiente.

Los principales archivos de documentación son:

```text
README.md
CHANGELOG.md
docs/arquitectura/README.md
CONTRIBUTING.md
```

Cuando una modificación altere significativamente la arquitectura del sistema, también debe actualizarse:

```text
docs/arquitectura/README.md
```

Los cambios relevantes entre versiones deben registrarse en:

```text
CHANGELOG.md
```

---

## Seguridad

Las credenciales y datos sensibles deben mantenerse fuera del código fuente y del control de versiones.

### API keys

Nunca incluir una API key directamente en archivos Python, commits, Pull Requests o documentación pública.

La API key de Groq debe almacenarse mediante una variable de entorno:

```text
GROQ_API_KEY=tu_clave_de_groq
```

El archivo:

```text
.env
```

debe permanecer excluido mediante `.gitignore`.

Para distribuir el proyecto se puede utilizar:

```text
.env.example
```

con una referencia sin credenciales reales:

```text
GROQ_API_KEY=tu_clave_de_groq
```

### Información sensible

No deben incorporarse al repositorio:

- API keys;
- contraseñas;
- tokens;
- credenciales;
- archivos `.env`;
- información privada;
- archivos generados que contengan datos sensibles.

Antes de realizar un commit se debe revisar:

```powershell
git status
```

y comprobar los cambios mediante:

```powershell
git diff
```

---

## Dependencias

Las dependencias directas deben declararse en:

```text
requirements.txt
```

Cuando se incorpore una nueva dependencia, se debe verificar que:

1. sea necesaria para el proyecto;
2. sea compatible con las demás dependencias;
3. esté correctamente instalada;
4. no genere conflictos;
5. quede registrada en `requirements.txt`.

Después de modificar las dependencias se recomienda ejecutar:

```powershell
python -m pip check
```

---

## Calidad del código

Las modificaciones deben procurar mantener:

- separación de responsabilidades;
- estructura modular;
- nombres descriptivos;
- código legible;
- ausencia de código duplicado innecesario;
- compatibilidad con la arquitectura existente.

No se recomienda realizar modificaciones que afecten múltiples componentes sin una justificación clara.

---

## Publicación de cambios

Una vez verificadas las modificaciones, los cambios pueden publicarse en el repositorio remoto:

```powershell
git push origin nombre-de-la-rama
```

La publicación de nuevas versiones debe realizarse mediante el proceso de versionado establecido para el proyecto.

Las versiones oficiales se identifican mediante etiquetas Git:

```text
v0.6.1
```

---

## Principio general

Toda contribución debe procurar mantener TechDocAI en un estado:

```text
Funcional
   +
Reproducible
   +
Documentado
   +
Seguro
   +
Mantenible
```

Los cambios deben priorizar la estabilidad del proyecto y mantener la coherencia entre el código fuente, la documentación, las dependencias y la versión publicada.