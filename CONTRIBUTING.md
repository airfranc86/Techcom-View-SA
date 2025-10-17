# Guía de Contribución

¡Gracias por tu interés en contribuir a TechComView SA! 🚀

## 🚀 Cómo Contribuir

### 1. Fork del Repositorio
```bash
# Clonar tu fork
git clone https://github.com/tu-usuario/Techcom-View-SA.git
cd Techcom-View-SA

# Agregar upstream
git remote add upstream https://github.com/airfranc86/Techcom-View-SA.git
```

### 2. Crear una Rama
```bash
# Crear y cambiar a nueva rama
git checkout -b feature/nueva-funcionalidad
# o
git checkout -b fix/correccion-bug
```

### 3. Hacer Cambios
- Sigue las convenciones de código existentes
- Agrega comentarios en español
- Mantén funciones bajo 50 líneas
- Usa type hints cuando sea posible

### 4. Commit y Push
```bash
# Agregar cambios
git add .

# Commit con mensaje descriptivo
git commit -m "feat: agregar nueva funcionalidad de análisis"

# Push a tu fork
git push origin feature/nueva-funcionalidad
```

### 5. Crear Pull Request
- Ve a GitHub y crea un Pull Request
- Describe claramente los cambios
- Menciona cualquier issue relacionado

## 📝 Convenciones de Commits

Usamos [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: nueva funcionalidad
fix: corrección de bug
docs: actualización de documentación
style: cambios de formato (espacios, comas, etc.)
refactor: refactorización de código
test: agregar o modificar tests
chore: tareas de mantenimiento
```

### Ejemplos:
```bash
git commit -m "feat: agregar filtro por tecnología 5G"
git commit -m "fix: corregir error en cálculo de métricas"
git commit -m "docs: actualizar README con nuevas funcionalidades"
```

## 🔧 Estándares de Código

### Python
- **PEP 8**: Seguir estándares de Python
- **Type Hints**: Usar anotaciones de tipo
- **Docstrings**: Documentar funciones importantes
- **Imports**: Ordenar según PEP 8

### Streamlit
- **Widgets**: Usar nombres descriptivos
- **Caching**: Usar `@st.cache_data` para datos
- **Layout**: Usar columnas para organización

### Ejemplo de Función:
```python
def calculate_metrics(dataframe: pd.DataFrame) -> Dict[str, float]:
    """
    Calcula métricas de telecomunicaciones.
    
    Args:
        dataframe: DataFrame con datos de países
        
    Returns:
        Diccionario con métricas calculadas
    """
    total_cells: int = int(dataframe['total_cells'].sum())
    return {'total_cells': total_cells}
```

## 🧪 Testing

### Antes de Enviar PR:
```bash
# Verificar sintaxis
python -m py_compile app.py

# Ejecutar linting
pylint app.py --disable=C0114,C0116

# Probar imports
python -c "import streamlit, pandas, plotly.express"
```

## 📋 Checklist para PR

- [ ] Código sigue estándares PEP 8
- [ ] Funciones tienen type hints
- [ ] Comentarios en español
- [ ] Sin errores de linting
- [ ] Tests pasan
- [ ] Documentación actualizada
- [ ] Commit messages descriptivos

## 🐛 Reportar Bugs

### Usar Template de Issue:
```markdown
**Descripción del Bug**
Descripción clara del problema.

**Pasos para Reproducir**
1. Ir a '...'
2. Hacer clic en '...'
3. Ver error

**Comportamiento Esperado**
Qué debería pasar.

**Screenshots**
Si aplica, agregar capturas.

**Información Adicional**
- OS: Windows/Linux/Mac
- Python: 3.x
- Streamlit: x.x
```

## 💡 Sugerir Mejoras

### Usar Template de Feature:
```markdown
**Funcionalidad Sugerida**
Descripción clara de la mejora.

**Problema que Resuelve**
Qué problema soluciona.

**Solución Propuesta**
Cómo implementarías la mejora.

**Alternativas Consideradas**
Otras opciones evaluadas.
```

## 📚 Recursos

- [Streamlit Docs](https://docs.streamlit.io/)
- [Plotly Python](https://plotly.com/python/)
- [Pandas Docs](https://pandas.pydata.org/docs/)
- [PEP 8](https://pep8.org/)

## 🤝 Código de Conducta

- Sé respetuoso y constructivo
- Enfócate en el problema, no en la persona
- Ayuda a otros a aprender
- Celebra las contribuciones de otros

## 📞 Contacto

- **Issues**: [GitHub Issues](https://github.com/airfranc86/Techcom-View-SA/issues)
- **Discusiones**: [GitHub Discussions](https://github.com/airfranc86/Techcom-View-SA/discussions)

---

¡Gracias por contribuir! 🎉
