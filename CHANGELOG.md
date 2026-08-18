# Changelog

Todos los cambios relevantes de TechDocAI se documentan en este archivo.

El proyecto utiliza versiones etiquetadas mediante Git para mantener la trazabilidad de los diferentes estados funcionales del sistema.

---

## [0.7.0] - 2026-08-17

### Changed

- Actualización del modelo de inteligencia artificial utilizado por TechDocAI a `openai/gpt-oss-120b`.
- Mantenimiento de Groq como proveedor de inteligencia artificial.
- Actualización de la versión de la aplicación a `0.7.0`.
- Sincronización de la versión entre `VERSION` y `config.py`.
- Actualización de la documentación técnica y arquitectónica para reflejar el estado actual del proyecto.

### Validation

- Verificación de la conexión con la API de Groq.
- Ejecución funcional de TechDocAI.
- Carga y procesamiento de un documento PDF.
- Análisis del documento mediante `openai/gpt-oss-120b`.
- Generación del informe consolidado.
- Generación del resumen ejecutivo.

---

## [0.6.1] - 2026-08-12

### Changed

- Normalización de la configuración general del proyecto.
- Actualización de la versión de la aplicación a `0.6.1`.
- Sincronización de la versión entre `VERSION` y `config.py`.
- Normalización de las dependencias directas declaradas en `requirements.txt`.
- Eliminación de configuraciones redundantes o que ya no eran utilizadas directamente.
- Verificación de las dependencias mediante `pip check`.
- Verificación de compilación de los módulos principales mediante `compileall`.
- Validación de la ejecución funcional desde un clon limpio del repositorio.

### Validation

- Clon de la versión `v0.6.1` desde GitHub.
- Creación de un entorno virtual independiente.
- Instalación de las dependencias mediante `requirements.txt`.
- Configuración de la API de Groq mediante `.env`.
- Ejecución de TechDocAI.
- Carga y análisis de un documento PDF.
- Generación del informe consolidado.
- Generación del resumen ejecutivo.
- Exportación de resultados.

---

## [0.6.0] - 2026-08-12

### Changed

- Limpieza integral del proyecto.
- Eliminación de componentes obsoletos o que ya no formaban parte del flujo funcional.
- Eliminación de archivos y módulos que dejaron de utilizarse.
- Actualización de la estructura del proyecto después de la limpieza.

### Removed

- `app/core/processor.py`
- `app/utils/helpers.py`
- `prompts/conclusiones.txt`
- `prompts/preguntas.txt`
- `prompts/recomendaciones.txt`
- `tests/tests/__init__.py`

---

## [0.5.0]

### Added

- Generación de resumen ejecutivo a partir del análisis consolidado del documento.
- Integración del flujo de generación del resumen ejecutivo en la aplicación.
- Prompt específico para la generación del resumen técnico.

---

## [0.4.0]

### Added

- Funcionalidades de exportación y gestión de reportes.
- Exportación de los resultados del análisis a formatos de salida.
- Integración de los servicios necesarios para la generación de documentos.

---

## [0.3.0]

### Changed

- Evolución de la estructura funcional del proyecto.
- Consolidación de componentes relacionados con el procesamiento y análisis de documentos.

---

## [0.2.0]

### Changed

- Evolución de la arquitectura inicial del proyecto.
- Incorporación de componentes para la gestión estructurada de documentos.
- Consolidación progresiva del flujo de análisis documental.

---

## Versiones anteriores

Las etapas iniciales del desarrollo corresponden a la construcción progresiva del proyecto antes de las versiones actualmente documentadas mediante tags.

No se incorporan aquí versiones `v0.0.0` o `v0.1.0` como releases oficiales porque no han sido identificadas como tags oficiales en el historial utilizado para esta auditoría.

---

## Próxima versión

La siguiente versión se definirá después de completar las etapas pendientes de entrega, incluyendo:

- documentación técnica final;
- documentación de arquitectura;
- empaquetamiento de la aplicación;
- validación del paquete de distribución;
- preparación del material audiovisual;
- auditoría final del MVP.

La numeración de la próxima versión dependerá de los cambios que finalmente se incorporen.

---
