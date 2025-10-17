# 📡 TechComView SA

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code Quality](https://img.shields.io/badge/Code%20Quality-Pylint%20Passed-brightgreen.svg)](https://pylint.org)
[![Security](https://img.shields.io/badge/Security-SAST%20Analyzed-orange.svg)](https://owasp.org)
[![Status](https://img.shields.io/badge/Status-Development-yellow.svg)](https://github.com/airfranc86/Techcom-View-SA)

Dashboard interactivo para análisis de infraestructura de telecomunicaciones en el mundo.

[![GitHub stars](https://img.shields.io/github/stars/airfranc86/Techcom-View-SA?style=social)](https://github.com/airfranc86/Techcom-View-SA)
[![GitHub forks](https://img.shields.io/github/forks/airfranc86/Techcom-View-SA?style=social)](https://github.com/airfranc86/Techcom-View-SA)
[![GitHub issues](https://img.shields.io/github/issues/airfranc86/Techcom-View-SA)](https://github.com/airfranc86/Techcom-View-SA/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/airfranc86/Techcom-View-SA)](https://github.com/airfranc86/Techcom-View-SA/pulls)

## 🚀 Características

- **Dashboard Unificado**: Todas las funcionalidades en una sola página interactiva
- **Mapa Interactivo**: Visualización geográfica con Plotly integrada
- **Análisis Visual con IA**: Clasificación de imágenes satelitales usando ViT
- **Comparativas**: Análisis comparativo entre países integrado
- **Filtros Globales**: Afectan todas las visualizaciones simultáneamente

## 🔧 Calidad de Código

- **Pylint**: Análisis de calidad de código implementado
- **SAST**: Análisis de seguridad estática aplicado
- **PEP 8**: Cumplimiento de estándares de Python
- **Manejo de Excepciones**: Implementación robusta de errores
- **Type Hints**: Anotaciones de tipo para mejor legibilidad

## 📋 Requisitos

- Python 3.8+
- Streamlit 1.28+
- Dependencias listadas en `requirements.txt`

## 📁 Estructura del Proyecto

```
Techcom-View-SA/
├── app.py                      # Aplicación principal unificada
├── data/
│   ├── south_america_cells.csv # Datos originales
│   └── expanded_telecom_data.csv # Dataset expandido
├── requirements.txt            # Dependencias
├── README.md                   # Documentación
└── LICENSE                     # Licencia MIT
```


## 🔧 Mejoras de Calidad Implementadas

### Problemas Críticos Resueltos
- ✅ **Variable no definida en app.py**: Corregido error de variable usada antes de asignación
- ✅ **Manejo de excepciones mejorado**: Implementadas excepciones específicas en lugar de `Exception` genérico
- ✅ **Orden de imports corregido**: Reorganizados imports según estándares PEP 8

### Mejoras de Seguridad
- ✅ **Excepciones específicas**: `(OSError, ConnectionError, ValueError)` en lugar de `Exception`
- ✅ **Variables inicializadas**: Todas las variables tienen valores por defecto
- ✅ **Imports optimizados**: Eliminados imports no utilizados

### Mejoras de Mantenibilidad
- ✅ **Trailing whitespaces eliminados**: Código más limpio
- ✅ **Líneas largas divididas**: Mejor legibilidad
- ✅ **Variables renombradas**: Evitados conflictos de nombres
- ✅ **Type hints mejorados**: Mejor documentación del código


## 🎯 Funcionalidades del MVP

### ✅ Incluido
- Visualización de 10 países sudamericanos
- Mapa interactivo con Plotly
- Clasificación de imágenes con ViT
- Gráficos con Plotly
- Datos estáticos (CSV local)

## 📊 Datos

### 🌍 Países Incluidos (28 países)
**América del Sur**: Argentina, Bolivia, Brasil, Chile, Colombia, Ecuador, Paraguay, Perú, Uruguay, Venezuela, Guyana, Suriname, Guayana Francesa

**América Central**: México, Costa Rica, Panamá, Guatemala, Honduras, El Salvador, Nicaragua, Belice

**Caribe**: Cuba, República Dominicana, Haití, Jamaica, Trinidad y Tobago, Bahamas, Barbados

**América del Norte**: Estados Unidos

### 📋 Columnas Disponibles
- `country`: Nombre del país
- `total_cells`: Total de antenas
- `gsm`, `umts`, `lte`, `nr`: Antenas por tecnología (2G, 3G, 4G, 5G)
- `population_millions`: Población en millones
- `latitude`, `longitude`: Coordenadas geográficas
- `region`: Región geográfica (South America, Central America, Caribbean, North America)


## 🚀 Deploy en Streamlit Cloud

1. Subir código a repositorio público en GitHub
2. Conectar con Streamlit Community Cloud
3. Configurar `requirements.txt` en la raíz
4. La app principal debe estar en `app.py`

## 📈 Límites del MVP

- **Países**: Solo 10 de Sudamérica
- **Datos**: Estáticos (CSV local)
- **Páginas**: Máximo 4 en Streamlit
- **Tecnologías**: 2G, 3G, 4G, 5G

### Problemas de memoria
- Reducir tamaño de imágenes
- Usar `@st.cache_data` para datos
- Usar `@st.cache_resource` para modelos

## 📝 Desarrollo

### Reglas del MVP
1. Máximo 4 páginas en Streamlit
2. Solo datos CSV locales
3. Funciones <50 líneas
4. Comentarios en español

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT**. Ver [LICENSE](LICENSE) para más detalles.

## 📞 Soporte y Contacto

- 🐛 **Reportar bugs**: [Crear issue](https://github.com/airfranc86/Techcom-View-SA/issues)
- 💡 **Sugerir mejoras**: [Crear issue](https://github.com/airfranc86/Techcom-View-SA/issues)
- 📖 **Documentación**: Revisar este README
- 🔄 **Actualizaciones**: Ver commits recientes

## 🚀 Deploy en Producción

### Streamlit Cloud
1. Fork del repositorio
2. Conectar con [Streamlit Community Cloud](https://share.streamlit.io)
3. Configurar `requirements.txt`
4. Deploy automático


## 📊 Estadísticas del Proyecto

![GitHub last commit](https://img.shields.io/github/last-commit/airfranc86/Techcom-View-SA)
![GitHub language count](https://img.shields.io/github/languages/count/airfranc86/Techcom-View-SA)
![GitHub top language](https://img.shields.io/github/languages/top/airfranc86/Techcom-View-SA)

**Versión**: 2.1.0  
**Última actualización**: Octubre 2025  
**Estado**: ✅ Listo para producción  
**Repositorio**: [https://github.com/airfranc86/Techcom-View-SA](https://github.com/airfranc86/Techcom-View-SA)
