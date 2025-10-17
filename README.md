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

## 🛠️ Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/airfranc86/Techcom-View-SA.git
cd Techcom-View-SA
```

### 2. Crear entorno virtual
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación unificada
```bash
streamlit run app.py
```

**🎯 Nueva Estructura Unificada:**
- **Una sola página**: Todas las funcionalidades integradas
- **Filtros globales**: Afectan todas las visualizaciones
- **Navegación fluida**: Sin cambios de página
- **Interactividad completa**: Análisis en tiempo real

## 🔍 Análisis de Calidad

### Ejecutar Pylint
```bash
# Análisis completo
python -m pylint app.py data_loader.py image_classifier.py

# Análisis de páginas
python -m pylint pages/

# Con configuración específica
python -m pylint app.py --disable=C0114,C0116
```

### Verificar Sintaxis
```bash
# Verificar sintaxis de todos los archivos
python -m py_compile app.py
python -m py_compile data_loader.py
python -m py_compile image_classifier.py

# Verificar páginas
for file in pages/*.py; do python -m py_compile "$file"; done
```

### Tests de Funcionalidad
```bash
# Test de imports
python -c "import streamlit, pandas, plotly.express; print('✅ Imports OK')"

# Test de módulos locales
python -c "from data_loader import load_telecom_data; print('✅ data_loader OK')"
python -c "from image_classifier import load_vit_model; print('✅ image_classifier OK')"
```

## 📁 Estructura del Proyecto

```
Techcom-View-SA/
├── app.py                      # Aplicación principal unificada
├── data/
│   ├── south_america_cells.csv # Datos originales
│   └── expanded_telecom_data.csv # Dataset expandido
├── data_loader.py              # Carga de datos
├── image_classifier.py         # Clasificador ViT
├── requirements.txt            # Dependencias
├── README.md                   # Documentación
└── LICENSE                     # Licencia MIT
```

### 🗂️ Archivos Principales
- **`app.py`**: Dashboard unificado con todas las funcionalidades
- **`data/`**: Datasets de telecomunicaciones (28 países)
- **`data_loader.py`**: Gestión y carga de datos
- **`image_classifier.py`**: Clasificación de imágenes con IA

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

### Puntuaciones de Calidad
| Archivo | Antes | Después | Mejora |
|---------|-------|---------|--------|
| `app.py` | 6.74/10 | ✅ Sin errores | +3.26 |
| `data_loader.py` | 8.08/10 | ✅ Sin errores | +1.92 |
| `image_classifier.py` | 6.43/10 | ✅ Sin errores | +3.57 |
| `pages/` | Múltiples errores | ✅ Corregidos | +100% |

## 🎯 Funcionalidades del MVP

### ✅ Incluido
- Visualización de 10 países sudamericanos
- Mapa interactivo con Plotly
- Clasificación de imágenes con ViT
- Gráficos con Plotly
- Datos estáticos (CSV local)

### ❌ Fuera de Scope
- APIs externas en tiempo real
- Múltiples modelos de IA
- Exportación PDF
- Autenticación de usuarios
- Base de datos externa

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

## 🤖 Modelo de IA

- **Modelo**: Vision Transformer (ViT)
- **Versión**: google/vit-base-patch16-224
- **Propósito**: Clasificación de tipos de zona
- **Categorías**: Urbana, Residencial, Industrial, Rural, Comercial

## 🚀 Deploy en Streamlit Cloud

1. Subir código a repositorio público en GitHub
2. Conectar con Streamlit Community Cloud
3. Configurar `requirements.txt` en la raíz
4. La app principal debe estar en `app.py`

## 🔧 Comandos Útiles

```bash
# Ejecutar localmente
streamlit run app.py

# Limpiar caché
streamlit cache clear

# Ver logs
streamlit run app.py --logger.level debug
```

## 📈 Límites del MVP

- **Países**: Solo 10 de Sudamérica
- **Datos**: Estáticos (CSV local)
- **Páginas**: Máximo 4 en Streamlit
- **Modelo IA**: Solo 1 (ViT)
- **Tecnologías**: 2G, 3G, 4G, 5G

## 🐛 Solución de Problemas

### Error de carga de datos
```bash
# Verificar que el archivo CSV existe
ls data/south_america_cells.csv
```

### Error del modelo ViT
```bash
# Limpiar caché de Streamlit
streamlit cache clear
```

### Problemas de memoria
- Reducir tamaño de imágenes
- Usar `@st.cache_data` para datos
- Usar `@st.cache_resource` para modelos

## 📝 Desarrollo

### Reglas del MVP
1. Máximo 4 páginas en Streamlit
2. Solo datos CSV locales
3. Un solo modelo de IA
4. Funciones <50 líneas
5. Comentarios en español

### Estructura de commits
```
feat: nueva funcionalidad
fix: corrección de bug
docs: actualización de documentación
style: cambios de formato
```

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Para contribuir:

1. **Fork** del repositorio
2. **Crear** rama feature (`git checkout -b feature/nueva-funcionalidad`)
3. **Commit** con mensaje descriptivo (`git commit -m "feat: agregar nueva funcionalidad"`)
4. **Push** a la rama (`git push origin feature/nueva-funcionalidad`)
5. **Crear** Pull Request

### 📝 Convenciones de Commits
```
feat: nueva funcionalidad
fix: corrección de bug
docs: actualización de documentación
style: cambios de formato
refactor: refactorización de código
test: agregar o modificar tests
```

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

### Docker (Opcional)
```bash
# Crear Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## 📊 Estadísticas del Proyecto

![GitHub repo size](https://img.shields.io/github/repo-size/airfranc86/Techcom-View-SA)
![GitHub last commit](https://img.shields.io/github/last-commit/airfranc86/Techcom-View-SA)
![GitHub language count](https://img.shields.io/github/languages/count/airfranc86/Techcom-View-SA)
![GitHub top language](https://img.shields.io/github/languages/top/airfranc86/Techcom-View-SA)

**Versión**: 1.0.0  
**Última actualización**: Octubre 2025  
**Estado**: ✅ Listo para producción  
**Repositorio**: [https://github.com/airfranc86/Techcom-View-SA](https://github.com/airfranc86/Techcom-View-SA)
