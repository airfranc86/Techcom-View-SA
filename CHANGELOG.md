# Changelog

Todos los cambios notables de este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-10-17

### Added
- Dashboard unificado con todas las funcionalidades
- Mapa interactivo con Plotly y configuración fija (Turbo + Carto Dark Matter)
- Dataset expandido con 28 países de América
- Análisis de telecomunicaciones por tecnología (2G, 3G, 4G, 5G)
- Filtros por región y país
- Visualizaciones con Plotly Express
- Sistema de métricas en tiempo real
- Clasificación de imágenes con IA (ViT)
- Análisis comparativo entre países
- Soporte para múltiples regiones geográficas

### Changed
- Migración de estructura multi-página a aplicación unificada
- Optimización de la interfaz de usuario
- Mejora en la gestión de datos
- Actualización de nombres de países a español (Brasil, Estados Unidos)

### Fixed
- Corrección de errores de linting (Pylint)
- Resolución de problemas de tipo de datos
- Optimización del manejo de excepciones
- Corrección de variables no definidas

### Security
- Implementación de análisis SAST
- Mejora en el manejo de excepciones específicas
- Eliminación de imports no utilizados
- Validación de variables

## [2.1.0] - 2025-10-16

### Added
- Estructura inicial del proyecto
- Dashboard básico con Streamlit
- Datos de 10 países sudamericanos
- Mapa interactivo básico
- Análisis de telecomunicaciones
- Sistema de páginas múltiples

### Technical Details
- Python 3.8+
- Streamlit 1.28+
- Plotly Express para visualizaciones
- Pandas para manejo de datos
- Transformers para IA